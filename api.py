from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import utils, mongo, os

load_dotenv()

def crear_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
    ASSISTANT_ID = os.getenv("ASSISTANT_ID")
    
    
    @app.before_request
    def restrict_domains():
        host = request.headers.get('Host')
        if not host.startswith('jumotech.com'):
            return jsonify({'error': 'Acceso denegado','message': 'El dominio no es válido', 'status_code': 403})
            

    @app.route('/chat', methods=['POST'])
    def chat_reply():
        user_id = request.values.get('id').strip()
        incoming_msg = request.values.get('message', '').strip()
        thread_id = mongo.get_thread(user_id)
        if not thread_id:
            thread_id = mongo.create_thread(user_id)

        print("Mensaje Recibido!")
        print(f"- User: {incoming_msg}")
        
        try:
            ans = utils.submit_message(incoming_msg, thread_id, ASSISTANT_ID)
        except Exception as error:
            print(f"Historial reseteado por el siguiente error: {error}")
            thread_id = mongo.create_thread(user_id)
            ans = utils.submit_message(incoming_msg, thread_id, ASSISTANT_ID)
        
        interactions = mongo.get_interactions(user_id)
        
        return jsonify({'message': ans, 'status_code': 200, 'interactions': interactions})
        
    return app

if __name__ == '__main__':
    app = crear_app()
    app.run(debug=True, host='0.0.0.0', port=3028)
