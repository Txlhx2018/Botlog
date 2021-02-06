import discord 
from discord.ext import commands 

client = commands.Bot(command_prefix ='YOUR PREFIX')

#Simple Botlog when the Bot joined a Guild or leave a Guild

@client.event
async def on_guild_join(guild):

        channel = client.get_channel(int(YOUR CHANNEL ID))
        embed=discord.Embed(title="**Bot Joined Guild**", color=0x00ff00)
        embed.add_field(name="Guild Name", value=f"{guild}", inline=False)
        embed.add_field(name="Owner", value=f"{guild.owner}", inline=False)     
        embed.add_field(name="Members", value=f"{guild.member_count}", inline=False)
        embed.add_field(name="Guild-ID", value=f"{guild.id}", inline=False)
        embed.add_field(name="Guild Created at", value=f"{guild.created_at.__format__('%A, %d. %B %Y | %H:%M:%S')}", inline=False)
        embed.set_thumbnail(url=guild.icon_url)
        await channel.send(embed=embed)
        
@client.event
async def on_guild_remove(guild):
        
        channel = client.get_channel(int(YOUR CHANNEL ID))
        embed=discord.Embed(title="**Bot Left Guild**", color=0xFF1800)
        embed.add_field(name="Guild Name", value=f"{guild}", inline=False)
        embed.add_field(name="Owner", value=f"{guild.owner}", inline=False)     
        embed.add_field(name="Members", value=f"{guild.member_count}", inline=False)
        embed.add_field(name="Guild-ID", value=f"{guild.id}", inline=False)
        embed.add_field(name="Guild Created at", value=f"{guild.created_at.__format__('%A, %d. %B %Y | %H:%M:%S')}", inline=False)
        embed.set_thumbnail(url=guild.icon_url)
        await channel.send(embed=embed)
       
client.run('YOUR BOT Token FROM DISCORD DEVELOPER PORTAL')
