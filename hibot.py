from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'pxbH3Ap4j684pu9P0UESYf0jSpe3G2dPL/l88oLKu1fGHPRVmhPvph5Lt2v04kDXvd+bbjmSBPSyH/2WLtWt9sOXHfcBlQhbQ3WUn4WsJwAYnl1W8RjabGIRKuEKTR6232Va5uWycm0zBrfVcaN7YgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ae05c21de4d24de723d09aa4a64eb206')


@app.route('/')
def index():
    return "hi big"


"""
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
"""


@app.route("/callback", methods=['GET', 'POST'])
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

    if request.method == 'POST':
        return request.data
    elif request.method == 'GET':
        return request.gata

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    def testDate(test):
        if (test == 'gat') or (test == 'pat'):
            date = 'สอบ 24 – 27 กุมภาพันธ์ 2561'
        if (test == 'o-net') or (test == 'O-net') or (test == 'onet') or (test == 'Onet'):
            date = 'สอบ 3 – 4 มีนาคม 2561'

        return date

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="%s") % testDate(event.message.text))

    """if event.message.text == 'A':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Big sexy boy"))
    else:
        line_bot_api.reply_message(event.reply_token, TextMessage(text=event.message.text))
"""


if __name__ == "__main__":
    app.run()
