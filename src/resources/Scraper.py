import json
import aiohttp

class Scraper:

    def __init__(self):
        with open("src/config.json", "r") as r:
            data = json.load(r)
            Scraper.cookies = {".ROBLOSECURITY": data["Roblox"]["Cookie"]}


    async def open_new_session(self, placeid):
        try:
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36', 
                'Referer': f"https://www.roblox.com/games/{placeid}/", 
                'Origin': 'https://www.roblox.com'
            }

            return aiohttp.ClientSession(headers=headers, cookies=Scraper.cookies)
        except Exception as e:
            print(__name__, e)


    
    async def __multiget(self, session, placeid):
        resp = await session.get(f'https://games.roblox.com/v1/games/multiget-place-details?placeids={placeid}')
        resp_json = await resp.json()

        return resp_json

    
    async def __gamev1(self, session, placeid):
        resp = await session.get(f'https://games.roblox.com/v1/games/{placeid}/servers/Public?sortOrder=Asc&limit=25')
        resp_json = await resp.json()

        return resp_json


    async def __assetgame(self, session, placeid, jobid):
        Data = json.dumps({
                "placeId": placeid,
                "isTeleport": False,
                "gameId": jobid,
                "gameJoinAttemptId": jobid
            })
        resp = await session.post(
            url=f"https://gamejoin.roblox.com/v1/join-game-instance",
            headers={
                "Referer": f"https://www.roblox.com/games/{placeid}/",
                "Origin": "https://roblox.com",
                "User-Agent": "Roblox/WinInet",
                "Content-Type": "application/json"
            },
            data=Data,
            cookies =Scraper.cookies
            )
        resp_json = await resp.json(content_type=None)
        return resp_json


    async def __join_script_url(self, session, url):
        resp = await session.get(url)
        print(resp)
        print(await resp.json())
        resp_text = await resp.text()
        print(resp_text)
        resp_json_string = resp_text.split('==%')[1]
        resp_json = json.loads(resp_json_string)

        return resp_json

    
    async def get_universe_from_place(self, session, placeid):
        resp = await session.get(f"https://api.roblox.com/universes/get-universe-containing-place?placeid={placeid}")
        resp_json = await resp.json()

        return resp_json

    
    async def get_ids_from_universe(self, session, universeid):
        resp = await session.get(f"https://develop.roblox.com/v1/universes/{universeid}/places?sortOrder=Asc&limit=25")
        resp_json = await resp.json()

        return resp_json


    async def fetch_place_details(self, session, placeid):
        try:
            resp = await self.__gamev1(session, placeid)
            if resp == None:
                return {
                    "error": "Application Error"
                }
                pass
            if not resp["data"]:
                return {
                    "jobids": [
                    ],
                    "playings": [
                    ],
                    "pings": [
                    ],
                    "maxPlayers": None,
                    "title": None
                }

            max_players = resp["data"][0]["maxPlayers"]

            jobids = []
            playings = []
            pings = []

            for _,v in enumerate(resp["data"]):
                playings.append(v["playing"])
                jobids.append(v["id"])
                try:
                    pings.append(v["ping"])
                except:
                    pings.append("0")

            resp = await self.__multiget(session, placeid)
            if resp == None:
                pass

            return {
                "jobids": jobids,
                "playings": playings,
                "pings": pings,
                "maxPlayers": max_players,
                "title": resp[0]["name"]
            }
        except:
            return {
                "error": "Application Error"
            }


    async def single_server(self, session, placeid, jobid):
        try:
            resp = await self.__assetgame(session, placeid, jobid)
            return {
                "host": resp["joinScript"]["ServerConnections"][0]["Address"],
                "port": resp["joinScript"]["ServerConnections"][0]["Port"]
                }
        except Exception as e:
            print(__name__, e)

    async def u_single_server(self, session, placeid, jobid):
        try:
            resp = await self.__assetgame(session, placeid, jobid)
            if resp['joinScript']:
                return {
                    "host": resp["joinScript"]["ServerConnections"][0]["Address"],
                    "port": resp["joinScript"]["ServerConnections"][0]["Port"]
                }
            else:
                return {
                    "error": "Application Error"
                }
            
        except Exception as e:
            print(__name__, e)
            return {
                "error": "Application Error"
            }