import os, requests, time, json, random, discord, threading
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token, guild = config['Bot']['token'], config['Bot']['guild']
intents, intents.members = discord.Intents.all(), True
client = commands.Bot(command_prefix='q', case_insensitive=False, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    await ban().scrape()

class ban():
    def __init__(self):
        self.token = token
        self.guild = guild

    async def scrape(self):
        await client.wait_until_ready()
        ob = client.get_guild(int(self.guild))
        members = await ob.chunk()
        os.remove('Core/botscrape.txt')

        with open('Core/botscrape.txt', 'a') as txt:
            for member in members:
                txt.write(str(member.id) + '\n')
            txt.close()
            await ban().thread()
    
    async def thread(self):
        print('\n [>] Banning...\n')
        txt = open('Core/botscrape.txt')
        for member in txt:
            threading.Thread(target=ban.mass, args=(self.guild, member,)).start()
        txt.close() # return

    def mass(self, member):
        try:
            requests.put(f'https://discord.com/api/v{random.choice([6, 7, 8, 9])}/guilds/{guild}/bans/{member}', headers={'Authorization': f'Bot {token}'}), time.sleep(0.1)
        except:
            pass

if __name__ == '__main__':
    try:
        os.system('cls')
        client.run(token)
    except ImportError:
        os.system('python -m pip install discord')
        client.run(token)
    except:
        input('\n [!] Invalid Token\n')