from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    # Mantivemos a mensagem original da sua Semana 4
    return "<h1>🚀 DOCKER FUNCIONANDO!</h1><p>Semana 4 ✅</p>"

@app.route('/status')
def status():
    return jsonify({"status": "online", "message": "API operando normalmente"}), 200

@app.route('/info')
def info():
    return jsonify({"projeto": "DevOps", "fase": "Parte 2", "testes": "Pytest"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)