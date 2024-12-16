from SANKIRIGHT import SANKIRIGHT as app
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random
import pymongo
import os
import logging
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from config import BOT_TOKEN, MONGO_URL, OWNER_ID

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# MongoDB setup
client = pymongo.MongoClient(MONGO_URL)
db = client['telegram_bot']
groups_collection = db['groups']
photos_collection = db['photos']
captions_collection = db['captions']

# Initialize the bot
updater = Updater(BOT_TOKEN, use_context=True)
scheduler = BackgroundScheduler()

# Function to send random message and photo
def send_random_message_and_photo(context: CallbackContext):
    group_ids = [group['chat_id'] for group in groups_collection.find()]
    if not group_ids:
        return

    for group_id in group_ids:
        # Get random photo
        photos = list(photos_collection.find())
        if photos:
            photo = random.choice(photos)
            photo_file = photo['file_path']
            context.bot.send_photo(chat_id=group_id, photo=InputFile(photo_file))

        # Get random caption
        captions = list(captions_collection.find())
        if captions:
            caption = random.choice(captions)
            context.bot.send_message(chat_id=group_id, text=caption['text'])

# Command to add photo
def add_photo(update: Update, context: CallbackContext):
    if str(update.effective_user.id) != OWNER_ID:
        update.message.reply_text("You are not authorized to use this command.")
        return

    if update.message.reply_to_message and update.message.reply_to_message.photo:
        file_id = update.message.reply_to_message.photo[-1].file_id
        new_file = context.bot.get_file(file_id)
        file_path = f'photos/{file_id}.jpg'
        new_file.download(file_path)

        photos_collection.insert_one({'file_path': file_path})
        update.message.reply_text("Photo added successfully!")
    else:
        update.message.reply_text("Please reply to a photo to add it.")

# Command to add caption
def add_caption(update: Update, context: CallbackContext):
    if str(update.effective_user.id) != OWNER_ID:
        update.message.reply_text("You are not authorized to use this command.")
        return

    if context.args:
        caption_text = ' '.join(context.args)
        captions_collection.insert_one({'text': caption_text})
        update.message.reply_text("Caption added successfully!")
    else:
        update.message.reply_text("Please provide a caption.")

# Command to add group
def add_group(update: Update, context: CallbackContext):
    group_id = update.effective_chat.id
    if groups_collection.find_one({'chat_id': group_id}) is None:
        groups_collection.insert_one({'chat_id': group_id})
        update.message.reply_text("Group added successfully!")
    else:
        update.message.reply_text("This group is already added.")

# Start the scheduler
scheduler.add_job(send_random_message_and_photo, 'cron', hour='7,22')  # 7 AM and 10 PM
scheduler.start()

# Handlers
updater.dispatcher.add_handler(CommandHandler('addpic', add_photo))
updater.dispatcher.add_handler(CommandHandler('addcptn', add_caption))
updater.dispatcher.add_handler(CommandHandler('addgroup', add_group))
