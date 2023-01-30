import os
import openai
from dotenv import load_dotenv
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse 


app = Flask(__name__)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

 


@app.route('/bot', methods=['POST'])
def bot():
    
    try:
        incoming_msg = request.form.get("Body", '').lower()


        resp_gpt = openai.Completion.create(
        model="text-davinci-003",
        prompt=incoming_msg,
        temperature=0.3,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
        
        quote = str(resp_gpt["choices"][0]["text"])


        resp = MessagingResponse()
        msg = resp.message()

        msg.body(str(quote))
       

        return str(resp)



    except:
        quote = str("Erro 🤖")

        msg.body(str(quote))

    




if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8070)

