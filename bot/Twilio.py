from twilio.rest import Client
from LogDBHandler import LogDBHandler
 
class Twilio:

    def send_sms(msg, to):
        try:
            sid = "AC24dba720f479f16657c3f21328204b32"
            auth_token = "f471fd9b94fc6b55fb6695250ca9d59f"
            twilio_number = "HKLEGENDA"
            client = Client(sid, auth_token)
            message = client.messages.create(body=msg,from_=twilio_number,to=to,)
            LogDBHandler.log(Actions.sms, "sms", to, msg, "sucess", "bot") 
        except Exception as e:
            LogDBHandler.log(Actions.sms, "sms", to, msg, "fail", "bot", "",str(e.message).replace("/","//").replace("'","\""))