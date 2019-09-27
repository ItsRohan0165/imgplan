import discord
from discord.ext import commands
import random

from googleapiclient.discovery import build
import pprint
import asyncio
import os


description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='/',description=description)

@bot.event
async def on_ready():
   await client.send_message('614784025973751808', 'restarted...')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(bot)

@bot.command()
async def google(*text: str):
    finaltext = ' '
    for word in text:
        finaltext = finaltext + word  + " "
    
    api_key = "AIzaSyDWpZCMkyw6g-VackfIQ-zqIZwXpxxoC6w"
    cse_id = "002090988512210948953:3llemhwwasw"
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']    
    results = google_search(finaltext, api_key, cse_id, num=3)
    for result in results:
        formatText="*" + result['snippet'] + "*"
        await bot.say(formatText)
@bot.command()
async def img(*text : str):
    print('got here')

    """Searches google for an image described by input"""
    finaltext = " "
    
    for word in text:
        finaltext = finaltext + word + " "
    
    api_key = "AIzaSyDEI9ei37MeTgaDyQhayyXSdHPM8ZJ4Gfk"
    cse_id = "001464282721790659668:_ja4f_we2rk"

    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        pprint.pprint(res)
        return res['items']

    results = google_search(finaltext, api_key, cse_id, num=1, searchType= 'image')
    for result in results:
        formatText = "" + result['link'] + ""
        await bot.say(formatText)
@bot.command()
async def jimmy():
    """In case I'm not here obviously"""
    random.seed()
    #await bot.say(foo)
@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
            rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return
    if(rolls > 50 or limit > 50):
        result = 'HEY NOW THAT\'S A LOTTA DICE!'
    else:
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)
    print (bot.get_channel())
    bot.send_message(bot.get_channel, 'boop')
@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))
@bot.command()
async def KrillMe():
    """Posts Krill"""
    await bot.say("http://coolaustralia.org/wp-content/uploads/2013/05/billandwill.jpg")
@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))
@bot.command()
async def Tides():
    """How quickly the tides turn"""
    await bot.say("http://i1.kym-cdn.com/photos/images/original/001/072/409/23c.gif")
@bot.command()
async def meme(message):
    await bot.send_message(message.channel, foo, tts=1)
    return 'boop'
@bot.command()
async def Delet():
    """Posts Delet this"""
    await bot.say("http://imgur.com/a/QrzQV")
#@asyncio.coroutine
#def on_message(message):
    #yield from self.process_commands(message)
   # if("jimmy" in message.content ):
        #foo=random.choice(["day seven. still have not finished the binding of isaac", "NEVER SHOULD HAVE COME HERE", "YOU'VE VIOLATED MY MOTHER!", "PICKED A BAD TIME TO GET LOST FRIEND", "You'll MAKE A FINE RUG, CAT", "Am I supposed to stand idly by WHILE A DRAGON BURNS MY HOLD AND SLAUGHTERS MY PEOPLE!?","porque no los dos","tough love is the only love","ukraine is game to you!?","https://i1.rgstatic.net/ii/profile.image/AS%3A272457688940593@1441970383991_l/Mike_Roggenkamp.png ","Don't mind me, just taking my hotdogs for a walk ( ͡° ͜ʖ ͡°)╯╲___ :hotdog:","( ͡° ͜ʖ ͡°)╯╲___卐卐卐卐","http://coolaustralia.org/wp-content/uploads/2013/05/billandwill.jpg","Remember the playlist!", "I blame Sean personally.", ".play seinfeld in the trap", "Don't forget I hate you all", "Don't forget you're here forever", "have you tried turning it on and off again", "that's the dumbest shit I've heard today.", "delete that fucking bird right now I swear to god", "nice microphone quality", "get a headset", "I might be a nazi mod but at least I'm not the one posting shit", "beep boop sean is a ro-bot", "arma 3 isn't a game it's a tactical simulator", "that's XCOM baby", "not my fault you're shit at games", "My anime is better than yours, by virtue of how awful it is"])
        #bot.send_message(message.channel, foo, tts=1)
    #print('bloop')
bot.run(os.getenv('DISCORD_TOKEN'))
