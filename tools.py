from dotenv import load_dotenv
from getToken import *
from utils import *
from datetime import datetime, timedelta

function_json = {
    "name": "create_lead",
    "description": "Consulta el presupuesto con el que cuenta la empresa para iniciar negociaciones con el cliente.",
    "parameters": {
        "type": "object",
        "properties": {
            "email": {
                "type": "string",
                "description": "Correo del cliente interesado"
            },
            "name": {
                "type": "string",
                "description": "Nombre del cliente interesado"
            }
        },
        "required": ["email", "name"]
    }
}

load_dotenv()
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

assistant = client.beta.assistants.update(
    ASSISTANT_ID,
    tools=[
        {"type": "function", "function": function_json},
    ],
)
show_json(assistant)





