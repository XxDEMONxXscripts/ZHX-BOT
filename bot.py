import discord
import os

# Create a Discord client with default intents
intents = discord.Intents.default()
intents.message_content = True   # Enable reading message content if you need it

client = discord.Client(intents=intents)

# Event: when the bot is ready and online
@client.event
async def on_ready():
    print(f'✅ {client.user} is now online!')

# Event: when a message is sent in a server the bot can see
@client.event
async def on_message(message):
    # Don't reply to the bot's own messages
    if message.author == client.user:
        return

    # Simple ping command
    if message.content.lower() == '!ping':
        await message.channel.send('Pong! 🏓')

    # Process commands if you're using discord.ext.commands.Bot (optional)
    # await client.process_commands(message)   # Uncomment only if you switch to commands.Bot

# Run the bot using the token from environment variables
client.run(os.getenv('MTQ2NzA5MjkzMzY5MzAxODMzMw.Gy74vW.aoCYiFTjNo5YhguhXaB-LRCHyqNJ1bcplYwwUk'))
