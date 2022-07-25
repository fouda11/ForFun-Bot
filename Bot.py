import discord
from discord.ext import commands
import discord.utils

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready")

@bot.command(name="give",aliases=["ادي"])
async def give(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)

@bot.command(name="remove",aliases=["شيل"])
async def remove(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)

@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    verify_channel = bot.get_channel(1001184563030143066)
    if payload.channel_id == verify_channel.id:
        myguild = bot.get_guild(payload.guild_id)
        role = discord.utils.get(myguild.roles,name="ForFun")
        await payload.member.add_roles(role)



bot.run(TOKEN)
