import discord, os, random
from webserver import keep_alive
intents = discord.Intents.default()
bot = discord.Client(intents = intents, status = discord.Status.online, activity = discord.Activity(name="You", type=discord.ActivityType.watching))
responses = ['Yes.', 'No.', 'Hohoho!', 'Ben?', 'Uhhh.']
@bot.event
async def on_ready():
	print("Bot Active")
@bot.event
async def on_message(message):
	message.content = message.content.lower()
	if bot.user.mentioned_in(message):
		await message.channel.send("Yes. (send 'ben' followed by your question, ex 'ben are you a bot?')")
	elif message.content.startswith('ben '):
		await message.channel.send(responses[random.randrange(0, len(responses))])
TOKEN = os.environ["TOKEN"]
keep_alive()
bot.run(TOKEN)
