import os
import discord
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_waifu():
  response = requests.get("https://api.waifu.pics/sfw/wink")
  json_data = json.loads(response.text)
  waifu = json_data['url'] + " -"
  return(waifu)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

TOKEN = os.environ['key']

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

client.run(TOKEN)