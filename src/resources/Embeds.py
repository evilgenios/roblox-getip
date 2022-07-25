import discord


class Embeds:

    def __init__(self):
        Embeds.banner = "https://cdn.discordapp.com/attachments/886316612804808714/959307322520399923/68708434.png"
        Embeds.logo = "https://cdn.discordapp.com/attachments/886316612804808714/959307322520399923/68708434.png"

    def error(self, desc):

        embed = discord.Embed(
            title="__**Blackies.com Bot Error**__",
            description=f"```diff\n--- {desc}\n```",
            color=0xffffff
        )
    
        embed.set_image(url=self.banner)
        embed.set_footer(text="Blackies.com API", icon_url=self.logo)
        return embed

    
    def nodata(self, title):
        embed = discord.Embed(
            title="__**Blackies.com**__",
            description=f"```diff\n--- {title}\n- No data on that universe\n```",
            color=0xffffff
        )
        
        embed.set_image(url=self.banner)
        embed.set_footer(text="Blackies.com", icon_url=self.logo)
        return embed


    def post(self, title, desc):
        embed = discord.Embed(
            title="__**Blackies.com**__",
            description=f"```diff\n--- {title}\n{desc}\n```",
            color=0xffffff
        )
        
        embed.set_image(url=self.banner)
        embed.set_footer(text="Blackies.com API", icon_url=self.logo)
        return embed


    def fetching(self):
        embed = discord.Embed(
            title="__**Blackies.com**__",
            description="```diff\n--- Fetching server data\n```",
            color=0xffffff
        )
        
        embed.set_image(url=self.banner)
        embed.set_footer(text="Blackies.com API", icon_url=self.logo)
        return embed

