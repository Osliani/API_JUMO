from openai import OpenAI
import os, utils

client = OpenAI(api_key=os.environ.get("API_KEY"))

assistant = client.beta.assistants.create (
    name="Resumidor",
    instructions="Se te enviaran conversaciones entre un cliente y un asistente para que analices los aspectos mas importantes que se hablaron. Responderas con un texto que resuma toda la conversacion y quede bien definida la intencion del cliente.",
    model="gpt-4-1106-preview",
)

print(assistant.id)