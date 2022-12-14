import random as r
import asyncio, time
import os
import os.path
import discord
from discord.ui import Button, View
from discord.ext import commands
import requests
import json
import csv

sleepVar = 0.5

intents = discord.Intents.all()
helpCommand = commands.DefaultHelpCommand(no_category="Commands")

bot = commands.Bot(command_prefix='!logan',
                   intents=intents,
                   helpCommand=helpCommand)


@bot.event
async def on_connect():
  print("Bot is Online")


@bot.command(brief=" Sends Logan is the Best",
             description=" Sends a message which states Logan is the best",
             Arguements="None")
async def Message(ctx):
  await ctx.send("Logan is the best")


@bot.command(
  aliases=["rps", "RPS"],
  brief=" Plays Rock paper scissors",
  description=
  ' Has options of Rock, Paper, Scissors, and Plays. The first three will have you battle the bot in rock, paper, scissors, while plays will display how many times the bot has played Rock, Paper, Scissors',
  Arguements="Rock,Paper,Scissors,Plays")
async def Rps(ctx, message):
  answer = message.lower()
  possible = ["rock", "paper", "scissors"]
  botAnswer = r.choice(possible)
  if answer not in possible:
    if answer == "plays":
      file_open = open("NumberOfTimesRun:.txt", "r")
      read = file_open.read()
      await ctx.send("I've played rock, paper, scissors " + read + " times!")
    else:
      await ctx.send("Input not understood. Try Again")
  else:
    file_open = open("NumberOfTimesRun:.txt", "r")
    read = file_open.read()
    x = int(read) + 1
    file_open.close()
    file_open = open("NumberOfTimesRun:.txt", "w")
    file_open.write(str(x))
    file_open.close()
    await ctx.send("Your input: " + answer)
    await asyncio.sleep(sleepVar)
    await ctx.send("Bot's input: " + botAnswer)
    await asyncio.sleep(sleepVar)
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


@bot.command(
  brief=" Adds two given values",
  description=' The format for adding is !LoganAdd (Value1) (Value2)',
  Arguements="Value1 Value2")
async def Add(ctx, value1, value2):
  if value1.strip('-').isnumeric() and value2.strip('-').isnumeric():
    sum = int(value1) + int(value2)
    await ctx.send(str(value1) + " + " + str(value2) + " = " + str(sum))
  else:
    await ctx.send("Answer couldn't be computed")


@bot.command(
  brief=" Subtracts two given values",
  description=' The format for Subtracting is !LoganSub (Value1) (Value2)',
  Arguements="Value1 Value2")
async def Sub(ctx, value1, value2):
  if value1.strip('-').isnumeric() and value2.strip('-').isnumeric():
    sum = int(value1) - int(value2)
    await ctx.send(str(value1) + " - " + str(value2) + " = " + str(sum))
  else:
    await ctx.send("Answer couldn't be computed")


@bot.command(
  brief=" Multiplies two given values",
  description=' The format for Multiplying is !LoganMult (Value1) (Value2)',
  Arguements="Value1 Value2")
async def Mult(ctx, value1, value2):
  if value1.strip('-').isnumeric() and value2.strip('-').isnumeric():
    sum = int(value1) * int(value2)
    await ctx.send(str(value1) + " * " + str(value2) + " = " + str(sum))
  else:
    await ctx.send("Answer couldn't be computed")


@bot.command(
  brief=" Divides two given values",
  description=' The format for Dividing is !LoganDiv (Value1) (Value2)',
  Arguements="Value1 Value2")
async def Div(ctx, value1, value2):
  if value1.strip('-').isnumeric() and value2.strip('-').isnumeric():
    sum = int(value1) / int(value2)
    await ctx.send(str(value1) + " / " + str(value2) + " = " + str(sum))
  else:
    await ctx.send("Answer couldn't be computed")


@bot.command(brief=" Says hello to a given name",
             description=' The format for Name is !LoganName (name)',
             Arguements="name")
async def Name(ctx, name):
  await ctx.send("Hello " + name + "!")


@bot.command(
  brief=" Gives a response from a given time",
  description=' The format for Time is !LoganTime 11 pm(Or any other time)',
  Arguements="None")
async def Time(ctx, Time, amPm):
  if amPm.lower() == "am":
    if Time in ["12", "1", "2", "3", "4"]:
      await ctx.send("Good Night!")
    elif Time in ["5", "6", "7", "8", "9", "10", "11"]:
      await ctx.send("Good Morning!")
  elif amPm.lower() == "pm":
    if Time in ["12", "1", "2", "3", "4", "5"]:
      await ctx.send("Good Afternoon!")
    elif Time in ["6", "7", "8", "9", "10", "11"]:
      await ctx.send("Good Night!")


@bot.command(
  brief=" Sends a photo of a banana",
  description=
  " Sends a banana photo of a heart. No further parameters are needed for this command",
  Arguements="None")
async def Banana(ctx):
  await ctx.send(
    "https://domf5oio6qrcr.cloudfront.net/medialibrary/6372/202ebeef-6657-44ec-8fff-28352e1f5999.jpg"
  )


