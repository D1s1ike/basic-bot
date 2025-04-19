import nextcord
from nextcord.ext import commands

# MADE BY dis1ik3

class VerifyButton(nextcord.ui.View):
    def __init__(self, role: nextcord.Role, client: commands.Bot):
        self.role = role
        super().__init__(timeout=None)

        async def callback(interaction: nextcord.Interaction):
            await interaction.response.send_message('✅ | Successfully verified!', ephemeral=True)
            if self.role:
                await interaction.user.add_roles(self.role)

        emoji = nextcord.utils.get(client.emojis, name='verify')

        self.button = nextcord.ui.Button(label='Verify', emoji=emoji, style=client.cfg.get('buttonStyle', nextcord.ButtonStyle.green),
                                         custom_id='v_button')
        self.add_item(self.button)
        self.button.callback = callback


class Verify(commands.Cog):
    def __init__(self, client):
        self.role = None
        self.client = client

    @nextcord.slash_command(name='setup-verify', description='Setup channel for verify system')
    async def set_verify(self, interaction: nextcord.Interaction, channel: nextcord.TextChannel = None):
        if channel is None:
            channel = interaction.channel
        if interaction.user.guild_permissions.administrator:
            embed = nextcord.Embed(title=f'Welcome to {interaction.guild.name}\'s Verify.',
                                   description='Click the button below to get verified.',
                                   color=interaction.guild.self_role.colour)
            embed.set_thumbnail(url=self.client.user.avatar)
            embed.set_footer(text=f'Verify | Developed by dis1ik3', icon_url=self.client.user.avatar)
            await interaction.channel.send(embed=embed, view=VerifyButton(self.role, client=self.client))
            await interaction.response.send_message(f'Success.', ephemeral=True)
        else:
            await interaction.response.send_message('You are not allowed to use this command')

    @commands.Cog.listener()
    async def on_ready(self):
        guild = self.client.get_guild(int(self.client.cfg['guildId']))
        self.role = nextcord.utils.get(guild.roles, id=int(self.client.cfg['verifyRole']))
        self.client.add_view(VerifyButton(self.role, client=self.client))


def setup(client):
    client.add_cog(Verify(client))
