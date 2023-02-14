import openai
import telegram

# Set up your OpenAI API key
openai.api_key = "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"

# Set up your Telegram bot token
bot = telegram.Bot(token="6165729604:AAFpWF-PKltmBBe91MasjjU72yaDZxs3Uac")

# Define a function to generate responses
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Define a function to handle incoming messages
def handle_message(update, context):
    message_text = update.message.text
    response_text = generate_response(message_text)
    update.message.reply_text(response_text)

# Set up a Telegram message handler
updater = telegram.ext.Updater(token="your-telegram-bot-token", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# Start the bot
updater.start_polling()