@bot.command(
  brief=" Sends a picture of a random sesame street character",
  description=
  " Sends a random photo of a sesame street character from a list of characters. No further parameters are needed for this command",
  Arguements="None")
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


@bot.command(
  brief=" Tells you the probability of your question happening",
  description=" The format for EightBall is !LoganEightBall (Question)",
  Arguements="Question")
async def EightBall(ctx, *, phrase: str):
  ouputList = [
    "Without a Doubt", "Yes definitely", "As I see it, yes", "Yes",
    "Ask again later", "Cannot predict now", "My reply is no",
    "Outlook not so good"
  ]
  rand = r.randint(0, int(len(ouputList)) - 1)
  output = ouputList[rand]
  await ctx.send(phrase + " : " + output)


@bot.command(
  brief=" Dances",
  description=" Uses sending and unsending message to have the bot dance",
  Arguements="None")
async def Dance(ctx, times):
  if times.isnumeric():
    messages = ["???(???o???)???", "???( ???o???)???"]
    for x in range(int(times)):
      message = await ctx.send(messages[x % 2])
      await asyncio.sleep(.5)
      await message.delete()
  else:
    await ctx.send("Command was not understood")


@bot.command(
  brief=" Sends a random joke, split up into setup and punchline",
  description=
  " Uses a joke API to send a random setup and punchline. No further parameters needing for this command",
  Arguements="None")
async def Joke(ctx):

  # created variable for the joke api url
  url = "https://official-joke-api.appspot.com/random_joke"

  # contact url
  req = requests.get(url)

  # get data from joke url
  data = req.json()

  # the data
  setup = data["setup"]
  punchLine = data["punchline"]

  await ctx.send(setup)
  await asyncio.sleep(2)
  await ctx.send(punchLine)


@bot.command(
  brief=" Gives you a brief description and temperature of a given zip code",
  description=" The format for weather is !LoganWeather (Valid Zip code)",
  Arguements="Zip Code")
async def Weather(ctx, zip):
  my_API = os.environ['WeatherAPIkey']
  url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",US&appid=" + my_API

  req = requests.get(url)

  data = req.json()

  description = data["weather"][0]["description"]
  temp = data["main"]["temp"]
  celsisus = float(temp) - 273.16
  faren = (celsisus * 1.8) + 32
  temp = round(faren, 1)
  await ctx.send(zip + "'s' description is " + description +
                 ", and it has a temp of " + str(temp) +
                 " degrees fahrenheit right now")


#============================================================


# api with parameter
@bot.command(
  brief=" Uses your name to guess your age, gender, and nationality",
  description=" The format for NP is !loganNP (name)",
  Arguements="Name")
async def NP(ctx, Name):
  # uses name to get a guess of someone's age
  url = 'https://api.agify.io/?name=' + Name
  req = requests.get(url)
  data = req.json()
  Age = data["age"]

  # uses name to get a guess of someone's gender
  url = 'https://api.genderize.io/?name=' + Name
  req = requests.get(url)
  data = req.json()
  Gender = data["gender"]

  # uses name to get a guess of someone's nationality
  url = "https://api.nationalize.io/?name=" + Name
  req = requests.get(url)
  data = req.json()
  identity1 = data["country"][0]["probability"]
  identity2 = data["country"][1]["probability"]
  identity3 = data["country"][2]["probability"]
  identity4 = data["country"][3]["probability"]
  identity5 = data["country"][4]["probability"]
  # the five guesses the website creates
  identities = [identity1, identity2, identity3, identity4, identity5]
  # finds the highest value of the five guesses
  TrueIdentity = 0
  for x in range(5):
    if identities[x] >= TrueIdentity:
      TrueIdentity = identities[x]
  identity = identities.index(TrueIdentity)
  # This system works, but I found out the first listed nationality is always the highest, so finding the highest wasn't needed
  Nationality = data["country"][identity]["country_id"]

  # takes in the country code of the Nationality and gives its country name
  url = "http://country.io/names.json"
  req = requests.get(url)
  data = req.json()
  Country = data[Nationality]

  # sends a combination of all the above data

  await ctx.send("```Your name is " + Name + ", so your age is probably " +
                 str(Age) + ", you are most likely a " + str(Gender) +
                 ", and from " + Country + ".```")


# regular definition using api key
@bot.command(
  brief=
  " Gives you the top definition of the given war from Modern Dictionary of the given word",
  description=" The format for Def is !loganDef (English Word)",
  Arguements="Word")
