import os
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from operations import calculate_damage
from mongo_db import all_weapons


load_dotenv(find_dotenv())
token = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} is online!')


@client.command()
async def roll(ctx, *args):
    try:
        n_dices = int(args[0])
        weapon = args[1].title() if args[2].isnumeric() else args[1].title() + ' ' + args[2].title()
        modifier = int(args[2]) if args[2].isnumeric() else int(args[3])
        advantage = args[3].lower() if args[3].isalpha() else args[4].lower()
        damage = calculate_damage(n_dices, weapon, modifier, advantage)
        await ctx.send(f'{damage}')
    except Exception as e:
        await ctx.send("Oops! Acho que alguns dados se perderam. Tente novamente. Em caso de dúvida, utilize o comando /help.")


@client.command()
async def ajuda(ctx, *args):
    try:
        embedVar = discord.Embed(title="Lucky Roller - Lista de comandos")
        embedVar.add_field(name="/roll", value="Rolagem: quantidade de dados + arma + modificador + vantagem, desvantagem ou normal\n"
                                               "Exemplo 1: 1 Espada Grande 2 desvantagem\n"
                                               "Exemplo 2: 3 Rapieira 3 normal", inline=False)
        embedVar.add_field(name="/armas",
                           value="Lista de armas disponíveis", inline=False)
        embedVar.add_field(name="/ajuda",
                           value="Lista de comandos", inline=False)
        await ctx.send(embed=embedVar)
    except Exception as e:
        print(e)


@client.command()
async def armas(ctx, *args):
    try:
        embedVar = discord.Embed(title="Lucky Roller",
                                 description="Lista de armas disponíveis")

        embedVar.add_field(name='', value='\n'.join(all_weapons()), inline=False)
        await ctx.send(embed=embedVar)
    except Exception as e:
        print(e)


def run():
    client.run(token)
