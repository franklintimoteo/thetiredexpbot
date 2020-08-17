import discord
from discord.ext import commands

from scrappertaleon import get_experience_members_today

#Altera o prefix de comando para !th (!thetired)
bot = commands.Bot(command_prefix="$")

@bot.command()
async def rank(ctx):
    """Envia o rank atual de exp do dia com todos membros da guild"""
    #TODO: verificar membros inativos e não mostrar no rank
    #TODO: aceitar argumento com quantidade de membros retornados
    experience_members_today = get_experience_members_today()
    await ctx.send(experience_members_today)

print("running...")
bot.run('NzQ0OTEzNzIyNzkwOTAzODc4.XzqI9w.PHW8cq8puzvd2FbePoccj_zmvB8')
print("Exit...")