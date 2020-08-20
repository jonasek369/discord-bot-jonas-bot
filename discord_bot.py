import asyncio
import os
import youtube_dl
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime
import random
import requests
import json
import discord

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    check_live_jonasek369.start()
    check_live_panau9.start()
    check_live_agraelus.start()
    print("bot is on")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("mine prefix is ."))



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = '**né tak rychle** tento command můžes použít za {:.2f} sekunds'.format(error.retry_after)
        await ctx.send(msg)


@client.command
async def on_member_join(member):
    print(f"{member} se pripojil")


@client.command
async def on_member_remove(member):
    print(f"{member} se odpojil")


@client.command(aliases=["dev"])
async def developer(ctx):
    await ctx.send("developer of this bot is jonasek369#4537")


@client.command()
async def ping(ctx):
    now = datetime.now()
    cyear = now.year
    cmon = now.month
    cday = now.day
    chou = now.hour
    cmin = now.minute
    csec = now.second
    date = f"{chou}:{cmin}:{csec} {cday}:{cmon}:{cyear}"
    user = ctx .message.author
    await ctx.send(f"ping of this bot is {round(client.latency * 1000)}ms")
    print(date, f":{user} has pinged bot, ping of bot is {round(client.latency * 1000)}ms")


@client.command()
async def time(ctx):
    now = datetime.now()
    cyear = now.year
    cmon = now.month
    cday = now.day
    chou = now.hour
    cmin = now.minute
    csec = now.second
    await ctx.send(f"{chou}:{cmin}:{csec} {cday}:{cmon}:{cyear}")


@client.command()
async def hi(ctx):
    user = ctx.message.author
    await ctx.send(f"hi {user}")


@client.command(aliases=['rn', 'rannum'])
async def randomnumber(ctx, number1, number2):
    user = ctx.message.author
    r = random.randint(int(number1), int(number2))
    await ctx.send(f"{user} your number is {r}")


@client.command(aliases=["hot", "HOT"])
async def heads_or_tails(ctx, side):
    h_t = ["heads", "tails"]
    randomm = random.choice(h_t)
    if side == "tails":
        if randomm == "heads":
            await ctx.send("you lost it was heads")
        if randomm == "tails":
            await ctx.send("you won it was tails")
    if side == "heads":
        if randomm == "tails":
            await ctx.send("you lost it was tails")
        if randomm == "heads":
            await ctx.send("you won it was heads")


@client.command()
async def game(ctx, game):
    user = ctx.message.author
    print(f"{user} chce hrat {game}")
    channel = client.get_channel(733763230064836760)
    await channel.send(f"@everyone {user} want to play {game}")


@client.command(aliases=["cal", "calc"])
async def calculator(ctx, number, znacka, number2):
    if znacka == ":":
        await ctx.send(int(number) / int(number2))
    if znacka == "*":
        await ctx.send(int(number) * int(number2))
    if znacka == "-":
        await ctx.send(int(number) - int(number2))
    if znacka == "+":
        await ctx.send(int(number) + int(number2))


@tasks.loop(seconds=10)
async def check_live_jonasek369():
    API_ENDPOINT = "https://api.twitch.tv/helix/streams?user_login=jonasek369"

    Client_ID = "yourclientid"
    botToken = "yourbottoken"

    head = {
    'client-id': Client_ID,
    'authorization': 'Bearer ' + botToken
    }

    r = requests.get(url = API_ENDPOINT, headers = head, )


    w = r.text
    if "live" in w:
        channel = client.get_channel(673138335614631948)

        em = discord.Embed(title="Stream announcements", color=discord.Color.purple())
        streamer = "jonasek369"
        em.add_field(name="Streamer", value=streamer)
        em.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/b4b1e48c-0de6-4ac4-b7ec-19e2a6f66d7c-profile_image-70x70.png")
        em.set_footer(text ="check him out at https://www.twitch.tv/jonasek369")

        await channel.send(embed=em)
        await asyncio.sleep(1800)
    else:
        await asyncio.sleep(5)

@tasks.loop(seconds=10)
async def check_live_agraelus():
    API_ENDPOINT = "https://api.twitch.tv/helix/streams?user_login=agraelus"

    Client_ID = "yourclientid"
    botToken = "yourbottoken"

    head = {
    'client-id': Client_ID,
    'authorization': 'Bearer ' + botToken
    }

    r = requests.get(url = API_ENDPOINT, headers = head, )


    w = r.text
    if "live" in w:
        channel = client.get_channel(673138335614631948)

        em = discord.Embed(title="Stream announcements", color=discord.Color.purple())
        streamer = "agraelus"
        em.add_field(name="Streamer", value=streamer)
        em.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/ea3d506d-0339-40e7-ae44-eb104d5a546b-profile_image-70x70.png")
        em.set_footer(text ="check him out at https://www.twitch.tv/agraelus")

        await channel.send(embed=em)
        await asyncio.sleep(1800)
    else:
        await asyncio.sleep(5)


