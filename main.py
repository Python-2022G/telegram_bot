from telegram import Bot
import os 

# Get the token from the environment variables
TOKEN = os.environ['TOKEN']
# Create a bot object
bot = Bot(TOKEN)
# Print the bot info


# AgACAgIAAxkBAAM7Y8ff0rHRcCSf2BBKaHnwsZt0Rt0AAovCMRtA6kFKibAqEiqrfHoBAAMCAANzAAMtBA
print(bot.sendPhoto('1258594598',
    'AgACAgIAAxkBAAM7Y8ff0rHRcCSf2BBKaHnwsZt0Rt0AAovCMRtA6kFKibAqEiqrfHoBAAMCAANzAAMtBA'))
