from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from dotenv import load_dotenv
import utils, mongo, os
from waitress import serve

load_dotenv()

def crear_app():
    app = Flask(__name__)
    CORS(app)
    app.secret_key = os.urandom(24)
    JUMO_ASSISTANT_ID = os.getenv("JUMO_ASSISTANT_ID")
    
    
    @app.before_request
    def before_request():
        token = request.headers.get('token')
        if token != os.getenv("TOKEN_API"):
            print("Token inválido.")
            abort(401)
    
    
    @app.route('/chat', methods=['POST'])
    def chat_reply():
        user_id = str(request.values.get('id')).strip()
        incoming_msg = str(request.values.get('message')).strip()
        thread_id = mongo.get_thread(user_id)
        if not thread_id:
            thread_id = mongo.create_thread(user_id)

        print("Mensaje Recibido!")
        print(f"- User: {incoming_msg}")
        mongo.update_chat(user_id, "User", incoming_msg)
        
        try:
            ans = utils.submit_message(incoming_msg, thread_id, JUMO_ASSISTANT_ID, user_id)
        except Exception as error:
            print(f"Error: {error}")
            thread_id = mongo.create_thread(user_id)
            print(f"Historial Reseteado.")
            ans = utils.submit_message(incoming_msg, thread_id, JUMO_ASSISTANT_ID, user_id)
        
        print("Respuesta Enviada!")
        print(ans)
        mongo.update_chat(user_id, "Assistant", ans)
        interactions = mongo.get_interactions(user_id)
        return jsonify({'message': ans, 'status_code': 200, 'interactions': interactions})
        
    return app


if __name__ == '__main__':
    app = crear_app()
    #app.run(debug=True, host='0.0.0.0', port=3028)
    serve(app, host='0.0.0.0', port=3028)
