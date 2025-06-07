from telegram.ext import Updater, CommandHandler
import requests
import json

# Replace YOUR_TOKEN_HERE with your real token
updater = Updater(token='7697628750:AAGsDFmCjrCGUDSYZet5E_A37a3_32iZQr0', use_context=True)
dispatcher = updater.dispatcher

# /hello command
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

# Register the /hello command
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

# /summary command
def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if response.status_code == 200:
        data = response.json()
        global_data = data['Global']
        message = (
            f"🌍 Global COVID-19 Stats:\n\n"
            f"New Confirmed: {global_data['NewConfirmed']}\n"
            f"Total Confirmed: {global_data['TotalConfirmed']}\n"
            f"New Deaths: {global_data['NewDeaths']}\n"
            f"Total Deaths: {global_data['TotalDeaths']}\n"
            f"New Recovered: {global_data['NewRecovered']}\n"
            f"Total Recovered: {global_data['TotalRecovered']}"
        )
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")

# Register the /summary command
summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(summary_handler)

# Start polling for messages
updater.start_polling()
