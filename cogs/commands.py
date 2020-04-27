import discord
from discord.ext import commands, tasks

class Commands(commands.Cog):
       
    def __init__(self, bot):
        self.bot = bot

    #Events    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"-----\n |Logged in as: {self.bot.user.name} : {self.bot.user.id} \n |My current prefix is: .\n-----")

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)} ms')

    @commands.command(name='hi', aliases=['hello'])
    async def _hi(self, ctx):
        await ctx.send(f'Hi {ctx.author.mention}')

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *,reason=None):
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
        
    @commands.command()
    async def unban(self, ctx, *,member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return


def setup(bot):
    bot.add_cog(Commands(bot))