import discord
from discord.ext import commands
import discord.utils
import asyncio

TOKEN = ""

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=".help"))
    print("Ready")

@commands.has_role('Sudo')
@bot.command(name="give")
async def give(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)

@commands.has_role('Sudo')
@bot.command(name="remove")
async def remove(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)

@commands.has_role('Admin')
@bot.command(name="mute")
async def mute(ctx,member: discord.Member):
    myserver = bot.get_guild(733871808163348490)
    role = discord.utils.get(myserver.roles,name="Muted")
    if role not in member.roles:
        await member.add_roles(role)
        await ctx.send("Muted " + member.mention)

@commands.has_role('Admin')
@bot.command(name="unmute")
async def unmute(ctx,member: discord.Member):
    myserver = bot.get_guild(733871808163348490)
    role = discord.utils.get(myserver.roles,name="Muted")
    if role in member.roles:
        await  member.remove_roles(role)
        await ctx.send("Unmuted "+ member.mention)

@commands.has_role('Admin')
@bot.command(name="ban")
async def ban(ctx, user:discord.Member, args = None):
    await ctx.guild.ban(user)
    await ctx.send("Banned " + user.mention)
    days = 0
    hours = 0
    minutes = 0
    tmp = 0
    seconds = 0
    total_seconds = 0
    if args:
        args = args.lower()
        for arg in args:
            if arg == 'd':
                days += tmp
                tmp = 0

            elif arg == 'h':
                hours += tmp
                tmp = 0
                
            elif arg == 'm':
                minutes += tmp
                tmp = 0

            elif arg == 's':
                seconds += tmp
                tmp = 0

            elif arg.isdigit():
                tmp = tmp * 10
                tmp += int(arg)

        total_seconds = (days * 3600 * 24) + (hours * 3600) + (minutes * 60) + seconds
        await asyncio.sleep(total_seconds)
        await ctx.guild.unban(user)

@bot.command(name="unban")
async def unban(ctx, user: discord.User):
    await ctx.guild.unban(user)
    await ctx.send("Unbanned " + user.mention)

@commands.has_role('Admin')
@bot.command(name="close")
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    role = discord.utils.get(ctx.guild.roles,name="ForFun")
    overwrite = channel.overwrites_for(role)
    overwrite.send_messages = False
    await channel.set_permissions(role, overwrite=overwrite)
    await ctx.send('Channel locked.')

@commands.has_role('Admin')
@bot.command(name="open")
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    role = discord.utils.get(ctx.guild.roles,name="ForFun")
    overwrite = channel.overwrites_for(role)
    overwrite.send_messages = True
    await channel.set_permissions(role, overwrite=overwrite)
    await ctx.send('Channel unlocked.')

@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    myserver = bot.get_guild(733871808163348490)
    verify_channel = bot.get_channel(1001184563030143066)
    if payload.channel_id == verify_channel.id:
        role = discord.utils.get(myserver.roles,name="ForFun")
        await payload.member.add_roles(role)

@bot.command(name="color")
async def color(ctx,arg = None):
    myserver = bot.get_guild(733871808163348490)
    if ctx.channel.id == 1001191707334934628:
        if arg.isdigit():
            for x in range(16):
                role = discord.utils.get(myserver.roles,name=str(x))
                if role in ctx.author.roles:
                    await ctx.author.remove_roles(role)
            if 0 < int(arg) < 16:
                role = discord.utils.get(myserver.roles,name=arg)
                await ctx.author.add_roles(role)

bot.run(TOKEN)