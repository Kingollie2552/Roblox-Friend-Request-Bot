import requests, json, asyncio, aiohttp, discord, datetime, urllib
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from datetime import date
from discord_components import Button,ButtonStyle, Select, SelectOption, ComponentsBot


req = requests.Session()

## Config
waittime = 60
token = "DISCORD BOT TOKEN"
channelid = CHANNELIDHERE 
cookie = "ROBLOX COOKIE HERE BRRR"
## end of 'config'


req.cookies['.ROBLOSECURITY'] = cookie




client = ComponentsBot("!")


async def requests1():
    await client.wait_until_ready()
    channel33 = client.get_channel(channelid)
    while True:
        
        r = req.get("https://api.roblox.com/incoming-items/counts")
        if not r.status_code == 200:
            print("Uh Oh Stinky SOmething went Wrong (InvalidCookie/Ratelimit)")
            break
        ##Check for invalid cookie / ratelimit


        incoming = r.json()["friendRequestsCount"]
        if incoming > 0:
            ## if incoming requests over 0 then...

            w = req.get("https://friends.roblox.com/v1/my/friends/requests?fetchMutualFriends=false&sortOrder=Desc&limit=100").json()
            for block in w["data"]:
                data = {}
                desc = block["description"]
                if desc == "":
                    desc = "No Description"
                ## Get Description If None set variable 

                followers = req.get(f"https://friends.roblox.com/v1/users/{block['id']}/followers/count").json()["count"]
                following = req.get(f"https://friends.roblox.com/v1/users/{block['id']}/followings/count").json()["count"]
                friends = req.get(f"https://friends.roblox.com/v1/users/{block['id']}/friends/count").json()["count"]
                ## get friends/following/followers
                
                
                infoblock = json.loads(json.dumps(block["friendRequest"]))

                datecreated = block["created"].split("T")[0].split("-")
                diff = datetime.date.today() - datetime.date(int(datecreated[0]), int(datecreated[1]), int(datecreated[2]))
                daysold = f"{diff.days} Days Old"

                datesent = infoblock["sentAt"].split("T")[0].split("-")
                diff1 = datetime.date.today() - datetime.date(int(datesent[0]), int(datesent[1]), int(datesent[2]))
                daysoldsent = f"{diff1.days} Days Ago"
                ## get shit to do with dates ^^

                avatarurl = "http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username={}".format(urllib.parse.quote(block['name']))
                embed = discord.Embed(title=f'**Friend Request Incoming!**', description=f'', color=0x33C5FF)
                embed.set_thumbnail(url=f'{avatarurl}')
                embed.add_field(name="Username:", value=block["name"], inline=True)
                embed.add_field(name="Display Name:", value=block["displayName"], inline=True)
                embed.add_field(name="UserID:", value=block["id"], inline=True)
                embed.add_field(name="Is Banned:", value=block["isBanned"], inline=True)
                embed.add_field(name="Account Created:", value=daysold, inline=True)
                embed.add_field(name="Sent:", value=daysoldsent, inline=True)
                embed.add_field(name="Following:", value=following, inline=True)
                embed.add_field(name="Followers:", value=followers, inline=True)
                embed.add_field(name="Friends:", value=friends, inline=True)
                embed.add_field(name="Description:", value=f"```{desc}```", inline=False)
                ## Build Sexy Embed

                            
                await channel33.send(embed=embed, components=[Button(style=ButtonStyle.URL, label="User Profile", url=f"https://web.roblox.com/users/{block['id']}/profile"),Button(style=ButtonStyle.URL, label="Accept Friend Request (POST)", url=f"https://friends.roblox.com/v1/users/{block['id']}/unfriend"),Button(style=ButtonStyle.URL, label="Deny Friend Request (POST)", url=f"https://friends.roblox.com/v1/users/{block['id']}/unfriend")])


                
                ## and finally send :)


        await asyncio.sleep(waittime)
        ## wait for ..time.. 







client.loop.create_task(requests1())
## make our loop
client.run(token)





