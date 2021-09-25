import os
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

sus_words = ["sussy", "Sussy", "sus", "Sus", "SUS"]

starter_sussy_replies = [
  "You Sussy little Baka!",
  "When imposter is SUS??!",
  "SUSSY AMOGUS?"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_sussy_replies(sussy_reply):
  if "sussy_replies" in db.keys():
    sussy_replies = db["sussy_replies"]
    sussy_replies.append(sussy_reply)
    db["sussy_replies"] = sussy_replies
  else:
    db["sussy_replies"] = [sussy_reply]

def delete_sussy_reply(index):
  sussy_replies = db["sussy_replies"]
  if len(sussy_replies) > index:
    del sussy_replies[index]
    db["sussy_replies"] = sussy_replies

def get_waifu():
  response = requests.get("https://api.waifu.pics/sfw/wink")
  json_data = json.loads(response.text)
  waifu = "*LOADING WINK...* \n " + json_data['url']
  return(waifu)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

TOKEN = os.environ['key']

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_sussy_replies
    if "sussy_replies" in db.keys():
      options.extend(db["sussy_replies"])
      # options = options + db["sussy_replies"]

    if any(word in msg for word in sus_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    sussy_reply = msg.split("$new ",1)[1]
    update_sussy_replies(sussy_reply)
    await message.channel.send("New reply added")

  if msg.startswith("$del"):
    sussy_replies = []
    if "sussy_replies" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_sussy_reply(index)
      sussy_replies = db["sussy_replies"]
    await message.channel.send(sussy_replies)

  if msg.startswith("$list"):
    sussy_replies = []
    if "sussy_replies" in db.keys():
      sussy_replies = db["sussy_replies"]
    await message.channel.send(sussy_replies)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() =="true":
      db["responding"]= False
      await message.channel.send("Responding is on")
    else:
      db["responding"]= False
      await message.channel.send("Responding is off")

  if message.content.startswith('$wink'):
    waifu = get_waifu()
    await message.channel.send(waifu)

# this keeps the webserver running
keep_alive()
client.run(TOKEN)