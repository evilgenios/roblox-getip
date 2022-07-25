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


    def attack(self, host, port, time, cooldown, authorid):
        embed = discord.Embed(
            title = "__**Blackies.com OVH Attack Sent**__",
            description = f"__**HOST** __\n{host}\n\n__**PORT** __\n{port}\n\n__**TIME** __\n{time}\n\n__**COOLDOWN** __\n{cooldown}\n\n__**SENDER**__\n<@{authorid}>",
            color = 0xffffff
        )
        embed.set_image(url=self.banner)
        embed.set_thumbnail(url=self.logo)
        embed.set_footer(text="Blackies.com API", icon_url=self.logo)

        return embed


    def database(self, desc):
        embed = discord.Embed(
            title="__**Blackies.com**__",
            description=f"```diff\n--- {desc}\n```",
            color=0xffffff
        )
        
        embed.set_image(url=self.banner)
        embed.set_footer(text="Blackies.com", icon_url=self.logo)
        return embed

    
    def plan(self, array):
        embed = discord.Embed(  
            title="__**Blackies.com**__",
            color=0xffffff
        )
        embed.add_field(
            name="Attack Cons",
            value=array["concurrents"],
            inline=False
        )
        embed.add_field(
            name="Attack Cooldown",
            value=array["cooldown"],
            inline=False
        )
        embed.add_field(
            name="Allowed Attack Time",
            value=array["time"],
            inline=False
        )
        embed.add_field(
            name="Vip Status",
            value=array["vip"],
            inline=False
        )
        embed.add_field(
            name="Plan",
            value=array['plan'],
            inline=False
        )
        embed.add_field(
            name="Expiration",
            value=array['datetime'],
            inline=False
        )
        # embed.set_thumbnail(url=self.logo)
        # embed.set_image(url=self.banner)
        embed.set_footer(text="Blackies.com")
        return embed
    
    def FivemIP(self, array):
        embed = discord.Embed(  
            title="__**Blackies.com**__",
            color=0xffffff
        )
        embed.add_field(
            name="**__Server Details__**",
            value=f"__IP/PORT:__ `{array['ip']}:{array['port']}`\n__Country:__ `{array['country']}`\n__ISP:__ `{array['isp']}`\n__Org:__ `{array['org']}`\n__Zip Code:__ `{array['zip']}`\n__Timezone:__ `{array['timezone']}`",
            inline=False
        )
        embed.add_field(
            name="**FiveM Server**", 
            value=f"__Server Name:__ `{array['hostname']}`\n\n__Max Players:__ `{array['players']}/{array['svMaxclients']}`\n__Artifacts:__ `{array['server']}`\n__OneSync Enabled:__ `{array['vars']}`",
            inline=False
        )
        embed.set_footer(text="Blackies.com")
        return embed
