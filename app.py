"""
    Example Flask app illustrating the use of JWT using EC public key signatures
    JWT algorithm is ES256 = EC P-256 DSA with SHA-256
    Network transport is HTTPS
"""

from flask import Flask, Response, request, jsonify
import jwt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from datetime import datetime
import re
import base64
import ssl

context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

app = Flask(__name__)

#app.config['JWT_SECRET_KEY'] = 'top secret!'  # CHANGE THIS!
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 60
app.config['JWT_ALGORITHM'] = 'ES256'
app.config['JWT_PUBLIC_KEY'] = open('ec-pub.key','r').read()
app.config['JWT_PRIVATE_KEY'] = open('ec.key','r').read()

jwtManager = JWTManager(app)

@app.route("/")
def home():
    return Response("Hello, Flask!")

@app.route('/auth', methods=['POST'])
def auth():
    accessToken = None
    datetime.time
    if not request.is_json:
        return jsonify({'msg' : 'Request is not JSON encoded'}), 400
    subjectUUID = request.json.get('subjectUUID', None)
    credentials = request.json.get('credentials', None)
    if not subjectUUID:
        return jsonify({'msg' : 'Request is missing subjectUUID'}), 400
    if not credentials:
        return jsonify({'msg': 'Request is missing credentials'}), 400
    if authenticate(subjectUUID, credentials):
        accessToken = create_access_token(identity=subjectUUID)
    return jsonify(accessToken), 200

# CHANGE THIS!
# AuthN mock-up: auth succeeds with any non-None subject and creds
def authenticate(subject, credentials):
    isSuccess = False
    if subject != None and credentials != None:
        isSuccess = True
    return isSuccess

@app.route("/secure")
@jwt_required
def secure():
    subjectUUID = get_jwt_identity()
    return jsonify(logged_in_as=subjectUUID), 200

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return Response(content)

if __name__ == "__main__":
    app.run("0.0.0.0", port=443, debug=True, ssl_context=context)