@tasks.loop(seconds=10)
async def check_live_panau9():
    API_ENDPOINT = "https://api.twitch.tv/helix/streams?user_login=the_chobis"


    Client_ID = "yourclientid"
    botToken = "yourbottoken"

    head = {
    'client-id': Client_ID,
    'authorization': 'Bearer ' + botToken
    }

    r = requests.get(url = API_ENDPOINT, headers = head, )


    w = r.text
    if "live" in w:
        channel = client.get_channel(673138335614631948)
        em = discord.Embed(title="Stream announcements", color=discord.Color.purple())

        streamer = "the_chobis"
        em.add_field(name="Streamer", value=streamer)
        em.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/a55c909f-3330-4fa1-a140-46c6b5418886-profile_image-70x70.png")
        em.set_footer(text="check him out at https://www.twitch.tv/the_chobis")

        await channel.send(embed=em)
        await asyncio.sleep(1800)
    else:
        await asyncio.sleep(40)


@client.command()
async def withdraw(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("zadej castku co ches vyzvednout")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("nemas tolik penez")
        return
    if amount<0:
        await ctx.send("částka musi byt kladná")
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1*amount,"bank")

    await ctx.send(f"vyzbednul sis {amount} coinu")


@client.command()
async def deposit(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("zadej castku co ches depozitnou")
        return

    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("nemas tolik penez")
        return
    if amount<0:
        await ctx.send("částka musi byt kladná")
        return


    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author, amount, "bank")

    await ctx.send(f"depositnul sis {amount} coinu")

@client.command()
async def send(ctx, member:discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("zadej castku co ches vyzvednout")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("nemas tolik penez")
        return
    if amount<0:
        await ctx.send("částka musi byt kladná")
        return

    await update_bank(ctx.author, -1*amount,"bank")
    await update_bank(member, amount, "bank")

    await ctx.send(f"dal jsi {amount} coinu {member}")

@commands.cooldown(1, 5, commands.BucketType.user)
@client.command(aliases=["bal"])
async def balance(ctx, member : discord.Member = None):
    if member == None:
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title=f"{ctx.author.name}'s balance", color=discord.Color.red())
        em.add_field(name="Wallet balance", value = wallet_amt)
        em.add_field(name="Bank balance", value = bank_amt)
        await ctx.send(embed=em)
        return

    await open_account(member)
    user = member
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f"{member.name}'s balance", color=discord.Color.red())
    em.add_field(name="Wallet balance", value=wallet_amt)
    em.add_field(name="Bank balance", value=bank_amt)
    await ctx.send(embed=em)

@commands.cooldown(1, random.randint(20, 120), commands.BucketType.user)
@client.command()
async def work(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    time = random.randint(4, 12)

    money = 8
    bonus = random.randint(0, 30)
    alfin = money * time
    fin = alfin + bonus
    users[str(user.id)]["wallet"] +=fin

    if bonus ==0:
        em = discord.Embed(title="paycheck from work")
        em.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/7/7b/United_States_one_dollar_bill%2C_obverse.jpg")
        em.add_field(name="paycheck", value=alfin)
        em.add_field(name="bonus", value=bonus)
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title="paycheck from work")
        em.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/7/7b/United_States_one_dollar_bill%2C_obverse.jpg")
        em.add_field(name="paycheck", value=alfin)
        em.add_field(name="bonus", value=bonus)
        await ctx.send(embed=em)




    with open("bank.json","w") as f:
        json.dump(users,f)

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("bank.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("bank.json","r") as f:
        users = json.load(f)

    return users

async def update_bank(user,change=0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change


    with open("bank.json","w") as f:
        json.dump(users,f)


    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]

    return bal

@commands.cooldown(1, 5, commands.BucketType.user)
@client.command()
async def slots(ctx, castka=None):

    await open_account(ctx.author)


    if castka == None:
        await ctx.send("zaděj částku")
        return

    bal = await update_bank(ctx.author)

    amount= int(castka)

    if amount>bal[0]:
        await ctx.send("nemáš tolik coinu")
        return
    if amount<0:
        ctx.send("částka musí být kladná")
        return

    a = random.choice([":cherries:", ":100:", ":seven:"])
    b = random.choice([":cherries:", ":100:", ":seven:"])
    c = random.choice([":cherries:", ":100:", ":seven:"])


    e = amount * 2


    w = str(e)



    if a == b ==c:
        await update_bank(ctx.author, -1 * amount)
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        em = discord.Embed(title=f"you won [({a},{b},{c})] you won", color=discord.Color.dark_green())
        em.add_field(name="vyhrál jsi", value=w)
        em.add_field(name="Zbývá ti", value=wallet_amt)
        await ctx.send(embed=em)
        await update_bank(ctx.author, 2 * amount)
        return

    else:
        await update_bank(ctx.author, -1 * amount)
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]

        em = discord.Embed(title=f"you lost [({a},{b},{c})] you lost", color=discord.Color.dark_green())
        em.add_field(name="prohrál jsi", value=castka)
        em.add_field(name="Zbývá ti", value=wallet_amt)
        await ctx.send(embed=em)
        return