async def Def(ctx, message):

  url = "https://modern-dictionary.p.rapidapi.com/en/"

  querystring = {"word": message}

  my_secret = os.environ['DefKey']
  headers = {
    "X-RapidAPI-Key": my_secret,
    "X-RapidAPI-Host": "modern-dictionary.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  data = response.json()
  definition = data["meanings"][0]["definitions"][0]["definition"]
  await ctx.send("```The definition to " + message + " is\n\t-" + definition +
                 "```")


#urban dictionary using api key
@bot.command(
  brief=" Gives you the top definition from urban dictionary of the given word",
  description=" The format for UrbanDef is !loganUrbanDef (English Word)",
  Arguements="Word")
async def UrbanDef(ctx, message):

  url = "https://urban-dictionary7.p.rapidapi.com/v0/define"
  querystring = {"term": message}

  my_secret = os.environ['DefKey']

  headers = {
    "X-RapidAPI-Key": my_secret,
    "X-RapidAPI-Host": "urban-dictionary7.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  data = response.json()
  definition = data["list"][0]["definition"]

  await ctx.send("```The definition to " + message + " is\n\t-" + definition +
                 ".```")


#============================================================

player, opponent = ':x:', ':green_circle:'


def isMovesLeft(board):

  for i in range(3):
    for j in range(3):
      if (board[i][j] == ':white_large_square:'):
        return True
  return False


def evaluate(b):

  # Checking for Rows for X or O victory.
  for row in range(3):
    if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
      if (b[row][0] == player):
        return 10
      elif (b[row][0] == opponent):
        return -10

  # Checking for Columns for X or O victory.
  for col in range(3):

    if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

      if (b[0][col] == player):
        return 10
      elif (b[0][col] == opponent):
        return -10

  # Checking for Diagonals for X or O victory.
  if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

    if (b[0][0] == player):
      return 10
    elif (b[0][0] == opponent):
      return -10

  if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

    if (b[0][2] == player):
      return 10
    elif (b[0][2] == opponent):
      return -10

  # Else if none of them have won then return 0
  return 0


# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax):
  score = evaluate(board)

  # If Maximizer has won the game return his/her
  # evaluated score
  if (score == 10):
    return score

  # If Minimizer has won the game return his/her
  # evaluated score
  if (score == -10):
    return score

  # If there are no more moves and no winner then
  # it is a tie
  if (isMovesLeft(board) == False):
    return 0

  # If this maximizer's move
  if (isMax):
    best = -1000

    # Traverse all cells
    for i in range(3):
      for j in range(3):

        # Check if cell is empty
        if (board[i][j] == ':white_large_square:'):

          # Make the move
          board[i][j] = player

          # Call minimax recursively and choose
          # the maximum value
          best = max(best, minimax(board, depth + 1, not isMax))

          # Undo the move
          board[i][j] = ':white_large_square:'
    return best

  # If this minimizer's move
  else:
    best = 1000

    # Traverse all cells
    for i in range(3):
      for j in range(3):

        # Check if cell is empty
        if (board[i][j] == ':white_large_square:'):

          # Make the move
          board[i][j] = opponent

          # Call minimax recursively and choose
          # the minimum value
          best = min(best, minimax(board, depth + 1, not isMax))

          # Undo the move
          board[i][j] = ':white_large_square:'
    return best


# This will return the best possible move for the player
def findBestMove(board):
  bestVal = -1000
  bestMove = (-1, -1)

  # Traverse all cells, evaluate minimax function for
  # all empty cells. And return the cell with optimal
  # value.
  for i in range(3):
    for j in range(3):

      # Check if cell is empty
      if (board[i][j] == ':white_large_square:'):

        # Make the move
        board[i][j] = player

        # compute evaluation function for this
        # move.
        moveVal = minimax(board, 0, False)

        # Undo the move
        board[i][j] = ':white_large_square:'

        # If the value of the current move is
        # more than the best value, then update
        # best
        if (moveVal > bestVal):
          bestMove = (i, j)
          bestVal = moveVal

  return bestMove


def botcheck(name, v1, p1, v2, p2, v3, p3):
  open_file = open(name, "r")
  ValidMoves = open_file.readline().strip("\n").split("|")
  board = []
  for _ in range(3):
    value = open_file.readline()
    board.append(value.strip("\n").split(","))
  open_file.close()
  if board[v1][p1] == ":x:" and board[v2][p2] == ":x:" and board[v3][
      p3] == ":x:":
    open_file = open(name, "w")
    open_file.write("Bot Won!")
    open_file.close()


def check(name, v1, p1, v2, p2, v3, p3):
  open_file = open(name, "r")
  ValidMoves = open_file.readline().strip("\n").split("|")
  board = []
  for _ in range(3):
    value = open_file.readline()
    board.append(value.strip("\n").split(","))
  open_file.close()
  if board[v1][p1] == ":green_circle:" and board[v2][
      p2] == ":green_circle:" and board[v3][p3] == ":green_circle:":
    open_file = open(name, "w")
    open_file.write("You Won!")
    open_file.close()


def Checks(name):
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()
  if not (x == ['You Won!'] or x == ['Bot Won!']):
    check(name, 0, 0, 0, 1, 0, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()
  if not (x == ['You Won!'] or x == ['Bot Won!']):
    check(name, 1, 0, 1, 1, 1, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()
  if not (x == ['You Won!'] or x == ['Bot Won!']):
    check(name, 2, 0, 2, 1, 2, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()
  if not (x == ['You Won!'] or x == ['Bot Won!']):
    check(name, 0, 0, 1, 0, 2, 0)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()
  if not (x == ['You Won!'] or x == ['Bot Won!']):
    check(name, 0, 1, 1, 1, 2, 1)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    check(name, 0, 2, 1, 2, 2, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    check(name, 0, 0, 1, 1, 2, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    check(name, 0, 2, 1, 1, 2, 0)

  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    botcheck(name, 0, 0, 0, 1, 0, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    botcheck(name, 1, 0, 1, 1, 1, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    botcheck(name, 2, 0, 2, 1, 2, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    botcheck(name, 0, 0, 1, 0, 2, 0)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    botcheck(name, 0, 1, 1, 1, 2, 1)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    botcheck(name, 0, 2, 1, 2, 2, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    botcheck(name, 0, 0, 1, 1, 2, 2)
  open_file = open(name, "r")
  x = open_file.readline().strip("\n").split("|")
  open_file.close()

  if not (x == ['You Won!'] or x == ['Bot Won!']):
    botcheck(name, 0, 2, 1, 1, 2, 0)


def BotPlay(NAME):
  chance = r.randint(1, 3)
  open_file = open(NAME, "r")
  ValidMoves = open_file.readline().strip("\n").split("|")
  board = []
  for _ in range(3):
    value = open_file.readline()
    board.append(value.strip("\n").split(","))
  open_file.close()
  # Has a 1/3 to play a random move, and a 2/3 chance to play the best move
  if chance in [2, 3]:
    bestMove = findBestMove(board)
    play = str(bestMove[0] + 1) + "," + str(bestMove[1] + 1)
  elif chance == 1:
    play = r.choice(ValidMoves)
  board[int(play[0]) - 1][int(play[2]) - 1] = ":x:"
  ValidMoves.remove(play)
  L1 = "".join(board[0])
  L2 = "".join(board[1])
  L3 = "".join(board[2])
  Line1 = ",".join(board[0])
  Line2 = ",".join(board[1])
  Line3 = ",".join(board[2])
  Lines = [Line1, Line2, Line3]
  phrase = "\n".join(Lines)
  phrase1 = ""
  for l in range(int(len(ValidMoves))):
    phrase1 += ValidMoves[l] + "|"
  phrase1 = phrase1[:0] + "" + phrase1[:-1]
  open_file = open(NAME, "w")
  open_file.write(phrase1 + "\n" + phrase)
  open_file.close()
  return L1 + "\n" + L2 + "\n" + L3


@bot.command(
  brief=" Allows you to face a bot in TicTacToe",
  description=
  " Once you start the game, using !loganTicTacToe, this uses an x and y cord to place pieces",
  Arguements="X Y")
async def Play(ctx, x, y):
  if os.path.exists(str(ctx.author.name)):
    open_file = open(str(ctx.author.name), "r")
    ValidMoves = open_file.readline().strip("\n").split("|")
    if not (ValidMoves == ['You Won!'] or ValidMoves == ['Bot Won!']):
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
        open_file = open(str(ctx.author.name), "w")
        open_file.write(phrase1 + "\n" + phrase)
        open_file.close()
        if ValidMoves != []:
          botPlay = BotPlay(str(ctx.author.name))
          await ctx.send("\nBot Move\n")
          await ctx.send(botPlay)
        Checks(str(ctx.author.name))
        open_file = open(str(ctx.author.name), "r")
        x = open_file.readline().strip("\n").split("|")
        open_file.close()
        if x == ['You Won!']:
          await ctx.send("You Won!")
          os.remove(str(ctx.author.name))
        elif x == ['Bot Won!']:
          await ctx.send("Bot Won!")
          os.remove(str(ctx.author.name))
        elif ValidMoves == []:
          await ctx.send("No-One Won!")
          os.remove(str(ctx.author.name))
      else:
        await ctx.send("Invalid Move")
  else:
    await ctx.send(
      "```You are not currently playing TicTacToe\nUse !loganTicTacToe to begin```"
    )


@bot.command(
  brief=" Starts your TicTacToe game against the bot",
  description=
  " Must be used before you start and then once ran, you use !loganPlay x y to place pieces",
  Arguements="None")
async def TicTacToe(ctx):
  open_file = open(str(ctx.author.name), "w")
  open_file.write(
    "1,1|1,2|1,3|2,1|2,2|2,3|3,1|3,2|3,3\n:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:"
  )
  open_file.close()
  await ctx.send(
    "```You are now playing TictacToe\nUse !loganPlay x y to place your move```"
  )


#============================================================


def checks(piece, last, name):
  board = []
  open_file = open(name, "r")
  thing = open_file.readline()
  thing2 = open_file.readline()
  for x in range(6):
    value = open_file.readline()
    board.append(value.strip("\n").split(","))
  open_file.close()
  cords = last.split(',')
  i = int(cords[0])  # row/x
  j = int(cords[1])  # colum/y
  # checks for 000_
  if j > 2:
    if board[i][j - 1] == piece and board[i][j - 2] == piece and board[i][
        j - 3] == piece:
      return piece + " won"
  # checks for _000
  if j < 4:
    if board[i][j + 1] == piece and board[i][j + 2] == piece and board[i][
        j + 3] == piece:
      return piece + " won"
  # checks for downs
  if i < 3:
    if board[i + 1][j] == piece and board[i + 2][j] == piece and board[
        i + 3][j] == piece:
      return piece + " won"
  #check if you place in a 00_0
  if not j in [0, 1, 6]:
    if board[i][j + 1] == piece and board[i][j - 1] == piece and board[i][
        j - 2] == piece:
      return piece + " won"
  #check for 0_00
  if not j in [0, 5, 6]:
    if board[i][j + 1] == piece and board[i][j + 2] == piece and board[i][
        j - 1] == piece:
      return piece + " won"
  # check for top piece of a down-right diagonal
  if i < 3 and j < 4:
    if board[i + 1][j + 1] == piece and board[i + 2][j + 2] == piece and board[
        i + 3][j + 3] == piece:
      return piece + " won"
  # check for bottom piece of a down-right diagonal
  if i > 2 and j > 2:
    if board[i - 1][j - 1] == piece and board[i - 2][j - 2] == piece and board[
        i - 3][j - 3] == piece:
      return piece + " won"

  # check for top piece of down-left diagonal
  if i < 3 and j > 2:
    if board[i + 1][j - 1] == piece and board[i + 2][j - 2] == piece and board[
        i + 3][j - 3] == piece:
      return piece + " won"
  # check for bottom piece of down-left diagonal
  if i > 2 and j < 4:
    if board[i - 1][j + 1] == piece and board[i - 2][j + 2] == piece and board[
        i - 3][j + 3] == piece:
      return piece + " won"
  # check for 2nd top piece of down-right diagonal
  if i in [1, 2, 3] and j in [1, 2, 3, 4]:
    if board[i - 1][j - 1] == piece and board[i + 1][j + 1] == piece and board[
        i + 2][j + 2] == piece:
      return piece + " won"
  # check for 3rd piece of down-right diagonal
  if i in [2, 3, 4] and j in [2, 3, 4, 5]:
    if board[i - 1][j - 1] == piece and board[i - 2][j - 2] == piece and board[
        i + 1][j + 1] == piece:
      return piece + " won"
  # check for 2nd piece of down-left diagonal
  if i in [1, 2, 3] and j in [2, 3, 4, 5]:
    if board[i - 1][j + 1] == piece and board[i + 1][j - 1] == piece and board[
        i + 2][j - 2] == piece:
      return piece + " won"
  # check for 3rd piece in down-left diagonal
  if i in [2, 3, 4] and j in [1, 2, 3, 4]:
    if board[i - 1][j + 1] == piece and board[i + 1][j - 1] == piece and board[
        i - 2][j + 2] == piece:
      return piece + " won"


def place(name, Line, row):
  open_file = open(name, "r")
  board = []
  IDS = open_file.readline()
  piece = open_file.readline().strip("\n")
  for x in range(6):
    value = open_file.readline()
    board.append(value.strip("\n").split(","))
  open_file.close()
  Place = True
  while Place and Line != 6:
    if board[Line][row - 1] == ":white_large_square:":
      Line += 1
    else:
      Place = False
  Line -= 1
  board[Line][row - 1] = piece
  lastPlayed = str(Line) + "," + str(row - 1)
  Line1 = ",".join(board[0])
  Line2 = ",".join(board[1])
  Line3 = ",".join(board[2])
  Line4 = ",".join(board[3])
  Line5 = ",".join(board[4])
  Line6 = ",".join(board[5])
  Lines = [Line1, Line2, Line3, Line4, Line5, Line6]
  phrase = "\n".join(Lines)
  new_piece = ""
  if piece == ":green_circle:":
    new_piece = ":red_circle:\n"
  elif piece == ":red_circle:":
    new_piece = ":green_circle:\n"
  open_file = open(name, "w")
  open_file.write(IDS+new_piece + phrase)
  open_file.close()
  if board[0][row - 1] == piece:
    phrase = "Full row" + "|" + lastPlayed
    return phrase
  phrase = "unfull row" + "|" + lastPlayed
  return phrase

# in button pressing, read the new line
@bot.command(
  brief=" Begins your Connect 4 Game",
  description=
  " Displays the board and buttons, which will place your piece in the desired lane",
  Arguements="None")
async def Connect4(ctx):

  if not os.path.exists(ctx.author.name + "#"):
    open_file = open(ctx.author.name + "#", "w")
    open_file.write(
      ":green_circle:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:"
    )
    open_file.close()
    open_file = open(ctx.author.name + "#", "r")
  else:
    csv_file = ctx.author.name+'#'
    with open(csv_file) as file:
          reader = csv.reader(file)
          for row in reader:
              try:
                message_id = int(row[0])
                channel_id = int(row[1])
                message = await bot.get_channel(channel_id).fetch_message(message_id)
                await message.delete()
              except:
                pass
    open_file = open(ctx.author.name + "#", "r")
    IDS = open_file.readline()

  
  
  board = []
  piece = open_file.readline()
  for _ in range(6):
    value = open_file.readline()
    board.append(value.strip("\n").split(","))
  open_file.close()
  L1 = "".join(board[0])
  L2 = "".join(board[1])
  L3 = "".join(board[2])
  L4 = "".join(board[3])
  L5 = "".join(board[4])
  L6 = "".join(board[5])

  button1 = Button(label="",
                   emoji="1??????",
                   style=discord.ButtonStyle.gray,
                   row=0)
  button2 = Button(label="",
                   emoji="2??????",
                   style=discord.ButtonStyle.gray,
                   row=0)
  button3 = Button(label="",
                   emoji="3??????",
                   style=discord.ButtonStyle.gray,
                   row=0)
  button4 = Button(label="",
                   emoji="4??????",
                   style=discord.ButtonStyle.gray,
                   row=1)
  button5 = Button(label="",
                   emoji="5??????",
                   style=discord.ButtonStyle.gray,
                   row=1)
  button6 = Button(label="",
                   emoji="6??????",
                   style=discord.ButtonStyle.gray,
                   row=1)
  button7 = Button(label="",
                   emoji="7??????",
                   style=discord.ButtonStyle.gray,
                   row=1)
  button8 = Button(label="End Game",
                   style=discord.ButtonStyle.gray,
                   row=2)

  async def button1Clicked(interaction):
    returns = place(ctx.author.name + "#", 0, 1)
    items_returned = returns.split('|')
    x = items_returned[0]
    lastPlayed = items_returned[1]
    open_file = open(ctx.author.name + "#", "r")
    board = []
    IDS = open_file.readline()
    piece = open_file.readline()
    
    for _ in range(6):
      value = open_file.readline()
      board.append(value.strip("\n").split(","))
    open_file.close()
    L1 = "".join(board[0])
    L2 = "".join(board[1])
    L3 = "".join(board[2])
    L4 = "".join(board[3])
    L5 = "".join(board[4])
    L6 = "".join(board[5])
    message = piece + " turn\n" + L1 + "\n" + L2 + "\n" + L3 + "\n" + L4 + "\n" + L5 + "\n" + L6
    if x == "Full row":
      button1.disabled = True
    checkPiece = ""
    if piece.strip("\n") == ":green_circle:":
      checkPiece = ":red_circle:"
    if piece.strip("\n") == ":red_circle:":
      checkPiece = ":green_circle:"

    answer = checks(checkPiece, lastPlayed, ctx.author.name + "#")

    if answer == ":green_circle: won":
      message += "\n:green_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    elif answer == ":red_circle: won":
      message += "\n:red_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    else:
      fullBoard = await fullBoardCheck()
      if fullBoard == "Full":
        message += "\nNo-One Won"
        view1.clear_items()
        os.remove(str(ctx.author.name) + "#")
    await m.edit(content=message, view=view1)
    await interaction.response.defer()

  async def button2Clicked(interaction):
    returns = place(ctx.author.name + "#", 0, 2)
    items_returned = returns.split('|')
    x = items_returned[0]
    lastPlayed = items_returned[1]
    open_file = open(ctx.author.name + "#", "r")
    board = []
    IDS = open_file.readline()
    piece = open_file.readline()
    for _ in range(6):
      value = open_file.readline()
      board.append(value.strip("\n").split(","))
    open_file.close()
    L1 = "".join(board[0])
    L2 = "".join(board[1])
    L3 = "".join(board[2])
    L4 = "".join(board[3])
    L5 = "".join(board[4])
    L6 = "".join(board[5])
    message = piece + " turn\n" + L1 + "\n" + L2 + "\n" + L3 + "\n" + L4 + "\n" + L5 + "\n" + L6
    if x == "Full row":
      button2.disabled = True
    checkPiece = ""
    if piece.strip("\n") == ":green_circle:":
      checkPiece = ":red_circle:"
    if piece.strip("\n") == ":red_circle:":
      checkPiece = ":green_circle:"

    answer = checks(checkPiece, lastPlayed, ctx.author.name + "#")

    if answer == ":green_circle: won":
      message += "\n:green_circle: Won"
      view1.clear_items()
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    elif answer == ":red_circle: won":
      message += "\n:red_circle: Won"
      view1.clear_items()
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    else:
      fullBoard = await fullBoardCheck()
      if fullBoard == "Full":
        message += "\nNo-One Won"
        view1.clear_items()
        os.remove(str(ctx.author.name) + "#")
    await m.edit(content=message, view=view1)
    await interaction.response.defer()

  async def button3Clicked(interaction):
    returns = place(ctx.author.name + "#", 0, 3)
    items_returned = returns.split('|')
    x = items_returned[0]
    lastPlayed = items_returned[1]
    open_file = open(ctx.author.name + "#", "r")
    board = []
    IDS = open_file.readline()
    piece = open_file.readline()
    for _ in range(6):
      value = open_file.readline()
      board.append(value.strip("\n").split(","))
    open_file.close()
    L1 = "".join(board[0])
    L2 = "".join(board[1])
    L3 = "".join(board[2])
    L4 = "".join(board[3])
    L5 = "".join(board[4])
    L6 = "".join(board[5])
    message = piece + " turn\n" + L1 + "\n" + L2 + "\n" + L3 + "\n" + L4 + "\n" + L5 + "\n" + L6
    if x == "Full row":
      button3.disabled = True
    checkPiece = ""
    if piece.strip("\n") == ":green_circle:":
      checkPiece = ":red_circle:"
    if piece.strip("\n") == ":red_circle:":
      checkPiece = ":green_circle:"

    answer = checks(checkPiece, lastPlayed, ctx.author.name + "#")

    if answer == ":green_circle: won":
      message += "\n:green_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    elif answer == ":red_circle: won":
      message += "\n:red_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    else:
      fullBoard = await fullBoardCheck()
      if fullBoard == "Full":
        message += "\nNo-One Won"
        view1.clear_items()
        os.remove(str(ctx.author.name) + "#")
    await m.edit(content=message, view=view1)
    await interaction.response.defer()

  async def button4Clicked(interaction):
    returns = place(ctx.author.name + "#", 0, 4)
    items_returned = returns.split('|')
    x = items_returned[0]
    lastPlayed = items_returned[1]
    open_file = open(ctx.author.name + "#", "r")
    board = []
    IDS = open_file.readline()
    piece = open_file.readline()
    for _ in range(6):
      value = open_file.readline()
      board.append(value.strip("\n").split(","))
    open_file.close()
    L1 = "".join(board[0])
    L2 = "".join(board[1])
    L3 = "".join(board[2])
    L4 = "".join(board[3])
    L5 = "".join(board[4])
    L6 = "".join(board[5])
    message = piece + " turn\n" + L1 + "\n" + L2 + "\n" + L3 + "\n" + L4 + "\n" + L5 + "\n" + L6
    if x == "Full row":
      button4.disabled = True
    checkPiece = ""
    if piece.strip("\n") == ":green_circle:":
      checkPiece = ":red_circle:"
    if piece.strip("\n") == ":red_circle:":
      checkPiece = ":green_circle:"

    answer = checks(checkPiece, lastPlayed, ctx.author.name + "#")

    if answer == ":green_circle: won":
      message += "\n:green_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    elif answer == ":red_circle: won":
      message += "\n:red_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    else:
      fullBoard = await fullBoardCheck()
      if fullBoard == "Full":
        message += "\nNo-One Won"
        view1.clear_items()
        os.remove(str(ctx.author.name) + "#")
    await m.edit(content=message, view=view1)
    await interaction.response.defer()

  async def button5Clicked(interaction):
    returns = place(ctx.author.name + "#", 0, 5)
    items_returned = returns.split('|')
    x = items_returned[0]
    lastPlayed = items_returned[1]
    open_file = open(ctx.author.name + "#", "r")
    board = []
    IDS = open_file.readline()
    piece = open_file.readline()
    for _ in range(6):
      value = open_file.readline()
      board.append(value.strip("\n").split(","))
    open_file.close()
    L1 = "".join(board[0])
    L2 = "".join(board[1])
    L3 = "".join(board[2])
    L4 = "".join(board[3])
    L5 = "".join(board[4])
    L6 = "".join(board[5])
    message = piece + " turn\n" + L1 + "\n" + L2 + "\n" + L3 + "\n" + L4 + "\n" + L5 + "\n" + L6
    if x == "Full row":
      button5.disabled = True
    checkPiece = ""
    if piece.strip("\n") == ":green_circle:":
      checkPiece = ":red_circle:"
    if piece.strip("\n") == ":red_circle:":
      checkPiece = ":green_circle:"

    answer = checks(checkPiece, lastPlayed, ctx.author.name + "#")

    if answer == ":green_circle: won":
      message += "\n:green_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    elif answer == ":red_circle: won":
      message += "\n:red_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    else:
      fullBoard = await fullBoardCheck()
      if fullBoard == "Full":
        message += "\nNo-One Won"
        view1.clear_items()
        os.remove(str(ctx.author.name) + "#")
    await m.edit(content=message, view=view1)
    await interaction.response.defer()

  async def button6Clicked(interaction):
    returns = place(ctx.author.name + "#", 0, 6)
    items_returned = returns.split('|')
    x = items_returned[0]
    lastPlayed = items_returned[1]
    open_file = open(ctx.author.name + "#", "r")
    board = []
    IDS = open_file.readline()
    piece = open_file.readline()
    for _ in range(6):
      value = open_file.readline()
      board.append(value.strip("\n").split(","))
    open_file.close()
    L1 = "".join(board[0])
    L2 = "".join(board[1])
    L3 = "".join(board[2])
    L4 = "".join(board[3])
    L5 = "".join(board[4])
    L6 = "".join(board[5])
    message = piece + " turn\n" + L1 + "\n" + L2 + "\n" + L3 + "\n" + L4 + "\n" + L5 + "\n" + L6
    if x == "Full row":
      button6.disabled = True
    checkPiece = ""
    if piece.strip("\n") == ":green_circle:":
      checkPiece = ":red_circle:"
    if piece.strip("\n") == ":red_circle:":
      checkPiece = ":green_circle:"

    answer = checks(checkPiece, lastPlayed, ctx.author.name + "#")

    if answer == ":green_circle: won":
      message += "\n:green_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    elif answer == ":red_circle: won":
      message += "\n:red_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    else:
      fullBoard = await fullBoardCheck()
      if fullBoard == "Full":
        message += "\nNo-One Won"
        view1.clear_items()
        os.remove(str(ctx.author.name) + "#")
    await m.edit(content=message, view=view1)
    await interaction.response.defer()

  async def button7Clicked(interaction):
    returns = place(ctx.author.name + "#", 0, 7)
    items_returned = returns.split('|')
    x = items_returned[0]
    lastPlayed = items_returned[1]
    open_file = open(ctx.author.name + "#", "r")
    board = []
    IDS = open_file.readline()
    piece = open_file.readline()
    for _ in range(6):
      value = open_file.readline()
      board.append(value.strip("\n").split(","))
    open_file.close()
    L1 = "".join(board[0])
    L2 = "".join(board[1])
    L3 = "".join(board[2])
    L4 = "".join(board[3])
    L5 = "".join(board[4])
    L6 = "".join(board[5])
    message = piece + " turn\n" + L1 + "\n" + L2 + "\n" + L3 + "\n" + L4 + "\n" + L5 + "\n" + L6
    if x == "Full row":
      button7.disabled = True
    checkPiece = ""
    if piece.strip("\n") == ":green_circle:":
      checkPiece = ":red_circle:"
    if piece.strip("\n") == ":red_circle:":
      checkPiece = ":green_circle:"

    answer = checks(checkPiece, lastPlayed, ctx.author.name + "#")

    if answer == ":green_circle: won":
      message += "\n:green_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    elif answer == ":red_circle: won":
      message += "\n:red_circle: Won"
      view1.clear_items()
      os.remove(str(ctx.author.name) + "#")
    else:
      fullBoard = await fullBoardCheck()
      if fullBoard == "Full":
        message += "\nNo-One Won"
        view1.clear_items()
        os.remove(str(ctx.author.name) + "#")
    await m.edit(content=message, view=view1)
    await interaction.response.defer()

  async def button8Clicked(interaction):
    open_file = open(ctx.author.name + "#","r")
    board = []
    IDS = open_file.readline()
    piece = open_file.readline()
    for _ in range(6):
      value = open_file.readline()
      board.append(value.strip("\n").split(","))
    open_file.close()
    L1 = "".join(board[0])
    L2 = "".join(board[1])
    L3 = "".join(board[2])
    L4 = "".join(board[3])
    L5 = "".join(board[4])
    L6 = "".join(board[5])
    os.remove(ctx.author.name + "#")
    view1.clear_items()
    message = L1 + "\n" + L2 + "\n" + L3 + "\n" + L4 + "\n" + L5 + "\n" + L6 + "\n" + ctx.author.name + "'s Game Ended\nUse !loganConnect4 to begin a new game"
    await m.edit(content=message,view=view1)
    await  interaction.response.defer()

  button1.callback = button1Clicked
  button2.callback = button2Clicked
  button3.callback = button3Clicked
  button4.callback = button4Clicked
  button5.callback = button5Clicked
  button6.callback = button6Clicked
  button7.callback = button7Clicked
  button8.callback = button8Clicked
  
  async def fullBoardCheck():
    if button1.disabled == True and button2.disabled == True and button3.disabled == True and button4.disabled == True and button5.disabled == True and button6.disabled == True and button7.disabled == True:
      return "Full"

  open_file = open(ctx.author.name + "#", "r")
  first = open_file.readline()
  message = ""
  if not first == ":green_circle:\n":
    IDS = open_file.readline()
  board = []
  for _ in range(6):
    value = open_file.readline()
    board.append(value.strip("\n").split(","))
  open_file.close()
  buttons = [button1,button2,button3,button4,button5,button6,button7]
  for items in range(7):
    if board[0][items] == ":green_circle:" or board[0][items] == ":red_circle:":
      buttons[items].disabled = True
      
  

  
  
  view1 = View()
  view1.add_item(button1)
  view1.add_item(button2)
  view1.add_item(button3)
  view1.add_item(button4)
  view1.add_item(button5)
  view1.add_item(button6)
  view1.add_item(button7)
  view1.add_item(button8)

  m = await ctx.send(piece + " turn\n" + L1 + "\n" + L2 + "\n" + L3 + "\n" +
                     L4 + "\n" + L5 + "\n" + L6,
                     view=view1)

  open_file = open(ctx.author.name+"#","r")
  first = open_file.readline()
  message = ""
  if first == ":green_circle:\n":
    message = ":green_circle:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:\n:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:,:white_large_square:"
  else:
    piece = open_file.readline()
    message += piece
    for _ in range(6):
      value = open_file.readline()
      message+= value
    
  open_file = open(ctx.author.name+"#","w")
  open_file.write(str(m.id)+","+str(m.channel.id)+"\n"+message)
  open_file.close()
  


  

  




#============================================================

my_secret = os.environ['TOKEN']
bot.run(my_secret)
