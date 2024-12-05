import discord
from discord.ext import commands
from discord.permissions import Permissions

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot ready")


@bot.command()
async def hello(ctx):
    await ctx.send(f"hello there , {ctx.author.mention}")


@bot.command(aliases=["good", "morning"])
async def gm(ctx):
    await ctx.send(f"Good morning, {ctx.author.mention}")


@bot.command()
async def embed(ctx):
    embed_msg = discord.Embed(title="Some Title", description="Some Description also")
    embed_msg.set_thumbnail(url=ctx.author.avatar)
    embed_msg.add_field(name="some Name", value="Some value for field", inline=True)
    embed_msg.set_image(url=ctx.guild.icon)
    embed_msg.set_footer(text="Some Text", icon_url=ctx.author.avatar)
    await ctx.send(embed=embed_msg)


@bot.command()
async def ping(ctx):
    users = bot.users
    for user in users:
        user_id = user.id
        user_name = user.name
        is_bot = user.bot
        # Format the output with clear labels and spacing
        print(f"ID: {user_id:<15} Name: {user_name} Is Bot: {is_bot}")

    ping_embed = discord.Embed(
        title="Ping", description="Check bot Latency ", color=discord.Color.purple()
    )
    ping_embed.add_field(
        name=f"{bot.user.name}'s Latency (ms): ",
        value=f"{round(bot.latency * 1000 )}ms ",
        inline=True,
    )
    ping_embed.set_footer(
        text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar
    )
    await ctx.send(embed=ping_embed)


# @bot.command()
# async def lock(ctx):
#     roles = discord.Guild.get_role()
#     print(roles)
#     # await ctx.channel.set_permissions(
#     #     ctx.author, read_messages=True, send_messages=False
#     # )


@bot.command()
async def lock(ctx):
    # Get the guild object
    guild = ctx.guild

    # Get the moderator role (replace "moderator" with the actual role name)
    moderator_role = discord.utils.get(guild.roles, name="Moderator")
    member_role = discord.utils.get(guild.roles, name="Member")
    print(moderator_role)
    print(member_role)
    # Check if the role exists
    if not moderator_role:
        await ctx.send("There is no role named 'Moderator'.")
        return

    # Create an overwrite object to restrict send_messages permission
    overwrites = discord.PermissionOverwrite()
    overwrites.send_messages = False
    for channel in guild.text_channels:
        print(channel)
        # Set permissions for everyone except admins and moderators (including the bot)
        await channel.set_permissions(
            member_role, read_messages=True, send_messages=False
        )  # Specify 'everyone' as the target

        # Grant send_messages permission back to admins and moderators
        for role in guild.roles:
            print(f"{role} - {channel}")
            if role.permissions.administrator or role == moderator_role:
                await ctx.channel.set_permissions(
                    role, read_messages=True, send_messages=True
                )

    await ctx.send(" All Channel locked! Only admins and moderators can send messages.")


@bot.command()
async def unlock(ctx):
    # Get the guild object
    guild = ctx.guild

    # Get the moderator role (replace "moderator" with the actual role name)
    moderator_role = discord.utils.get(guild.roles, name="Moderator")
    member_role = discord.utils.get(guild.roles, name="Member")
    print(moderator_role)
    print(member_role)
    print(guild.text_channels)
    # for channel in guild.text_channels:
        # print(channel)
        # # Grant send_messages permission back to admins and moderators
        # for role in guild.roles:
        #     print(f"{role} - {channel}")
        #     await ctx.channel.set_permissions(
        #         role, read_messages=True, send_messages=True
        #     )
    
    # await ctx.send(" All Channel are Unlocked! Everyone can send messages.")


bot.run(" ")