client.remove_command("help")
@client.command()
async def help(ctx, command=None):

    module = command

    if module ==None:
        await ctx.send("zadej za .help názem commandu aby jsi se dozvěděl neco o určitém commandu")

    if module == "work":
        await ctx.send("pracuješ aby jsi ziskal pěníze")

    if module == "bal":
        await ctx.send("zjistíš kolik máš pěnez u sebe (wallet) nebo v bance")
        return

    if module == "balance":
        await ctx.send("zjistíš kolik máš pěnez u sebe (wallet) nebo v bance")
        return

    if module == "slots":
        await ctx.send(".slots (částka) můžeš vyhrát nebo prohrát svoje péníze")
        return

    if module == "withdraw":
        await ctx.send(".withdraw (částka) vyzvědneš si peníze ze sbojí banky .deposit(částka) aby jsi je poslal do banky")
        return

    if module == "deposit":
        await ctx.send(".deposit (částka) pošleš svoje peníze do svojí banky s .withdraw (částka) si je mužeš vyzvednout")
        return

    if module == "send":
        await ctx.send(".send (částka) (user) pošleš peníze někomu danýmu")
        return

    if module == "list":
        await ctx.send("otevře list všech commandu")
        return

    if module == "rules":
        await ctx.send("otevře pravidla serveru")
        return

    if module == "rps":
        await ctx.send("rps (user) rock paper scissors game")
        return
    else:
        await ctx.send("tento command neexistuje nebo neni přidán do tohoto listu")
        return

@client.command()
async def list(ctx):
    file = open("commands.txt", "r")
    f = file.read()
    await ctx.send(f)

@client.command()
async def rules(ctx):
    file = open("rules.txt", "r")
    f = file.read()
    await ctx.send(f)


@client.command()
async def rps(ctx, member : discord.Member):



    if member == ctx.author:
        await ctx.send("you cant have rock paper scissors fight with your self")
        return

    author = ctx.author



    msg1 = await member.send(f"{author} has started battle of rock paper scissors if you accept react with :white_check_mark: to this message if you dont want to play react with :negative_squared_cross_mark:")
    msg2 = await author.send(f"you challenged {member} to game of rock paper scissors you need to wait now till {member} accept or decline")
    def check(reaction, user):
        return user == member and str(reaction.emoji) == "✅" or "❎" and reaction.message.id == msg1.id

    reaction, user = await client.wait_for('reaction_add', timeout=None, check=check)

    if str(reaction.emoji) =="✅":
        await msg1.delete()
        await author.send(f"{member} accepted your battle waiting for his choice ")
        members_choice_1 = await member.send(f"you accepted {author}'s invite chose 🥌 for rock ✂ for scissors 📰 for paper")
        def check(reaction, user):
            return user == member and str(reaction.emoji) == "🥌" or "✂" or "📰"  and reaction.message.id == members_choice_1.id

        reaction, user = await client.wait_for('reaction_add', timeout=None, check=check)



    if str(reaction.emoji) == "🥌":
        author_choice_1 = await author.send(f"{member} chose his item, now your turn 🥌 for rock ✂ for scissors 📰 for paper")
        def check(reaction, user):
            return user == member and str(reaction.emoji) == "🥌" or "✂" or "📰"  and reaction.message.id == author_choice_1.id

        reaction, user = await client.wait_for('reaction_add', timeout=None, check=check)
        if str(reaction.emoji) == "🥌":
            await author.send(f"its a tie you both chose rock")
            await member.send(f"its a tie you both chose rock")
            return

        if str(reaction.emoji) == "📰":
            await author.send(f"you won you chose paper {member} chose rock")
            await member.send(f"you lost you chose rock {author} chose paper")
            return

        if str(reaction.emoji) == "✂":
            await author.send(f"you lost you chose scissors {member} chose rock")
            await member.send(f"you won you chose rock {author} chose rock ")
            return



    if str(reaction.emoji) == "✂":
        author_choice_2 = await author.send(f"{member} chose his item, now your turn 🥌 for rock ✂ for scissors 📰 for paper")

        def check(reaction, user):
            return user == member and str(reaction.emoji) == "🥌" or "✂" or "📰" and reaction.message.id == author_choice_2.id

        reaction, user = await client.wait_for('reaction_add', timeout=None, check=check)
        if str(reaction.emoji) == "🥌":
            await author.send(f"you won you chose rock {member} chose scissors")
            await member.send(f"you lost you chose scissors {author} chose rock")
            return
        if str(reaction.emoji) == "📰":
            await author.send(f"you lost you chose paper {member} chose scissors")
            await member.send(f"you won you chose scissors {author} chose paper")
            return
        if str(reaction.emoji) == "✂":
            await author.send(f"its tie you booth chose rock")
            await member.send(f"its tie you booth chose rock")
            return




    if str(reaction.emoji) == "📰":
        author_choice_3 = await author.send(f"{member} chose his item, now your turn 🥌 for rock ✂ for scissors 📰 for paper")

        def check(reaction, user):
            return user == member and str(reaction.emoji) == "🥌" or "✂" or "📰" and reaction.message.id == author_choice_3.id

        reaction, user = await client.wait_for('reaction_add', timeout=None, check=check)

        if str(reaction.emoji) == "🥌":
            await author.send(f"you lost you chose rock {member} chose paper")
            await member.send(f"you won you chose paper {author} chose rock")
            return
        if str(reaction.emoji) == "📰":
            await author.send(f"its a tie you both chose paper")
            await member.send(f"its a tie you both chose paper")
            return
        if str(reaction.emoji) == "✂":
            await author.send(f"you won you chose scissors {member} chose paper")
            await member.send(f"you lost you chose paper {author} chose scissors ")
            return


    if str(reaction.emoji) =="❎":
        await msg1.delete()
        w = await author.send(f"{member} decline your battle ")
        await asyncio.sleep(20)
        await w.delete()
        return


