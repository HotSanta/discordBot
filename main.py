import random as r
import asyncio, time
import os
import os.path
import discord
from discord.ext import commands
import requests
import json

sleepVar = 0.5

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!logan', intents=intents)


@bot.event
async def on_connect():
  print("Bot is Online")


@bot.command()
async def Message(ctx):
  await ctx.send("Logan is the best")


@bot.command()
async def Help(ctx):
  await ctx.send(
    "Commands with bot\n1. !loganMessage\n2. !loganRps (rock, paper, scissors, plays)\n3. !loganAdd (value1, value2)\n4. !loganSub (value1, value2)\n5. !loganMult (value1, value2\n6. !loganDiv (value1, value2)\n7. !loganName (name)\n8. !loganTime (time, Am or Pm)"
  )


@bot.command(aliases=["rps", "RPS"])
async def Rps(ctx, message):
  answer = message.lower()
  possible = ["rock", "paper", "scissors"]
  botAnswer = r.choice(possible)
  if answer not in possible:
    if answer == "plays":
      file_open = open("NumberOfTimesRun.txt", "r")
      read = file_open.read()
      await ctx.send("I've played rock, paper, scissors " + read + " times!")
    else:
      await ctx.send("Input not understood. Try Again")
  else:
    file_open = open("NumberOfTimesRun.txt", "r")
    read = file_open.read()
    x = int(read) + 1
    file_open.close()
    file_open = open("NumberOfTimesRun.txt", "w")
    file_open.write(str(x))
    file_open.close()
    await ctx.send("Your input: " + answer)
    time.sleep(sleepVar)
    await ctx.send("Bot's input: " + botAnswer)
    time.sleep(sleepVar)
    if botAnswer == answer:
      await ctx.send("You tied, both with " + answer)
    elif botAnswer == "rock":
      if answer == "scissors":
        await ctx.send("You lost, as " + botAnswer + " beats " + answer)
      elif answer == "paper":
        await ctx.send("You Won, as " + answer + " beats " + botAnswer)
    elif botAnswer == "paper":
      if answer == "scissors":
        await ctx.send("You Won, as " + answer + " beats " + botAnswer)
      elif answer == "rock":
        await ctx.send("You lost, as " + botAnswer + " beats " + answer)
    elif botAnswer == "scissors":
      if answer == "rock":
        await ctx.send("You Won, as " + answer + " beats " + botAnswer)
      elif answer == "paper":
        await ctx.send("You lost, as " + botAnswer + " beats " + answer)


@bot.command()
async def Add(ctx, value1, value2):
  if value1.strip('-').isnumeric() and value2.strip('-').isnumeric():
    sum = int(value1) + int(value2)
    await ctx.send(str(value1) + " + " + str(value2) + " = " + str(sum))
  else:
    await ctx.send("Answer couldn't be computed")


@bot.command()
async def Sub(ctx, value1, value2):
  if value1.strip('-').isnumeric() and value2.strip('-').isnumeric():
    sum = int(value1) - int(value2)
    await ctx.send(str(value1) + " - " + str(value2) + " = " + str(sum))
  else:
    await ctx.send("Answer couldn't be computed")


@bot.command()
async def Mult(ctx, value1, value2):
  if value1.strip('-').isnumeric() and value2.strip('-').isnumeric():
    sum = int(value1) * int(value2)
    await ctx.send(str(value1) + " * " + str(value2) + " = " + str(sum))
  else:
    await ctx.send("Answer couldn't be computed")


@bot.command()
async def Div(ctx, value1, value2):
  if value1.strip('-').isnumeric() and value2.strip('-').isnumeric():
    sum = int(value1) / int(value2)
    await ctx.send(str(value1) + " / " + str(value2) + " = " + str(sum))
  else:
    await ctx.send("Answer couldn't be computed")


@bot.command()
async def Name(ctx, name):
  await ctx.send("Hello " + name + "!")


@bot.command()
async def Time(ctx, time, amPm):
  if amPm.lower() == "am":
    if time in ["12", "1", "2", "3", "4"]:
      await ctx.send("Good Night!")
    elif time in ["5", "6", "7", "8", "9", "10", "11"]:
      await ctx.send("Good Morning!")
  elif amPm.lower() == "pm":
    if time in ["12", "1", "2", "3", "4", "5"]:
      await ctx.send("Good Afternoon!")
    elif time in ["6", "7", "8", "9", "10", "11"]:
      await ctx.send("Good Night!")


@bot.command()
async def Banana(ctx):
  await ctx.send(
    "https://domf5oio6qrcr.cloudfront.net/medialibrary/6372/202ebeef-6657-44ec-8fff-28352e1f5999.jpg"
  )


