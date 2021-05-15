import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
import os
import searchPage

load_dotenv('discordToken.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild: \n' 
        f'{guild.name} (id: {guild.id})'
    )
    
bot = commands.Bot(command_prefix='!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)
    

@bot.command(name='hello', help='Commands thr bot to greet you')
async def helloBot(ctx):
    
    response = 'Hello, ' + ctx.author.name
    await ctx.send(response)


# instantiate RunPeeWeb class from search_runpee.py
page_web = searchPage.RunSearchPage()

# no result message 
no_result_message = '''Sorry, we can\'t find what you are searching for. We may not have written anything about it yet, 
but you can subscribe to our news letter for updates of our newest content 
--> https://runpee.com/about-runpee/runpee-movie-newsletter/'''


@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  

  
  if message.content.startswith(f'$hello'):
    await message.channel.send('Hello there! I\'m the bad robot you fart face.')
    
  if f'$search' in message_content:

    key_words, search_words = page_web.key_words_search_words(message_content)
    result_links = page_web.search(key_words)
    links = page_web.send_link(result_links, search_words)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
    
    
#client.run(TOKEN)
bot.run(TOKEN)
