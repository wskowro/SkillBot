import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
TOKEN = "NDk0MzMyMzkyMzQyMDI4MzA5.W6rs6g.6l1aohio33Qr8mzM8hHySLxoHNg"
GUILD = "Team Stealthy Bush"

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

    # just trying to debug here
    #for guild in client.guilds:
     #   for member in guild.members:
    #        print(member.name, ' ')

    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')
    
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
    
    response = "Hello, " + ctx.author.str()
    await ctx.send(response)
    
    
#client.run(TOKEN)
bot.run(TOKEN)
