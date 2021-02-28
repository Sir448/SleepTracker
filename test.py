# import json
# import datetime
# from datetime import tzinfo,timedelta
# import pytz
import pandas as pd
# import numpy as np
# from math import ceil, floor
# import matplotlib.pyplot as plt
# import sys

# print(sys.argv)

sleep = pd.read_excel("Sleep.xlsx", index_col=0)
print(sleep)
sleep = sleep.iloc[0:0]
print(sleep)
# data = {"lastAccess": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

interval = 10 #interval length in minutes

# times = np.zeros(int(1440/interval))

# times = np.zeros(24)
# test = np.array([0,8,7,7,9,5,10,6])
# test2 = np.array([17,17,19,14,15,20,21,15])
# for i,j in zip(test,test2):
#     times[i:j] += 1
# # plt.hist(test4,weights = test3,lalig)
# # x = range(1,25)


# labels = []
# for i in range(24):
#     labels.append(str(i).zfill(2)+":00")
# labels = np.array(labels)


# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# fig.set_xticks(np.arange(len(times)))
# ax.bar(np.arange(len(times)),times,width=1)
# plt.bar(np.arange(len(times)),times,width = 1, color = '#8cddff')
# ax.plot(times, color='#00aeff')
# plt.xlabel("Time")
# plt.ylabel("Number of Days")
# plt.title("Time of Sleep")



# plt.bar(np.arange(len(times)),times,width = 1, color = '#8cddff')
# plt.plot(times, color='#00aeff')
# plt.xlabel("Time")
# plt.ylabel("Number of Days")
# plt.title("Time of Sleep")
# plt.xticks(range(len(labels)),labels,rotation = -70)
# plt.show()


# test3 = (test+test2)/2
# print(test)
# print(test2)
# print(test3)
# print(tens)
# tens[:5]+=1
# print(tens)
# print(zero_data)


"""
# with open("data.json", "w") as f:
#     json.dump(data,f,indent=4)
# with open("data.json", "r") as f:
#     data = json.load(f)

# print(data["lastAccess"])
# print(type(data["lastAccess"]))
# print(datetime.datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime.datetime.now() < datetime.datetime.strptime("2020-04-01 02:34:12","%Y-%m-%d %H:%M:%S"))
# sleep = pd.read_excel("Sleep.xlsx", index_col=0)
# # # # # # print(sleep[2][1])



# for i in range(len(sleep.index)):
#     if sleep[2][i] == 0 and sleep[2][i+1] == 1:
#         start = ceil((datetime.datetime.strptime(sleep[1][i],"%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(sleep[1][i][:-8]+"00:00:00","%Y-%m-%d %H:%M:%S")).total_seconds()/(interval*60))
#         end = floor((datetime.datetime.strptime(sleep[1][i+1],"%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(sleep[1][i+1][:-8]+"00:00:00","%Y-%m-%d %H:%M:%S")).total_seconds()/(interval*60))
#         if datetime.datetime.strptime(sleep[1][i+1],"%Y-%m-%d %H:%M:%S") <= datetime.datetime.strptime(sleep[1][i][:-8]+"23:59:59","%Y-%m-%d %H:%M:%S"):
#             times[start:end] += 1
#         else:
#             times[start:] += 1
#             times[:end] += 1
"""

# for i in range(len(sleep.index)):
#     if sleep[2][i] == 0 and sleep[2][i+1] == 1:
#         start = ceil((datetime.datetime.strptime(sleep[1][i],"%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(sleep[1][i][:-8]+"00:00:00","%Y-%m-%d %H:%M:%S")).total_seconds()/(interval*60))
#         end = floor((datetime.datetime.strptime(sleep[1][i+1],"%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(sleep[1][i+1][:-8]+"00:00:00","%Y-%m-%d %H:%M:%S")).total_seconds()/(interval*60))
#         if datetime.datetime.strptime(sleep[1][i+1],"%Y-%m-%d %H:%M:%S") <= datetime.datetime.strptime(sleep[1][i][:-8]+"23:59:59","%Y-%m-%d %H:%M:%S"):
#             times[start:end] += 1
#         else:
#             times[start:] += 1
#             times[:end] += 1

# print(times)




# get time at middle of sleep
# get duration of sleep

# stime = "2021-02-06 00:05:23"
# stime = "2021-02-06 00:00:00"
# etime = "2021-02-06 00:45:23"
# start = ceil((datetime.datetime.strptime(stime,"%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(stime[:-8]+"00:00:00","%Y-%m-%d %H:%M:%S")).total_seconds()/600)
# end = floor((datetime.datetime.strptime(etime,"%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(etime[:-8]+"00:00:00","%Y-%m-%d %H:%M:%S")).total_seconds()/600)
# times[start:end] +=1
# print(times)

#         # ceil(((sleep[1][i].strptime("%Y-%m-%d %H:%M:%S")-datetime.datetime(1970,1,1)).total_seconds())/600)*600
#         sleep[1][i].strptime("%Y-%m-%d %H:%M:%S")
# message = "s 2:34am"
# day = "2020-04-01 12:34:12"
# day2 = "2020-04-02 23:34:12"
# timeInput = message[message.index(":")-2:message.index(":")+3]
# if ord(message[message.index(":")-2]) < 48 or ord(message[message.index(":")-2]) > 57:
#     timeInput = "0"+timeInput[1:]
# if message[message.index("m")-1] == "p" and timeInput[:2] != "12":
#     timeInput = str(int(timeInput[:2])+12) + timeInput[2:]
# elif message[message.index("m")-1] == "a" and timeInput[:2] == "12":
#     timeInput = "00" + timeInput[2:]
# timeInput += ":00"
# # print(timeInput)
# # print(type(datetime.datetime.strptime(day,"%Y-%m-%d %H:%M:%S")))
# print(day[:-8]+timeInput)
# print(type(datetime.datetime.strptime(day[:-8]+timeInput,"%Y-%m-%d %H:%M:%S") if datetime.datetime.strptime(day,"%Y-%m-%d %H:%M:%S")>datetime.datetime.strptime(day[:-8]+timeInput,"%Y-%m-%d %H:%M:%S") else datetime.datetime.strptime(day[:-8]+timeInput,"%Y-%m-%d %H:%M:%S")-timedelta(days=1)))
# print(ord("9"))
# 48-57


# print(datetime.datetime.strptime(day,"%Y-%m-%d %H:%M:%S")-timedelta(hours=5))
# print(datetime.datetime.strptime(day[:-8]+"00:00:00","%Y-%m-%d %H:%M:%S"))
# print(datetime.datetime.strptime("2020-04-01 02:34:12","%Y-%m-%d %H:%M:%S"))


# print((datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds())

# print(len(sleep.index))