import discord

from General import Constants


def main():

    client = discord.Client()

    @client.event
    async def on_message(message):

        if message.author != client.user:
            if "true" in message.content:
                await message.channel.send("THIS IS A FACT")
            elif "bruh" in message.content:
                await message.channel.send("Bruh indeed...")

            word_list = ["trump", "election"]
            split_message = message.content.split(" ")
            for word in word_list:
                if word in split_message:
                    await message.channel.send("I'm triggered")

    client.run(Constants.discord_credentials)


main()
