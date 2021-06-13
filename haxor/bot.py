import discord
from discord import activity
from discord.ext import commands
import pyjokes
import pyttsx3
import datetime
from datetime import date
import requests
import random
import google_search_py
from pistonapi import PistonAPI


piston = PistonAPI()
c0mmands = """
**main:**
```
prefix = # or haxor
thanks = Display thanks message.
Hello = Display hello message.
date = Display date.
time = Display time.
joke = Display random joke.
date = Display date.
ping = Display latency.
yt + keyword = Display youtube search.
google + keyword = Display Google search.
say + word = Repeat message.
8ball + question = Display Yes No etc.
spam + @username = Ping 10 times.
whoru = Display bot name.
run py + code here = Run python code.
run js + code here = Run javascript code.
```
**Moderation:**
```
clear = Clear channel.
ban = Ban member.
kick = Kick member.
```
"""
client = commands.Bot(command_prefix = ["#", "haxor"])
client.remove_command("help")
e = datetime.datetime.now()

class bot():

    @client.command()
    async def yt(ctx, *, message):
        url = "https://pywhatkit.herokuapp.com/playonyt?topic=" + message
        GET_content = requests.get(url)
        Play_Content = str(GET_content.text)
        await ctx.send(embed=discord.Embed (color=0x9b59b6, title="Searched:" + " " + message))
        await ctx.send(Play_Content)

    
    @client.command()
    async def google(ctx, *, message):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, title="Googled:" + " " + message))
        await ctx.send(google_search_py.search(message, False)['result'])

    @client.command()
    async def run(ctx,n,*,code):
        nm = n.lower()
        a = code.replace("```", "")

        if nm == "py":
            b = (piston.execute(language="py", version="3.9", code=a))
            c = str(b)
            em = discord.Embed(title="Code Output",
            description=f"```py\nOutput:\n{c}```",
            color=0x9b59b6)

        elif nm == "js":
            b = (piston.execute(language="js", version="15.10.0", code=a))
            c = str(b)
            em = discord.Embed(title="Code Output",
            description=f"```py\nOutput:\n{c}```",
            color=0x9b59b6)

        else:
            await ctx.send(embed=discord.Embed (color=0x9b59b6, title="Error", description="**Not a supported language !**"))
        
        await ctx.send(embed=em)

    @client.command(aliases=["thx", "Thanks", "tk"])
    async def thanks(ctx):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, description="**Your'e welcome ! 😁**"))

    @client.command(aliases=["will_i", "8ball"])
    async def eightball(ctx):
        choices = ["Yes", "No", "Probably", "Probably Not", "I dont know"]
        result = random.choice(choices)
        await ctx.send(embed=discord.Embed (color=0x9b59b6, title="8ball", description=result))


    @client.command(aliases=["spam"])
    async def troll(ctx, message):
        for i in range (10):
            await ctx.send(message)

    @client.command()
    async def whoru(ctx):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, title="Profile", description=client.user))

    @client.command()
    async def say(ctx, message):
        message.replace(" ", "_")
        await ctx.send(embed=discord.Embed (color=0x9b59b6, title="I said", description=message))

    @client.command(aliases=["h", "Help", "hlp", "ineedhelp"])
    async def help(ctx):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, title="Haxor discord bot - Help", description=c0mmands))

    @client.event
    async def on_ready():
        print("bot is online")
        await client.change_presence(activity=discord.Game(name="#help"))

    @client.command()
    @commands.has_any_role("Moderator", "Administrator", "Admin", "Mod", "Founder", "owner")
    async def clear(ctx):
        await ctx.channel.purge()


    @client.command(aliases=["hello", "hell0", "hi"])
    async def Hello(ctx):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, description="**Hello There 😊**"))

    @client.command()
    @commands.has_role("Moderator")
    async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @client.command()
    @commands.has_role("Moderator")
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @client.command()
    async def ping(ctx):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, description=(f"**Pong!** latency : {round(client.latency * 1000)}MS")))

    @client.command(aliases=["Joke"])
    async def joke(ctx):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, title="😂 HAHA", description="**" + (pyjokes.get_joke(language='en', category= 'neutral')) + "**"))

    @client.command(aliases=["what's the time", "whats the time"])
    async def time(ctx):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, description="**The time is %s:%s**" % (e.hour, e.minute)))

    @client.command(aliases=["what's the date", "whats the date", "date"])
    async def todaysdate(ctx):
        await ctx.send(embed=discord.Embed (color=0x9b59b6, description=(date.today())))


    client.run("ODQzMTA1NzA5MTI2MDU4MDQ1.YJ_BYQ.KRL-SUtw8iRKRHF2fQgt7OwUjOo")