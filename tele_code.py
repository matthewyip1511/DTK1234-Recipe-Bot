#import packages required for the running of this bot
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import datetime
import json
import random
#hello

tele_id = "placeholder for tele id"

updater = Updater(tele_id, use_context=True)

#declare some variables to be used later
dish = [""]
recipes = {"Fried Rice" : "recipe placeholder", "Ramen" : "recipe placeholder", "Curry Chicken" : "recipe placeholder", 
           "Chicken Chop" : "recipe placeholder", "Mac n Cheese" : "recipe placeholder", "Carbonara" : "recipe placeholder" }

#functions to support the initialisation
def start(update: Update, context: CallbackContext):
    #write down the note to be shown to the user when the start is launched
    message = "Hello, welcome to the AI recipe bot. You can use this bot for suggestions on what to cook each day!\n\nTo begin using this bot, press /begin" 
    
    update.message.reply_text(message)
    print('user started the bot!')

def begin(update: Update, context: CallbackContext):
    message = "Welcome to the recipe bot! What would you like to eat today?\n\n/asian\n/western\n/vegetarian"

    #print out the message
    update.message.reply_text(message)
    print("user pressed begin!")
    

def help(update: Update, context: CallbackContext):
    #tells the user what the bot is about and what they can do with it
    update.message.reply_text("This bot can be used to suggest ideas for what to cook each day, along with the recipes to cook such dishes!")


#functions to support churning out the recipe
def asian(update: Update, context: CallbackContext):
    options = ["Fried Rice", "Ramen", "Curry Chicken"]

    #return a random dish from the basket of options 
    item = options[random.randint(0,2)]
    dish[0] = item

    message = "Well, today is a good day for " + item + ", don't you think? \n:)\n \n\nIf you need a recipe for this dish, you can click /recipe"

        
    update.message.reply_text(message)

def western(update: Update, context: CallbackContext):
    options = ["Chicken Chop", "Mac n Cheese", "Carbonara"]

    #return a random dish from the basket of options 
    item = options[random.randint(0,2)]
    dish[0] = item

    message = "Well, today is a good day for " + item + ", don't you think? \n:)\n \n\nIf you need a recipe for this dish, you can click /recipe"

        
    update.message.reply_text(message)

def vegetarian(update: Update, context: CallbackContext):
    options = ["Vegetarian Curry", "Stir fry bee hoon", "Nasi Goreng with egg"]

    #return a random dish from the basket of options 
    item = options[random.randint(0,2)]
    dish[0] = item

    message = "Well, today is a good day for " + item + ", don't you think? \n:)\n \n\nIf you need a recipe for this dish, you can click /recipe"

        
    update.message.reply_text(message)


def recipe(update: Update, context: CallbackContext):
    r = recipes[dish[0]]  #get the recipe for this current dish out from the dict of recipes

    update.message.reply_text(r)



def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  

#to handle incoming commands
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('begin', begin))
updater.dispatcher.add_handler(CommandHandler('asian', asian))
updater.dispatcher.add_handler(CommandHandler('western', western))
updater.dispatcher.add_handler(CommandHandler('vegetarian', vegetarian))
updater.dispatcher.add_handler(CommandHandler('recipe', recipe))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands

#line to deal with texts i
updater.dispatcher.add_handler(MessageHandler(Filters.text, texts))
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

#start running the bot proper
updater.start_polling()
