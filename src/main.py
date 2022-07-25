import discord, json, os, sys, traceback
from discord.ext import commands
from datetime import datetime

# Load Config

with open('src/config.json', 'r') as f:
    config = json.load(f)
    
# Bot Setup

bot = commands.Bot(command_prefix=config['Discord']['Prefix'], case_sensitive=True, intents=discord.Intents.all())

# Load Cogs

for file in os.listdir("src/commands"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"commands.{name}")
        print(f"[LISTENING]: {str(name).upper()}")
        
# Bot Events

@bot.event
async def on_ready():
    print("[READY]: " + bot.user.name)

# Error Handler

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error):
    if hasattr(ctx.command, "on_error"):
        return
            
    cog = ctx.cog
    if cog:
        if cog._get_overridden_method(cog.cog_command_error) is not None:
            return
            
    ignored = (commands.CommandNotFound)
        
    error = getattr(error, 'original', error)
    if isinstance(error, ignored):
        return
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            timestamp=datetime.now()
        )
        embed.add_field(name="__ERROR:__", value=f"You have to wait `{error.retry_after}`s, lets not make kids mad ok :)", inline=False)
        await ctx.respond(embed=embed, delete_after=30.0)
    elif isinstance(error, commands.MissingAnyRole):
        embed = discord.Embed(
            colour=discord.Colour(0xffffff),
            timestamp=datetime.now()
        )
        embed.add_field(name="__ERROR:__", value=f"You don't have the required permissions to use this command", inline=False)
        await ctx.respond(embed=embed, delete_after=30.0)
    else:
        print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        print(f"An unexpected error occured in command `{ctx.command.qualified_name}`.")

# Bot Run

bot.run(config['Discord']['Token'])