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


global wooo 
wooo = 0

global start 
start = 0     #0¥è•Â 1¥ŠJn

global answer 
ansewr = 0

global ansmuch
ansmuch = 0

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  global start
  global wooo
  global answer


  if start == 0 :
#..........................................
    if event.message.text == "Z–½" and len(event.message.text) == 2  :
            startqq =  random.randint(0,100)
            wooo = wooo+1
            if wooo > 3 :
               wooo = 0 
               line_bot_api.reply_message(event.reply_token,TextSendMessage("•ÊŠß‰ää˜ğšÓ{")) 
               return 0

            if startqq == 100:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("?‰^Ÿ†¢ŠEDŠÒ•s‹âÓÙ“§!!"))
               return 0

            if startqq == 0:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("‰^Ÿ†·”š —v‘e–å¿¬S˜Hç²–ì‹ç ?Ô –~Í Š……¿¬S?“"))
               return 0

            if startqq >0 and startqq <20:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("’´Š ”‡¥ÅŠ“I•Ê—¹"))
               return 0

            if startqq >=20 and startqq <40:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("¬Š ‘´›‰<Š>”‡ŒÂš”Oì<?>"))
               return 0

            if startqq >=40 and startqq <60:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("•’Ê ”‡•’ÊAæî‰ä“I_ˆÉˆêéâr"))
               return 0

            if startqq >=60 and startqq <80:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("‹g"))
               return 0

            if startqq >=80 and startqq <100:
               line_bot_api.reply_message(event.reply_token,TextSendMessage("‘å‹g ??"))
               return 0
#..........................................
    if event.message.text == "’·’Jì" :
        line_bot_api.reply_message(event.reply_token,TextSendMessage("???????"))   
        return 0
#..........................................
    if event.message.text == "wooo" :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(wooo))
        return 0
#..........................................
    if event.message.text == "ŠJnà£—VE" :
        start = 1
        line_bot_api.reply_message(event.reply_token,TextSendMessage("—VEŠJn¿—A“ü•sd•¡4ˆÊÉ"))
        list123 = [0,1,2,3,4,5,6,7,8,9]

        for i in range(9,-1,-1) :
          x = random.randint(0,9)
          list123[i] , list123[x] = list123[x] , list123[i]

        answer = list123[0]*1000 + list123[1]*100 + list123[2]*10 + list123[3]
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(answer))
        return 0
#..........................................

  if event.message.text == "‰ä’´à£‘zŠÅ“šˆÄ" and start == 1:
       start = 0
       if int(answer/1000) == 0:
          line_bot_api.reply_message(event.reply_token,TextSendMessage("0"+str(answer)))
          return 0
       line_bot_api.reply_message(event.reply_token,TextSendMessage(answer))
       return 0
#..........................................
  if start == 1 and len(event.message.text) == 4 :  
    aans = 0
    bans = 0
    list456 = [0,0,0,0]
    perans=int(event.message.text)
    
    
    list456[0] = int(perans/1000)
    list456[1] = int((perans%1000)/100)
    list456[2] = int(((perans%1000)%100)/10)
    list456[3] = int(((perans%1000)%100)%10)

    for i in range(0,4) :
        for j in range(i+1,4) : 
            if list456[i] == list456[j] :
               line_bot_api.reply_message(event.reply_token,TextSendMessage("‘zì•¾???"))
               return 0
    

    if int(perans/1000) == int(answer/1000) :
       aans =aans+1
    if int(perans/1000) == int((answer%1000)/100) :
       bans =bans+1 
    if int(perans/1000) == int(((answer%1000)%100)/10) :
       bans =bans+1 
    if int(perans/1000) == int(((answer%1000)%100)%10) :
       bans =bans+1
    
    if int((perans%1000)/100) == int(answer/1000) :
       bans =bans+1
    if int((perans%1000)/100) == int((answer%1000)/100) :
       aans =aans+1 
    if int((perans%1000)/100) == int(((answer%1000)%100)/10) :
       bans =bans+1 
    if int((perans%1000)/100) == int(((answer%1000)%100)%10) :
       bans =bans+1

    if int(((perans%1000)%100)/10) == int(answer/1000) :
       bans =bans+1
    if int(((perans%1000)%100)/10) == int((answer%1000)/100) :
       bans =bans+1 
    if int(((perans%1000)%100)/10) == int(((answer%1000)%100)/10) :
       aans =aans+1 
    if int(((perans%1000)%100)/10) == int(((answer%1000)%100)%10) :
       bans =bans+1

    if int(((perans%1000)%100)%10) == int(answer/1000) :
       bans =bans+1
    if int(((perans%1000)%100)%10) == int((answer%1000)/100) :
       bans =bans+1 
    if int(((perans%1000)%100)%10) == int(((answer%1000)%100)/10) :
       bans =bans+1 
    if int(((perans%1000)%100)%10) == int(((answer%1000)%100)%10) :
       aans =aans+1

    if aans == 4 :
       line_bot_api.reply_message(event.reply_token,TextSendMessage("—VEŒ‹‘©"))
       start = 0
       return 0

    line_bot_api.reply_message(event.reply_token,TextSendMessage(str(aans)+"A"+str(bans)+"B"))
    #line_bot_api.reply_message(event.reply_token,TextSendMessage(str(int(perans/1000))+"  "+str(answer/1000))) 
    return 0
    
    
       
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)