@client.command(aliases=["eco+", "economics+"])
async def economics_plus(ctx, member: discord.Member, amount):
    if ctx.author.id == 395165520229433344:
        await open_account(member)
        user = member
        users = await get_bank_data()

        amount = int(amount)

        users[str(user.id)]["wallet"] += amount

        await ctx.send(f"{ctx.author.name} has added {amount} of coins to {member} account")

        with open("bank.json", "w") as f:
            json.dump(users, f)
    else:
        await ctx.send("you dont have the permission")
        print(f"{ctx.author} has tried to add someone money")

@client.command(aliases=["eco-", "economics-"])
async def economics_minus(ctx, member: discord.Member, amount):
    if ctx.author.id == 395165520229433344:
        await open_account(member)
        user = member
        users = await get_bank_data()

        amount = int(amount)

        users[str(user.id)]["wallet"] -= amount

        await ctx.send(f"{ctx.author.name} has removed {amount} of coins to {member} account")

        with open("bank.json", "w") as f:
            json.dump(users, f)
    else:
        await ctx.send("you dont have the permission")
        print(f"{ctx.author} has tried to remove someone money")

@client.command(aliases=["resetacc", "reset"])
async def reset_acc_money(ctx, member: discord.Member):
    if ctx.author.id == 395165520229433344:
        await open_account(member)
        user = member
        users = await get_bank_data()

        users[str(user.id)]["wallet"] = 0

        await ctx.send(f"{ctx.author.name} has reseted account to {member} account")

        with open("bank.json", "w") as f:
            json.dump(users, f)
    else:
        await ctx.send("you dont have the permission")
        print(f"{ctx.author} has tried to remove someone money")

@client.command()
@commands.has_permissions(ban_members=True)
async def profile(ctx,*,  user: discord.Member = None):
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=user.color, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)

@client.command()
async def kick(ctx, member: discord.Member, *, reason = "Žádný důvod nebyl dán"):
    await member.send(f"byl jsi kicknut z {ctx.guild.name} důvod :  {reason}")
    await member.kick(reason=reason)


@client.command()
async def meme(ctx):

    reddit = praw.Reddit(client_id="reddit_client_id",
                         client_secret="reddit_secret",
                         username="reddit_username",
                         password="reddit_password",
                         user_agent="user_agent")
    subreddit = reddit.subreddit("dankmemes")
    all_subs = []

    top = subreddit.top(limit=200)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url
    author = random_sub.author

    em = discord.Embed(title=name,color=discord.Color.orange())
    em.set_image(url=url)
    em.set_footer(text=f"from r/memes by u/{author}")
    await ctx.send(embed=em)


client.run("yourbottoken")
