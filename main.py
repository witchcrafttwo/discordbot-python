import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_guild_member_add(member):
    channel = member.guild.get_channel(1153965115201290310)
    await channel.send(f'ようこそ {member.mention}')

    role = discord.utils.get(member.guild.roles, name='新規さん')
    if role:
        try:
            await member.add_roles(role)
            await channel.send(f'{member.mention} に新規さんロールを付与しました。自分で募集をするとロールが外されます')
        except Exception as error:
            print(f'ロール付与に失敗しました: {error}')

@bot.event
async def on_voice_state_update(member, before, after):
    target_voice_channel_id = 1144418046098804817
    target_role_id = 1259414360338727013

    if after.channel and after.channel.id == target_voice_channel_id and (before.channel is None or before.channel.id != target_voice_channel_id):
        target_role = member.guild.get_role(target_role_id)
        if target_role in member.roles:
            try:
                await member.remove_roles(target_role)
                print(f'{member} からロールを削除しました')
            except Exception as error:
                print(f'ロール削除に失敗しました: {error}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '!hasumint':
        await message.channel.send('はすはすだめぇ～')
    elif message.content == '!れおまる':
        await message.channel.send('レオ〇ワールド')
    elif message.content == '!YURABI':
        await message.channel.send('くたばりやがれ')
    elif message.content == 'お疲れ様':
        await message.channel.send('おつかれおまる～')
    elif message.content == 'IDplz':
        await message.channel.send('つー#1456')
    elif message.content == 'sika':
        await message.channel.send('しかのこのこのここしたんたん')
    elif message.content == '戦略':
        await message.channel.send('戦略が戦術に潰されてたまるものか！')
    elif message.content == 'I love':
        await message.channel.send('you~~~~~')
    elif message.content == '!help':
        await message.channel.send('利用可能なコマンド: !hasumint, !れおまる, !YURABI, お疲れ様, IDplz, sika, 戦略, I love')

bot.run("MTI1OTQxNjI3NTY2MzE5MjEwNQ.GiHR1v.Zn_XTA03Xou1K1IsguSopR9XNy8RMwZ6FpX2s4")
