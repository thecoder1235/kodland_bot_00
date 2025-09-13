import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command(name="zar")
async def zar(ctx):
    result = random.randint(1, 6)
    await ctx.send(f"🎲 {ctx.author.mention}, zarın: {result}")

@bot.command(name="yazi_tura")
async def yazi_tura(ctx):
    result = random.choice(["Yazı 🪙", "Tura 🪙"])
    await ctx.send(f"{ctx.author.mention}, sonuç: {result}")

@bot.command(name="sayi")
async def sayi(ctx, min: int = 1, max: int = 100):
    result = random.randint(min, max)
    await ctx.send(f"{ctx.author.mention}, rastgele sayı: {result}")


bot.run("")
