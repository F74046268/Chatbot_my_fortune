from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('r2BcuqIisuf4Moyjlwmm/2/ueyiDo/RTTusb7sDPt9Qjh1K0Gux2PYtepTiumK3YUHq2Z0+0HycZ3bhcJMvd47yJy6vEKw2+J0KrRIemyjbtwS2hebmFAmptZfotH6ws7+HS1OoJa+AILS0ASlTsSAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('cf3811f5926d15baa385d96a803228e7')

# 監聽所有來自 /callback 的 Post Request
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
    message = TextSendMessage(text='Hello moto yoooo')
    line_bot_api.reply_message(
        event.reply_token,
        message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
