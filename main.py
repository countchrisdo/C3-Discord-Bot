import os
import discord
import requests
import json
from discord.ext import commands
# importing replit database
# from replit import db
from keep_alive import keep_alive
import music

cogs = [music]

client = discord.Client()

# client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_waifu():
  response = requests.get("https://api.waifu.pics/sfw/wink")
  json_data = json.loads(response.text)
  waifu = "*LOADING WINK...* \n " + json_data['url']
  return(waifu)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$wink'):
    waifu = get_waifu()
    await message.channel.send(waifu)

# this keeps the webserver running
keep_alive()
#add music player cog
bot.add_cog(Player(bot))
#Use TOKEN variable to run bot (keep secret)
TOKEN = os.environ['key']
client.run(TOKEN)
bot.run(TOKEN)