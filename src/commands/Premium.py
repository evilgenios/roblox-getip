from discord.ext import commands
from resources.Embeds import Embeds
from resources.Scraper import Scraper

class Premium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role('Client', "Admin")
    async def ip(self, ctx, link):
        try:
            e_client = Embeds()
            
            embed = e_client.fetching()
            msg = await ctx.send(embed=embed)

            if not "https://www.roblox.com/games/" in link:
                embed = e_client.error("Link does not lead to a roblox game")
                return await msg.edit(embed=embed)

            client = Scraper()
            placeid = link.split("/")[4]
            session = await client.open_new_session(placeid)

            p = await client.fetch_place_details(session, placeid)
            info_string = ""

            if "jobids" not in p:
                embed = e_client.error("No servers are alive at that place")
                await session.close()
                return await msg.edit(embed=embed)

            for i,v in enumerate(p["jobids"]):
                s = await client.single_server(session, placeid, v)
                f = i+1

                if s != None:
                    info_string += "! Server {} ({}/{}) | {}:{} | {}ms\n".format(
                        f,
                        p["playings"][i], 
                        p["maxPlayers"], 
                        s["host"], 
                        s["port"], 
                        p["pings"][i]
                    )
                elif s == None:
                    info_string += "- Failed to fetch server details.\n"

                embed = e_client.post(p["title"], info_string)
                await msg.edit(embed=embed)

            await session.close()
        except Exception as e:
            print(__name__, e)
            if "session" in locals():
                await session.close()

            embed = e_client.error("Application Error")
            return await msg.edit(embed=embed)

    @commands.command()
    @commands.has_any_role('Client', "Admin")
    async def universe(self, ctx, link):    
        try:
            e_client = Embeds()
            
            embed = e_client.fetching()
            msg = await ctx.send(embed=embed)

            if not "https://www.roblox.com/games/" in link:
                embed = e_client.error("Link does not lead to a roblox game")
                return await msg.edit(embed=embed)

            client = Scraper()
            placeid = link.split("/")[4]
            session = await client.open_new_session(placeid)

            u = await client.get_universe_from_place(session, placeid)
            j = await client.get_ids_from_universe(session, u["UniverseId"])
            fetching = None

            for i,v in enumerate(j["data"]):
                _placeid = v["id"]
                p = await client.fetch_place_details(session, _placeid)
                if i > 0:
                    if "Fetching" in embed.description or fetching == True:
                        embed = e_client.nodata(p["title"])
                        await msg.edit()
                    embed = e_client.fetching()
                    msg = await ctx.send(embed=embed);fetching=True

                info_string = ""

                if "jobids" not in p:
                    embed = e_client.error("No servers are alive at this universe")
                    await msg.edit(embed=embed)
                    continue
    
                for i,v in enumerate(p["jobids"]):
                    s = await client.u_single_server(session, _placeid, v)
                    f = i+1

                    if s != None:
                        info_string += "! Server {} ({}/{}) | {}:{} | {}ms\n".format(
                            f,
                            p["playings"][i], 
                            p["maxPlayers"], 
                            s["host"], 
                            s["port"], 
                            p["pings"][i]
                        )
                    elif s == None:
                        info_string += "- Failed to fetch server details.\n"

                    embed = e_client.post(p["title"], info_string)
                    await msg.edit(embed=embed)

                    if fetching == True:
                        fetching = False

            await session.close()
        except Exception as e:
            print(e)
            if "session" in locals():
                await session.close()

            embed = e_client.error("Application Error")
            return await msg.edit(embed=embed)
    
    

def setup(bot):
    bot.add_cog(Premium(bot))