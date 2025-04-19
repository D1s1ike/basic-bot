from nextcord import Status, Activity, ActivityType, Guild
from nextcord.ext import commands

async def update_status(client):
    if client.guilds:
        guild: Guild = client.get_guild(client.cfg['guildId'])
    else:
        return
    try:
        await client.change_presence(status=Status.dnd, activity=Activity(type=ActivityType.watching,
                                     name=str(len(guild.members)) + ' Members'))
    except:
        pass


class BotStatus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener(name='on_guild_join')
    @commands.Cog.listener(name='on_guild_remove')
    @commands.Cog.listener(name='on_ready')
    @commands.Cog.listener(name='on_member_join')
    @commands.Cog.listener(name='on_member_remove')
    async def update_status(self, *args):
        await update_status(self.client)


def setup(client):
    client.add_cog(BotStatus(client))
