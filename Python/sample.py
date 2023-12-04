import discord

intents = discord.Intents.default()  # デフォルトのIntentsを設定
intents.messages = True  # メッセージイベントを受け取るために必要

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"ログインしました: {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("hello!"):
        await message.channel.send("こんにちは！")


# my token
token = "MTE3NjE0MzM0OTUwMjIwMTg3Nw.G-giQw.i5Pr3gc4t_rWs-Uzd0_Nu-CtRHW8PHkOFIK9DM"
client.run(token)
