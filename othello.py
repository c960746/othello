import requests

import re

import random

from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (
InvalidSignatureError
)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageSendMessage)


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('x49A0ZbuY2RE8BxTthzM4wIg4XnwavPosNJL3oGh/RxOOSHAwHiXL53cDNSMN1uxB18tW4C5fajGPDlmUeomHHg1DX+JuwTOfX/ZmIhQhlQPnXq/28lwGUgIPag1HJPsh+eLcUMIsMgBk7TvlAmMWAdB04t89/1O/w1cDnyilFU=')


# Channel Secret
handler = WebhookHandler('5fcc70c48caf46c18b81d2cb910803bb')

# ŠÄããŠ—L˜Ò© /callback “I Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  
    if event.message.text == "123" and len(event.message.text) == 2  :
            startqq =  random.randint(0,100)
            wooo = wooo+1
            if wooo > 3 :
               wooo = 0 
               line_bot_api.reply_message(event.reply_token,TextSendMessage("1")) 
               return 0

            if startqq == 100:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("2"))
               return 0

            if startqq == 0:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("3"))
               return 0

            if startqq >0 and startqq <20:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("4"))
               return 0

            if startqq >=20 and startqq <40:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("5"))
               return 0

            if startqq >=40 and startqq <60:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("6"))
               return 0

            if startqq >=60 and startqq <80:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("7"))
               return 0

            if startqq >=80 and startqq <100:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("8"))
               return 0

    return 0
    
    
       
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)