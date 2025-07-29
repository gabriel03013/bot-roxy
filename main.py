import discord
from discord.ext import commands
from random import randint as rd
from discord import SelectOption
import psycopg2
from psycopg2 import sql

adm = 614548307187990651

try:
    conexao = psycopg2.connect(database = "discord", host = 'pg-198bee84-discord-gb.d.aivencloud.com', user = 'avnadmin', password = 'AVNS_BPnCotxyGQ_PZW7nyV8', port = '14647')
    bd = conexao.cursor()
    bd.execute("SELECT current_database();") 

    print("Banco conectado:", bd.fetchone()[0])

except Exception as e:
    print("Erro ao conectar:", e)

permissoes = discord.Intents.all()
bot = commands.Bot(command_prefix='r!', intents=permissoes)
permissoes.bans = True  
permissoes.members = True

@bot.command()
async def roxy(ctx):
    await ctx.reply("oi eu sou a Roxy")

@bot.command()
async def oracao(ctx):
    arquivo = discord.File("assets/images/rudeusCalcinha.jpeg", filename="rudeusCalcinha.jpeg")
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
    Assim seja.""", file=arquivo)

@bot.command()
async def edit(ctx):
    with open("assets/videos/editRoxy.mp4", "rb") as f:
        await ctx.reply("EDIT DA DEUSA ROXY:", file=discord.File(f, "editRoxy.mp4"))

bot.run("MTM5OTc2MzAwNDQwMDM0MTAxNA.GNqiR2.cMsXePMopBD-aQM6CtSZJ-PUw2Pv7q3eYs_3Go")
