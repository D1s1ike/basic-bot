from nextcord.ext import commands
from nextcord import Member, slash_command, Interaction, Embed, TextChannel, ui, ButtonStyle, utils
from datetime import datetime
from json import load, dump
from os import path, mkdir


class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel = None
        self.members = []

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        if not path.exists('./data/welcome/config.json'):
            return
        if member.id in self.members:
            return
        else:
            self.members.append(member.id)
        if not self.channel:
            return
        text = f'{member.mention} Welcome to the server!\nPlease read our server rules in <#{self.client.cfg["rulesChannel"]}>'
        embed = Embed(title=f'Welcome {member.name} to {member.guild.name}!', description=text,
                      colour=member.guild.self_role.colour)
        embed.timestamp = datetime.now()
        g_icon = member.guild.icon.url if member.guild.icon else None
        u_icon = member.display_avatar.url if member.display_avatar else None
        embed.set_footer(icon_url=g_icon, text=f'Welcome | Developed by dis1ik3 \u200b')
        if member.display_avatar:
            embed.set_thumbnail(url=u_icon)
        view = ui.View(timeout=None)
        view.add_item(ui.Button(label=f'You are the {member.guild.member_count}th Member!',
                                style=self.client.cfg.get('buttonStyle', ButtonStyle.green), disabled=True))
        try:
            await self.channel.send(embed=embed, view=view)
        except Exception as e:
            print(f'Failed to send welcome message for user {member.name}: {e}')

    @slash_command(name='setup-welcome', description='Set welcome channel')
    async def set_welcome(self, interaction: Interaction, channel: TextChannel = None):
        if not interaction.user.guild_permissions.administrator:
            return await interaction.response.send_message(f'❌ | You don\'t have permission to use this command.',
                                                           ephemeral=True)
        if not channel:
            channel = interaction.channel
        with open('./data/welcome/config.json', 'w') as f:
            a = {
                'channel': channel.id
            }
            dump(a, f, indent=4)
        await interaction.response.send_message(f'Welcome channel set to {channel.mention}', ephemeral=True)

    @commands.Cog.listener()
    async def on_ready(self):
        if not path.exists('./data/welcome'):
            mkdir('./data/welcome')
        if not path.exists('./data/welcome/config.json'):
            self.channel = None
        else:
            with open('./data/welcome/config.json', 'r') as f:
                config = load(f)
                self.channel = utils.get(self.client.get_all_channels(), id=config['channel'])


def setup(client):
    client.add_cog(Welcome(client))
