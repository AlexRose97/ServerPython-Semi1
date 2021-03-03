# pip3 install flask
# pip3 install boto3
import boto3
from credenciales import aws_keys
from flask import Flask, jsonify, request
import base64
app = Flask(__name__)


credRekognition = aws_keys.get('rekognition')

# Ruta inicio server
@app.route('/')
def hello_world():
    return '<center><h1>Servidor Activo</h1><h2>Alex - 201602999</h2></center>'

# Ruta tarea 3
@app.route('/tarea3-201602999', methods=['POST'])
def reconocerTags():
    rekognition_client = boto3.client(
        'rekognition', aws_access_key_id=credRekognition.get('accessKeyId'),
        aws_secret_access_key=credRekognition.get('secretAccessKey'),
        region_name=credRekognition.get('region'))


    consulta = rekognition_client.detect_labels(
        Image={'Bytes': base64.b64decode(request.json['Image'])}, MaxLabels=10)

    return jsonify(consulta)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
