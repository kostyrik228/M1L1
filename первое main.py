
from tkinter import * 

from tkinter.ttk import *

from time import strftime



import googletrans
import calendar
from googletrans import Translator
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def smile(ctx):
    vabor = random.randint(1,5)
    if vabor == 1:
        await ctx.send("&#128512;")
    
    if vabor == 2:
        await ctx.send("&#128516;")
    
    if vabor == 3:
        await ctx.send("&#128513;")
    
    if vabor == 4:
        await ctx.send("&#128519;")
    
    if vabor == 5:
        await ctx.send("&#128535;")


@bot.command()
async def monetka(ctx):
    flip = random.randint(1, 2)
    if flip == 1:
        await ctx.send("ОРЕЛ")
    if flip == 2:
        await ctx.send("РЕШКА")
        


@bot.command()
async def password(ctx, pass_length: int):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    await ctx.send(password)
    

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')


@bot.command()
async def by(ctx):
    await ctx.send(f"Пока! {ctx.author}")



@bot.command()
async def add(ctx, left: int, right: int):
    #"""складывает два числа."""
    await ctx.send(left + right)



@bot.command()
async def info(ctx):
    await ctx.send("Это первый бот автора (Константина)")
    await ctx.send("Бот был создан 17 сентября 2023г")
    await ctx.send("Версия бота 1.1")
    await ctx.send("бот каждый день будет улучшать и когда нибудь придёт к тому что будет уметь всё))")



@bot.command()
async def roll(ctx, dice: str):
    #"""Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)






@bot.command()
async def helps(ctx):
    await ctx.send("smile - (Выводит рандомный смайлик)")
    await ctx.send("monetka - (Подбрасывает монетку)")
    await ctx.send("password - (Генерирует рандомный пороль)")
    await ctx.send("hello - (Бот поздаровается с вами)")
    await ctx.send("by - (Бот попрощается с вами)")
    await ctx.send("info - (Выводим всю информацию о бота)")
    await ctx.send("roll - (Вы задаёте параметр NdN и под бобрасывает кубик(кубики)) ")
    await ctx.send("number - (Выведитт календарь сейчасшний год и месяц)")
    await ctx.send("quote = (Расскажет вам цитату)")







@bot.command()
async def translate(ctx, lang, *, args):
    t = Translator()
    a = t.translate(args, dest=lang)
    await ctx.send(a.text)  



@bot.command()
async def number(ctx):
    year = 2023
    month = 9 
    await ctx.send(calendar.month(year,month))



@bot.command()
async def time(ctx):
    root = Tk()
    root.title("clock")

    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

    label = Label(root, font=("ds-digital",80),background="black",foreground="cyan")
    label.pack(anchor="center")
    await ctx.send("time()")
    await ctx.send("mainloop()")




@bot.command()
async def quote(ctx):
    vab = random.randint(1,5)
    if vab == 1:
        await ctx.send("Живи как хочешь, раз нельзя как хочется...")


    if vab == 2:
        await ctx.send("Никогда не откладвай на завтра, то что можешь сделать послезавтра")

    
    if vab == 3:
        await ctx.send("Каждый человек имеет право на собственное мнение — при условии, что оно совпадает с нашим")


    if vab == 4:
        await ctx.send("Добрым словом и револьвером вы сможете добиться большего, чем одним лишь добрым словом")


    if vab == 5:
        await ctx.send("Сходят с ума только те, у кого он есть")
