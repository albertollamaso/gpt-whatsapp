import serverless_wsgi
from flask import Flask,request,json
from twilio_client import twilio_send_message
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)



@app.route('/whatsapp', methods=['POST'])
def reply_whatsapp():

    source_phone = request.values["From"]
    source_msg = request.values["Body"]
    print("source_phone: " + source_phone)
    print("source_msg: " + source_msg)
    try:
        num_media = int(request.values.get("NumMedia"))
    except (ValueError, TypeError):
        return "Invalid request: invalid or missing NumMedia parameter", 400
    response = MessagingResponse()
    if not num_media:
        twilio_send_message(source_msg, source_phone)
    return str(response)

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
