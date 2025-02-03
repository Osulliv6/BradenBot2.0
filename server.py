from flask import Flask, request, jsonify
import requests
import time
import threading

app = Flask(__name__)

#YOU NEED TO CHANGE ALL OF THESE VALUES 
GROUPME_BOT_ID = "8706abc5070c17d8f3a3f4aeda" #created on the GroupMe Developers Account under bots 
GROUPME_GROUP_ID = "105781627"  # https://www.schmessage.com/IDFinder/ Links to the webiste to find the chatID
GROUPME_ACCESS_TOKEN = "QRBBArnPbV1BWAFemAdHEZQNP5HYZl4JeNXnTimf"  #Login to GroupMe developers account and hit access token 

def post_to_groupme(message):
    url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": GROUPME_BOT_ID, "text": message}
    response = requests.post(url, json=data)
    
    print("GroupMe Response:", response.text)

    if response.status_code == 202:
        time.sleep(2) 
        return get_last_message_id()  
    return None

def get_last_message_id():
    url = f"https://api.groupme.com/v3/groups/{GROUPME_GROUP_ID}/messages?token={GROUPME_ACCESS_TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "response" in data and "messages" in data["response"]:
            return data["response"]["messages"][0]["id"]  
    return None

def check_for_reactions(message_id):
    url = f"https://api.groupme.com/v3/groups/{GROUPME_GROUP_ID}/messages/{message_id}?token={GROUPME_ACCESS_TOKEN}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "response" in data and "message" in data["response"] and "favorited_by" in data["response"]["message"]:
            favorited_by = data["response"]["message"]["favorited_by"]
            print(f"Message reactions: {favorited_by}")
            return len(favorited_by) > 0  
    return False

def send_follow_up(message_id, original_message):
    time.sleep(300)  #5 minute delay for a warning message 
    
    if not check_for_reactions(message_id):
        print("No reactions found. Sending a follow-up message.")
        reminder_message = f"🚨 This company still hasn't been helped!! 🚨\n\n{original_message}"
        post_to_groupme(reminder_message)
    else:
        print("Message was reacted to. No follow-up needed.")

@app.route('/', methods=['POST'])
def webhook():
    """Handles incoming Google Forms data and posts to GroupMe."""
    formData = request.json  
    if formData is None:
        return jsonify({"status": "failure", "message": "No data received"}), 400

    header = "\nNew Company Request!\n"
    info = ""

    try:
        for field in formData.get("embeds", [])[0].get("fields", []):
            name = field.get("name", "Unknown Field")
            value = field.get("value", "No response")
            info += f"{name}: {value}\n"

        footer = "\n"  
        message_text = header + info + footer

        message_id = post_to_groupme(message_text)
        if message_id:
            print(f"Message sent successfully. Message ID: {message_id}")
            
            threading.Thread(target=send_follow_up, args=(message_id, message_text)).start()

        return jsonify({"status": "success", "message": "Posted to GroupMe"}), 200

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