@bot.command()
async def RandomSesame(ctx):
  imageList = [
    "https://static.wikia.nocookie.net/muppet/images/5/5a/Elmo-elmo-elmo.jpg/revision/latest/scale-to-width-down/280?cb=20110917000614",
    "https://static.wikia.nocookie.net/muppet/images/0/08/CookieMonsterWaving.jpg/revision/latest/scale-to-width-down/280?cb=20120128192952",
    "https://static.wikia.nocookie.net/muppet/images/9/92/Bigbirdnewversion.png/revision/latest/scale-to-width-down/280?cb=20120128201030",
    "https://static.wikia.nocookie.net/muppet/images/e/e1/Bert_smile.png/revision/latest/scale-to-width-down/280?cb=20110630173259",
    "https://static.wikia.nocookie.net/muppet/images/c/c3/Oscar-can2.jpg/revision/latest/scale-to-width-down/280?cb=20090819003837",
    "https://static.wikia.nocookie.net/muppet/images/f/f7/GroverFullFigure2.png/revision/latest/scale-to-width-down/280?cb=20190222025220"
  ]
  x = r.randint(0, int(len(imageList)) - 1)
  await ctx.send(imageList[x])


@bot.command()
async def EightBall(ctx, *, phrase: str):
  ouputList = [
    "Without a Doubt", "Yes definitely", "As I see it, yes", "Yes",
    "Ask again later", "Cannot predict now", "My reply is no",
    "Outlook not so good"
  ]
  rand = r.randint(0, int(len(ouputList)) - 1)
  output = ouputList[rand]
  if output != "Cannot predict now" or output != "Ask again later":
    await ctx.send(phrase + " : " + output)
  else:
    await ctx.send(output)


@bot.command()
async def Dance(ctx, times):
  if times.isnumeric():
    messages = ["┏(・o･)┛", "┗( ･o･)┓"]
    for x in range(int(times)):
      message = await ctx.send(messages[x % 2])
      await message.delete()
  else:
    await ctx.send("Command was not understood")


def check(name, v1, p1, v2, p2, v3, p3):
  open_file = open(name, "r")
  ValidMoves = open_file.readline().strip("\n").split("|")
  board = []
  for _ in range(3):
    value = open_file.readline()
    board.append(value.strip("\n").split(","))
  print(board)
  open_file.close()
  if board[v1][p1] == ":green_circle:" and board[v2][p2] == ":green_circle:" and board[v3][p3] == ":green_circle:":
    print("You Won!")
    os.remove(name)


def Checks(name):
  check(name, 0, 0, 0, 1, 0, 2)
  check(name, 1, 0, 1, 1, 1, 2)
  check(name, 2, 0, 2, 1, 2, 2)
  check(name, 0, 0, 1, 0, 2, 0)
  check(name, 0, 1, 1, 1, 2, 1)
  check(name, 0, 2, 1, 2, 2, 2)
  check(name, 0, 0, 1, 1, 2, 2)
  check(name, 0, 2, 1, 1, 2, 0)


@bot.command()
async def Play(ctx, x, y):
  if os.path.exists(str(ctx.author.name)):
    open_file = open(str(ctx.author.name), "r")
    value = open_file.read()
    open_file.close()
    print(value)
    if value != "|":
      open_file = open(str(ctx.author.name), "r")
      ValidMoves = open_file.readline().strip("\n").split("|")
      print(type(ValidMoves))
      if not ValidMoves == [[''], [''], ['']]:
        board = []
        for _ in range(3):
          value = open_file.readline()
          board.append(value.strip("\n").split(","))
        open_file.close()
        move = x + "," + y
        if move in ValidMoves:
          board[int(x) - 1][int(y) - 1] = ":green_circle:"
          ValidMoves.remove(x + "," + y)
          L1 = "".join(board[0])
          L2 = "".join(board[1])
          L3 = "".join(board[2])
          await ctx.send("\nYour Play\n")
          await ctx.send(L1 + "\n" + L2 + "\n" + L3)
          Line1 = ",".join(board[0])
          Line2 = ",".join(board[1])
          Line3 = ",".join(board[2])
          Lines = [Line1, Line2, Line3]
          phrase = "\n".join(Lines)
          phrase1 = ""
          for l in range(int(len(ValidMoves))):
            phrase1 += ValidMoves[l] + "|"
          phrase1 = phrase1[:0] + "" + phrase1[:-1]
          print(phrase1)
          open_file = open(str(ctx.author.name), "w")
          open_file.write(phrase1 + "\n" + phrase)
          open_file.close()
          Checks(str(ctx.author.name))
          #if ValidMoves != []:
          # botPlay()
        else:
          await ctx.send("Invalid Move")
      else:
        os.remove(str(ctx.author.name))
    else:
      print("over")
      os.remove(str(ctx.author.name))
  else:
    await ctx.send(
      "```You are not currently playing TicTacToe\nUse !loganTicTacToe to begin```"
    )


@bot.command()
async def TicTacToe(ctx):
  open_file = open(str(ctx.author.name), "w")
  open_file.write(
    "1,1|1,2|1,3|2,1|2,2|2,3|3,1|3,2|3,3\n:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:"
  )
  open_file.close()
  await ctx.send(
    "```You are now playing TictacToe\nUse !loganPlay x y to place your move```"
  )


my_secret = os.environ['TOKEN']
bot.run(my_secret)
