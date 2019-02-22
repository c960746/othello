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

# ŠÄããŠ—L˜ÒŽ© /callback “I Post Request
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
  
        if event.message.text == "123" :
        line_bot_api.reply_message(event.reply_token,TextSendMessage("???????"))   
        return 0

    return 0
    
    
       
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
