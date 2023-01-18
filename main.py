from telegram import Bot
import os 
import time

# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(TOKEN)
# Print the bot info
# 1258594598


def main():
    last_update = bot.getUpdates()
    last_update_id = last_update['update_id']

    while True:
        curr_update = bot.getUpdates()
        curr_update_id = curr_update['update_id']
        
        if curr_update_id != last_update_id:
            chat_id = curr_update['message']['from']['id']

            keys = list(curr_update['message'].keys())
            
            if 'sticker' in keys:
                file_id = curr_update['message']['sticker']['file_id']
                bot.sendSticker(chat_id, file_id)
                last_update_id = curr_update_id
            elif 'photo' in keys:
                file_id = curr_update['message']['photo'][0]['file_id']
                bot.sendPhoto(chat_id, file_id)
                last_update_id = curr_update_id
            elif 'text' in keys:
                text = curr_update['message']['text']
                bot.sendMessage(chat_id, text)
                last_update_id = curr_update_id


        time.sleep(1)

main()