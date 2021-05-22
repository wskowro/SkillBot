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
        'Cool. Cool cool cool cool cool cool cool, ',
        'no doubt no doubt no doubt no doubt.',
        'Title of your sex tape.',
        'Sarge, with all due respect, I am gonna completely ignore everything you just said.',
        'I ate one string bean. It tasted like fish vomit. That was it for me.',
        'The English language can not fully capture the depth and complexity of my thoughts, so I’m incorporating emojis into my speech to better express myself. Winky face.',
        'A place where everybody knows your name is hell. You’re describing hell.',
        'Cool, cool, cool, cool, cool. No doubt, no doubt, no doubt.',
        'If I die, turn my tweets into a book.',
        'Fine. but in protest, I’m walking over there extremely slowly!',
        'Jake, why don’t you just do the right thing and jump out of a window?',
        'I asked them if they wanted to embarrass you, and they instantly said yes.',
        'Captain Wuntch. Good to see you. But if you’re here, who’s guarding Hades?',
        'I’m playing Kwazy Cupcakes, I’m hydrated as hell, and I’m listening to Sheryl Crow. I’ve got my own party going on.',
        'Anyone over the age of six celebrating a birthday should go to hell.',
        'Captain, turn your greatest weakness into your greatest strength. Like Paris Hilton RE: her sex tape.',
        'Jake, piece of advice: just give up. It’s the Boyle way. It’s why our family crest is a white flag.',
        'Okay, no hard feelings, but I hate you. Not joking. Bye.',
        'Hello unsolved case. Do you bring me joy? No, because you’re boring and you’re too hard. See ya.',
        'Great, I’d like your $8-est bottle of wine, please.',
        'I don’t want to hang out with some stupid baby who’s never met Jake.',
        'Well, no one asked you. It’s a self-evaluation.'
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
#no_result_message = '''Sorry, we can\'t find what you are searching for. We may not have written anything about it yet, 
#but you can subscribe to our news letter for updates of our newest content 
#--> https://runpee.com/about-runpee/runpee-movie-newsletter/'''
no_result_message = "Error"


@bot.event
async def on_message(message): 
  if message.author == client.user:
      return  
  # lower case message
  message_content = message.content.lower()  
    
  if f'!search' in message_content:

    key_words, search_words = page_web.key_words_search_words(message_content)
    result_links = page_web.search(key_words)
    links = page_web.send_link(result_links, search_words)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
  await bot.process_commands(message)
    
bot.run(TOKEN)
