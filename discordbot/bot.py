from discord import Status, Member, User, TextChannel, VoiceChannel, Role, Invite, Game, Emoji, PartialEmoji, Colour
from discord.ext import commands
from rich.traceback import install as install_traceback

from discordbot.config import DEBUG

from .models import ReactionMapping
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async


install_traceback()
from rich.pretty import install as install_pretty

install_pretty()

#

CONVERTERS = {
    Member: commands.MemberConverter,
    User: commands.UserConverter,
    TextChannel: commands.TextChannelConverter,
    VoiceChannel: commands.VoiceChannelConverter,
    Role: commands.RoleConverter,
    Invite: commands.InviteConverter,
    Game: commands.GameConverter,
    Emoji: commands.EmojiConverter,
    PartialEmoji: commands.PartialEmojiConverter,
    Colour: commands.ColourConverter
}


class Reactor(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(self.get_command_prefix, **kwargs)

    def get_command_prefix(self, client, message):
        return ""

    async def on_ready(self):
        print(f'{bot.user} has connected to Discord!')

        for guild in self.guilds:
            print(
                f'{bot.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
            )
    async def on_message(self, message):
        if message.author == self.user:
            return

        @database_sync_to_async
        def get_object_synched():
            return list(ReactionMapping.objects.filter(user=message.author.name))

        obs = await get_object_synched()
        emojis = self.emojis
        print(emojis)

        def get_emoji(name):
            for em in emojis:
                if em.name == name:
                    return em
            return name

        if obs is not None:
            for reaction in obs:
                try:
                    reactionEmoji = get_emoji(reaction.reaction)
                    await message.add_reaction(reactionEmoji)
                except:
                    print(reaction)
                    pass


        if message.author.name == "MEE6":
            await message.add_reaction("😡")

# create Bot

bot = Reactor(
    description='Reactor hates MEE6',
    case_insensitive=True,
    status=Status.idle,
    help_command=None,
)


# Start

def run(TOKEN):
    print("[Bot] - Starting with DEBUG=" + str(DEBUG))
    bot.run(TOKEN, bot=True, reconnect=True)


if __name__ == "__main__":
    print("[Bot] - You must run this bot via your manage.py file: python3.8 manage.py run-discorbot")
