
import discord

client = discord.Client()

@client.event  

async def on_ready():
    print(f" We have logged in as {client.user}")

@client.event
async def on_message(message):
	print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

	if "selamun aleyküm"  in message.content.lower():
		await message.channel.send("aleyküm selam ")


		if "nasılsın" in message.content.lower():
			 await message.channel.send("iyiyim sen nasılsın")
	
	#elif "iyiyim" in message.content.lower():
		#await message.channel.send("allah daha iyi etsin")
client.run("It must be your token")