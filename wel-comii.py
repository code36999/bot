import discord
from discord import message
from discord import user

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# wishing users for joining


@client.event
async def on_member_join(member):
    guild = client.get_guild(880398935741579345)
    channel = guild.get_channel(880398935741579348)
    await channel.send(f"""welcome to Cyber-D {member.mention} !:partying_face:""")
    await channel.send(f"{member.mention}check out some previous massage for up to date what's going on")


# private command
@client.event
async def on_message(message):
    guild = client.get_guild(880398935741579345)
    id = client.get_guild(880398935741579345)
    channel = guild.get_channel(880398935741579348)
    if message.content.find(">users") != -1:
        await message.channel.send(f"""number of Members {id.member_count}""")

    elif message.content == ">help bot":
        embed = discord.Embed(title="Help on Bot",
                              description="command list for 'wel-comi' bot")
        embed.add_field(name="command :>Hacking different Topic",
                        value="list different hacking tutorials ")
        embed.add_field(name="command :>hacking tutorials",
                        value="list  hacking tutorials on web,fb,windo,android and more ")
        embed.add_field(name="command :>hacking books",
                        value="list seven hacking books for Advance users one if your basic knowlage is done ")
        embed.add_field(name="command : >users",
                        value="list all users in this  ")
        embed.add_field(name="command :>Hacking tools",
                        value="list different hacking tools ")

        await message.channel.send(content=None, embed=embed)

    elif message.content == ">hacking books":
        embed = discord.Embed(title="- Hacking Books -",
                              description="hacking related books for advance users")
        embed.add_field(name="red-team-command-manual ::",
                        value="https://doc.lagout.org/rtfm-red-team-field-manual.pdf")
        embed.add_field(name="Hacker Playbook Practical ",
                        value="https://doc.lagout.org/security/The-Hacker-Playbook-Practical-Guide-To-Penetration-Testing-2014.pdf")
        embed.add_field(name="Malware Analyst's Cookbook.pdf",
                        value="https://repo.zenk-security.com/Virus-Infections-Detections-Preventions/Malware%20Analyst's%20Cookbook.pdf")
        embed.add_field(name="Advanced Hacking ",
                        value="http://index-of.es/.../Advanced%20Penetration%20Testing.pdf")
        embed.add_field(name="Basic security testing",
                        value="http://index-of.es/Varios/CreateSpace.Publishing.Basic.Security.Testing.With.Kali.Linux.Jan.2014.ISBN.1494861275.pdf")
        embed.add_field(name="Reverse Engineering",
                        value="https://www.foo.be/cours/dess-20122013/b/Eldad_Eilam-Reversing__Secrets_of_Reverse_Engineering-Wiley(2005).pdf")
        embed.add_field(name="Advanced Penetration Testing.",
                        value="http://index-of.es/Varios-2/Advanced%20Penetration%20Testing.pdf")
        embed.add_field(name="Guide-to-Computer-Forensics",
                        value="https://www.profajaypashankar.com/wp-content/uploads/2018/12/Guide-to-Computer-Forensics-and-Investigations-1.pdf")
        await message.channel.send(content=None, embed=embed)

    elif message.content == ">hacking tutorials":
        embed = discord.Embed(title="Hacking tutorials",
                              description="reade these tutorials or ask if stuck there")
        embed.add_field(name="Hack android using kali",
                        value="https://null-byte.wonderhowto.com/how-to/hack-android-using-kali-remotely-0160161/")
        embed.add_field(name="hack computer over wifi",
                        value="https://null-byte.wonderhowto.com/how-to/hack-computers-over-wi-fi-with-wifi-duck-payload-deliverer-0296285/")
        embed.add_field(name="hacking windos 10",
                        value="https://null-byte.wonderhowto.com/how-to/hacking-windows-10-break-into-somebodys-computer-without-password-setting-up-payload-0183584/")
        embed.add_field(name="Wifi hacking",
                        value="https://null-byte.wonderhowto.com/how-to/hack-wi-fi-get-anyones-wi-fi-password-without-cracking-using-wifiphisher-0165154/")
        embed.add_field(name="Hacking facebook",
                        value="https://www.hacking-tutorial.com/hacking-tutorial/tutorial-hacking-facebook-using-phishing-method-fake-facebook-website/?fbclid=IwAR3YtnwhTQM6edjEOopmsbiR7mi9FZ0vtI7Mqy17gj9LI8_fVISLfxZepaE")
        embed.add_field(name="hacking android 2",
                        value="https://www.hacking-tutorial.com/hacking-tutorial/hacking-android-smartphone-tutorial-using-metasploit/?fbclid=IwAR0kY-licAWoChwkf9aDltf5PZMBg5r0xLbBnOPAZv1hdjgK9j-_yH_BnS4")
        embed.add_field(name="Brute force website ",
                        value="https://null-byte.wonderhowto.com/how-to/brute-force-nearly-any-website-login-with-hatch-0192225/")
        embed.add_field(name="man in the middle attack",
                        value="https://www.hacking-tutorial.com/hacking-tutorial/kali-linux-man-middle-attack/?fbclid=IwAR3z9RvLg7UouN8XhG5PT4o3DP5FDo9vtE4vNjzAkPTf6ylI_BG0Yz0zqpo")
        await message.channel.send(content=None, embed=embed)
    # tutorials
    if message.content == ">Hacking different Topic":
        embed = discord.Embed(title="Basic hacking resourses",
                              description="all the tutorials and tools are for exersise perpous not to damage systems")
        embed.add_field(name="Install kali linux in virtual box",
                        value="https://www.hacking-tutorial.com/hacking-tutorial/how-to-install-kali-linux-on-virtualbox-part-1/?fbclid=IwAR1Iwc4rZg7zfxa0dwfoOtQi5DhvoE8ajhaaVzQ_41Vp4WA8w_DnAPmumAY")
        embed.add_field(name="Install kali from live USB drive",
                        value="https://null-byte.wonderhowto.com/how-to/install-kali-linux-as-portable-live-usb-for-pen-testing-hacking-any-computer-0384587/")
        embed.add_field(name="find information from phone",
                        value="https://null-byte.wonderhowto.com/how-to/find-identifying-information-from-phone-number-using-osint-tools-0195472/")
        embed.add_field(name="Dark web surch engine work on TOR browser",
                        value="dark web => http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion/search?query=")
        embed.add_field(name="learn skils brfore learning hacking",
                        value="https://null-byte.wonderhowto.com/how-to/essential-skills-becoming-master-hacker-0154509/")
        embed.add_field(name="clear log or tracks after hacking",
                        value="https://null-byte.wonderhowto.com/how-to/clear-logs-bash-history-hacked-linux-systems-cover-your-tracks-remain-undetected-0244768/")
        embed.add_field(name="advise to protect yourself",
                        value="https://null-byte.wonderhowto.com/how-to/advice-from-real-hacker-protect-yourself-from-being-hacked-0157218/")
        embed.add_field(name="get kali || kali linux in ANDROID",
                        value="https://www.kali.org/get-kali/?fbclid=IwAR2qDUfNOSWkDL7duK67tjemaATabBxFPDSHVl-VnmoFSUrkw3eGxxmRHXg#kali-mobile")
        await message.channel.send(content=None, embed=embed)

    if message.content == ">Hacking tools":
        embed = discord.Embed(title="Liat of hacking tools",
                              description="tools work on android termux or pc or some woek on specific system")
        embed.add_field(name="Style your termux or terminal",
                        value="https://awesomeopensource.com/project/adi1090x/termux-style ")
        embed.add_field(name="Bunch of many different hacking tools in one",
                        value="https://awesomeopensource.com/project/thehackingsage/hacktronian ")
        embed.add_field(name="Bombing tools",
                        value="https://awesomeopensource.com/project/LimerBoy/Impulse ")
        embed.add_field(name="Bombing sms/mail/call/whatshap tools",
                        value="https://awesomeopensource.com/project/bhattsameer/Bombers")
        embed.add_field(name=" @COUSTION if tou want to be protected from Bombing tools",
                        value="Ask it in group you will get your answer ,its little long explanation ")
        await message.channel.send(content=None, embed=embed)


client.run("ODgxMDcwNzk2MzQ3NDEyNTQw.YSnfHw.cgKfrA-OYMCVO5Uuprta0PNiCaM")
