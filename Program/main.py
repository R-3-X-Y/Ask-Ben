import discord, os, random, asyncio
from discord import app_commands
from datetime import datetime
class Bot(discord.Client):
	synced = False
	responses = ['Yes.', 'No.', 'Hohoho!', 'Ben?', 'Uhhh.']
	tree = None
	def __init__(self):
		super().__init__(intents = discord.Intents.default(), status = discord.Status.online, activity = discord.Activity(name="You", type=discord.ActivityType.watching))
		self.tree = app_commands.CommandTree(self)

	async def on_ready(self):
		await self.wait_until_ready()
		if not self.synced:
			await self.tree.sync(guild = None)
			self.loop.create_task(self.update_presence())
			self.synced = True
			
		print(f"[{datetime.now()}]\tLogged in as {self.user}")

	async def update_presence(self):
		while True:
			await self.change_presence(activity=discord.Activity(name=f"{len(self.guilds)} Servers", type=discord.ActivityType.watching))
			print(f"[{datetime.now()}]\tUpdated presence")
			await asyncio.sleep(60 * 10)
		
bot = Bot()

@bot.tree.command(name = "ask", description = "Ask Ben a question.", guild = None)
async def test_command(interaction: discord.Interaction, question: str):
	print(f"[{datetime.now()}]\t'{interaction.user}' asked: {question}")
	message = f"**{interaction.user.name}**: {question}\n**{bot.user.name}**: {bot.responses[random.randrange(0, len(bot.responses))]}"
	await interaction.response.send_message(message)


TOKEN = os.environ["DISCORD_TOKEN"]
bot.run(TOKEN)

