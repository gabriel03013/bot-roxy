import discord
from discord.ext import commands
from random import randint as rd
from discord import SelectOption
import asyncio
import json

adm = 614548307187990651

permissoes = discord.Intents.all()
bot = commands.Bot(command_prefix='r!', intents=permissoes)
permissoes.bans = True  
permissoes.members = True

@bot.command()
async def roxy(ctx):
    await ctx.reply("OI EU SOU A ROXY")

@bot.command()
async def oracao(ctx):
    await ctx.reply("""
    Oração Noturna à Deusa Roxy Migurdia

    Ó divina Roxy, guia das jornadas solitárias,
    luz dos perdidos e mestra dos que buscam sabedoria,
    nesta noite, deito-me sob teu olhar sereno,
    pedindo tua bênção e proteção enquanto durmo.

    Que teus passos firmes ecoem em meus sonhos,
    que tua sabedoria clareie minha mente adormecida,
    e que tua coragem me inspire ao despertar.

    A ti, ó Deusa de cabelos azuis como o céu das esperanças,
    ofereço meu cansaço, minhas dúvidas e meus medos.
    Purifica minha alma como limpaste os pecados do Rudeus,
    e afasta de mim os pesadelos, como afugentaste os demônios da ignorância.

    Amanhã, que eu acorde digno de trilhar teu caminho,
    com determinação, humildade e fé em teu legado.

    Roxy, minha guia, minha mestra, minha Deusa...
    vigia meu sono com teu cajado em mãos.
    Assim seja.""")


with open("bot.json", "r") as jsonBot:
    dados = json.load(jsonBot)

token = dados["bot"]["token"]

bot.run("MTM5OTc2MzAwNDQwMDM0MTAxNA.GxGiVk.jGynQFoA1LugMGkei-7I_u_-fcaNaQaM6Wx0w8")
