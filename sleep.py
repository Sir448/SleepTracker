import discord
import asyncio
import pandas as pd
import json
import datetime
from datetime import timedelta
import pytz
import sys

with open('data.json', 'r') as f:
    data = json.load(f)

logs = []

client = discord.Client()

new = "n" in sys.argv

@client.event
async def on_ready():
    channel = client.get_channel(807907451919663104)
    if "lastAccess" in data.keys() and not new:
    # Records new messages since last run
        print("test")
        async for message in channel.history(limit = None, after = datetime.datetime.strptime(data["lastAccess"],"%Y-%m-%d %H:%M:%S")):
            event = 'Sleep'
            eventId = 0
            if message.content.lower()[0]=='s':
                event = 'Sleep'
                eventId = 0
            elif message.content.lower()[0]=='w':
                event = "Woke Up"
                eventId = 1
            elif message.content.lower()[0]=='c':
                event = "Couldn't Sleep"
                eventId = 2
            
            if message.content.find(":") == -1:
                logs.append({"type":eventId,"event":event,"time":(message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")})
            else:
                timeInput = message.content[message.content.index(":")-2:message.content.index(":")+3]
                if ord(message.content[message.content.index(":")-2]) < 48 or ord(message.content[message.content.index(":")-2]) > 57:
                    timeInput = "0"+timeInput[1:]
                if message.content[message.content.index("m")-1] == "p" and timeInput[:2] != "12":
                    timeInput = str(int(timeInput[:2])+12) + timeInput[2:]
                elif message.content[message.content.index("m")-1] == "a" and timeInput[:2] == "12":
                    timeInput = "00" + timeInput[2:]
                timeInput += ":00"

                # I'm a sucker for ternary operators, even if they look super ugly and impossible to read
                # Pretty much, if the time in the message hasn't passed yet today, then input that time yesterday
                trueTime = datetime.datetime.strptime((message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")[:-8]+timeInput,"%Y-%m-%d %H:%M:%S") if datetime.datetime.strptime((message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")>datetime.datetime.strptime((message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")[:-8]+timeInput,"%Y-%m-%d %H:%M:%S") else datetime.datetime.strptime((message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")[:-8]+timeInput,"%Y-%m-%d %H:%M:%S")-timedelta(days=1)
                logs.append({"type":eventId,"event":event,"time":trueTime.strftime("%Y-%m-%d %H:%M:%S")})
    else:
        # Records all messages since the beginning
        async for message in channel.history(limit = None):
            event = 'Sleep'
            eventId = 0
            if message.content.lower()[0]=='s':
                event = 'Sleep'
                eventId = 0
            elif message.content.lower()[0]=='w':
                event = "Woke Up"
                eventId = 1
            elif message.content.lower()[0]=='c':
                event = "Couldn't Sleep"
                eventId = 2

            if message.content.find(":") == -1:
                logs.insert(0,{"type":eventId,"event":event,"time":(message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")})
            else:
                timeInput = message.content[message.content.index(":")-2:message.content.index(":")+3]
                if ord(message.content[message.content.index(":")-2]) < 48 or ord(message.content[message.content.index(":")-2]) > 57:
                    timeInput = "0"+timeInput[1:]
                if message.content[message.content.index("m")-1] == "p" and timeInput[:2] != "12":
                    timeInput = str(int(timeInput[:2])+12) + timeInput[2:]
                elif message.content[message.content.index("m")-1] == "a" and timeInput[:2] == "12":
                    timeInput = "00" + timeInput[2:]
                timeInput += ":00"

                # I'm a sucker for ternary operators, even if they look super ugly and impossible to read
                # Pretty much, if the time in the message hasn't passed yet today, then input that time yesterday
                trueTime = datetime.datetime.strptime((message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")[:-8]+timeInput,"%Y-%m-%d %H:%M:%S") if datetime.datetime.strptime((message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")>datetime.datetime.strptime((message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")[:-8]+timeInput,"%Y-%m-%d %H:%M:%S") else datetime.datetime.strptime((message.created_at-timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")[:-8]+timeInput,"%Y-%m-%d %H:%M:%S")-timedelta(days=1)
                logs.insert(0,{"type":eventId,"event":event,"time":trueTime.strftime("%Y-%m-%d %H:%M:%S")})

    await client.close()

client.run(data["token"])

data["lastAccess"] = datetime.datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")

with open('data.json', 'w') as f:
    json.dump(data,f,indent = 4)


sleep = pd.read_excel("Sleep.xlsx", index_col=0)
if new:
    sleep = sleep.iloc[0:0]
for event in logs:
    row = pd.Series([event["event"],event["time"],int(event["type"])])
    sleep = sleep.append(row, ignore_index=True)
sleep.to_excel("Sleep.xlsx")
print(sleep)