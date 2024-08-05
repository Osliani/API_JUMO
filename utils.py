from dotenv import load_dotenv
from openai import OpenAI
import os, time, json, mongo, requests
from getToken import get_oauth_token

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def show_json(obj):
    print(json.loads(obj.model_dump_json()))
    
    
def wait_on_run(run, thread_id):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id = thread_id,
            run_id = run.id,
        )
        time.sleep(0.5)
    return run


def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()
    

def add_message(message, thread_id):
    message_object = client.beta.threads.messages.create (
        thread_id = thread_id, 
        role = "user", 
        content = message
    )
    return message_object


def add_assistant(assistant_id, thread_id):
    run = client.beta.threads.runs.create (
        thread_id = thread_id,
        assistant_id = assistant_id,
    )
    return run


def get_response(thread_id, message_object):
    response = client.beta.threads.messages.list(thread_id=thread_id, order="asc", after=message_object.id)
    ans = ""
    for r in response:
        ans += f"{r.content[0].text.value}\n"

    return ans


def resume_chat(user_id):
    chats = mongo.get_chat(user_id)
    history = ""
    for chat in chats:
        history += f"{chat['role']}: "
        history += f"{chat['message']} \n"
        
    thread = client.beta.threads.create()
    message_object = add_message(history, thread.id)
    RESUME_ASSISTANT_ID = os.getenv('RESUME_ASSISTANT_ID')
    run = add_assistant(RESUME_ASSISTANT_ID, thread.id)
    run = wait_on_run(run, thread.id)
    resume_history = get_response(thread.id, message_object)
    return resume_history
    
    
def create_lead(name, email, resume):
    lead_details = {
        "name": f"Jumoweb - {name}",
        "email": email,
        "message": resume,
    }
    
    token = get_oauth_token()
    
    form_data = {
        "model": "crm.lead",
        "method": "create",
        "args": json.dumps([
            {
                "stage_id": 1,
                "type": "opportunity",
                "name": f"JUMOWEB {lead_details['name']}",
                "email_from": lead_details["email"],
                "description": lead_details["message"],
            }
        ])
    }
    
    headers = {"Authorization": f"Bearer {token['access_token']}"}

    response = requests.post(
        "https://odoo.jumotech.com/api/v2/call",
        headers=headers,
        data=form_data,
    )

    if response.status_code == 200:
        data = response.json()
        print(data)
        return "El equipo de ventas se pondrá en contacto contigo proximamente."
    else:
        raise Exception(f"Error: {response.status_code}")
    
    
        
    
def submit_message(message:str, thread_id, assistant_id, user_id):
    message_object = add_message(message, thread_id)
    run = add_assistant(assistant_id, thread_id)
    run = wait_on_run(run, thread_id)
    
    if run.status == 'completed':
        return get_response(thread_id, message_object)
    else:
        print(run.status)
        tool_call = run.required_action.submit_tool_outputs.tool_calls[0]
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print("Function Name:", function_name)
        print(f"Function Arguments: {arguments}")
        
        tool_ans = ""
        if function_name == "create_lead":
            resume = resume_chat(user_id)
            print(f"Resumen: {resume}")
            tool_ans = create_lead(**arguments, resume=resume)
            #tool_ans = "El equipo de ventas se pondrá en contacto contigo proximamente."
        
        #enviar la respuesta de la tool
        try:
            run = client.beta.threads.runs.submit_tool_outputs_and_poll(
                thread_id = thread_id,
                run_id = run.id,
                tool_outputs = [{
                    "tool_call_id": tool_call.id,
                    "output": tool_ans,
                }],
            )
            print("Tool outputs submitted successfully.")
        except Exception as e:
            print("Failed to submit tool outputs:", e)
        
        #generar la respuesta del modelo
        run = wait_on_run(run, thread_id)
        return get_response(thread_id, message_object)
        