from flask import Flask
import telebot
import requests
import os

app = Flask(__name__)

Mytext = '''
✅ Download any videos ✅
✅ video facebook
✅ video pinterest
✅ video instgram
✅ video tiktok
✅ video shorts youtube
'''

bot = telebot.TeleBot("YourTokenBot")

@app.route('/', methods=['POST'])
def index():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200
def downvideo(link):
    url = link
    local_file_name = "newvideo.mp4"

    response = requests.get(url)

    if response.status_code == 200:
        with open(local_file_name, "wb") as local_file:
            local_file.write(response.content)
        print("File downloaded successfully.")
    else:
        print("Failed to download the file. Status code:", response.status_code)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, Mytext)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id

    if "facebook" in message.text:
        bot.send_message(chat_id, "wait for send the video ...")
        r = requests.get(f'https://anyshare-1.powerbots.repl.co/down?url={message.text}')
        r_json = r.json()
        vid = r_json.get("facebook")
        downvideo(vid)
        name_videos = 'newvideo.mp4'
        video_ = open(name_videos, 'rb')
        bot.send_video(chat_id, video_)
        os.remove(name_videos)

    elif "pin" in message.text:
        bot.send_message(message.chat.id, "wait for send the video ...")
        r=requests.get(f'https://anyshare-1.powerbots.repl.co/down?url={message.text}')
        r_json=r.json()
        vid=r_json.get("pinvid")
        downvideo(vid)
        name_videos='newvideo.mp4'
        video_=open(name_videos,'rb')
        bot.send_video(message.chat.id,video_)
        os.remove(name_videos)
    elif "instagram" in message.text:
        bot.send_message(message.chat.id, "wait for send the video ...")
        r=requests.get(f'https://anyshare-1.powerbots.repl.co/down?url={message.text}')
        r_json=r.json()
        vid=r_json.get("instavid")
        downvideo(vid)
        name_videos='newvideo.mp4'
        video_=open(name_videos,'rb')
        bot.send_video(message.chat.id,video_)
        os.remove(name_videos)
    elif "tiktok" in message.text:
        bot.send_message(message.chat.id, "wait for send the video ...")
        r=requests.get(f'https://anyshare-1.powerbots.repl.co/down?url={message.text}')
        r_json=r.json()
        vid=r_json.get("tiktok")
        downvideo(vid)
        name_videos='newvideo.mp4'
        video_=open(name_videos,'rb')
        bot.send_video(message.chat.id,video_)
        os.remove(name_videos)
    elif "youtube" in message.text:
        bot.send_message(message.chat.id, "wait for send the video ...")
        r=requests.get(f'https://anyshare-1.powerbots.repl.co/down?url={message.text}')
        r_json=r.json()
        vid=r_json.get("shorts")[0].get('vid')
        downvideo(vid)
        name_videos='newvideo.mp4'
        video_=open(name_videos,'rb')
        bot.send_video(message.chat.id,video_)
        os.remove(name_videos)


bot.polling()


app.run(host='0.0.0.0', port=81)
