# -*- coding: utf-8 -*-
# File: Alan__Bot
# Author: Alain Nishimwe <nishimwealain6l@gmail.com>
# CreateDate: 05-01-2020

# imports of Libraries

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

# Bot creation

englishBot = ChatBot("Chatterbot",
                     storage_adapter="chatterbot.storage.SQLStorageAdapter",
                     database_uri='postgres://qlkujblnysripk:e659e674392cfe433b0da15bb102346b8620fb72b5c4562a1a8d7a1849fbd228@ec2-184-72-235-159.compute-1.amazonaws.com:5432/dcvk7t170hi327',
                     logic_adapters=[
                         {
                             'import_path': 'chatterbot.logic.BestMatch',
                             'default_response': 'I am sorry, but I do not understand.',
                             'maximum_similarity_threshold': 0.60
                         }])

# training the bot for cavendish admission

trainer = ChatterBotCorpusTrainer(englishBot)

trainer.train("./corpus/")

# define app routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
# function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))


if __name__ == "__main__":
    app.run()
