import os
import openai
from dotenv import load_dotenv
from flask import Flask, request
from twilio.rest import Client 


app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
from_str=os.getenv("from")
to_str=os.getenv("to")


client = Client(account_sid, auth_token) 
 


@app.route('/bot', methods=['POST'])
def bot():
    
    try:
        incoming_msg = request.form.get("Body").lower()

        resp = openai.Completion.create(
        model="text-davinci-003",
        prompt=incoming_msg,
        temperature=0.3,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        
        quote = str(resp["choices"][0]["text"])

        message = client.messages.create( 
                                from_=from_str,  
                                body=quote,      
                                to=to_str
                            ) 
    
        
        # print(message.sid)


        return str(resp["choices"][0]["text"])

    except:
        quote = str("Erro 🤖")

        message = client.messages.create( 
                                from_=from_str,  
                                body=quote,      
                                to=to_str
                            ) 

    




if __name__ == '__main__':
   app.run(debug = True, port=8070)

