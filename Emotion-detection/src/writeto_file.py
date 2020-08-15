import csv
import numpy as np

#  {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
emoteCounter = [0, 0, 0, 0, 0, 0, 0]
emoteLTG = []
emotion_data = ""
emoteNames = ["Angry", "Disgusted", "Fearful", "Happy", "Neutral", "Sad", "Surprised"]


def writeto_file(emotionData):
    dataResult = ""+emotionData
    dataResult = dataResult
    get_counts(emotionData)
    data = []
    data = emotion_data.split(';')
    emoteCounts = ""
    i = 0
    while i<7:
        emoteCounts = ("\n"+str(emoteNames[i]) + ":   Number of occurrences: " + str(emoteCounter[i])+"\n")
        i=i+1
    text_file = open("emotiondata.txt", "w")
    n = text_file.write(dataResult+emoteCounts)
    text_file.close()


def get_counts(emotionData):
    emotion_data = emotionData
    data = []
    data = emotion_data.split(';')
    for i in data:
        currEmote = i
        switch_case(currEmote)
        print("emote Added")


def get_median():
    lowestVal = ""
    counterLen = len(emoteCounter)-1
    currIndex = j
    i = 0
    j = i+1
    lowestVal = i
    while i < counterLen:
        j = i+1
        while i < counterLen:
            lowestVal = emoteCounter[i]
            if emoteCounter[j] > lowestVal:
                j+1
            else:
                lowestVal = emoteCounter[j]
                j = counterLen
            i+1
        emoteLTG.append(switch_case_rev(j))
        i+1
    print(emoteLTG)


def switch_case(argument):
    switcher = {
        "Angry": emoteCounter[0]+1,
        "Disgusted": emoteCounter[1]+1,
        "Fearful": emoteCounter[2]+1,
        "Happy": emoteCounter[3]+1,
        "Neutral": emoteCounter[4]+1,
        "Sad": emoteCounter[5]+1,
        "Surprised": emoteCounter[6]+1,
    }
def switch_case_rev(argument):
    switcher = {
        0: "Angry",
        1: "Disgusted",
        2: "Fearful",
        3: "Happy",
        4: "Neutral",
        5: "Sad",
        6: "Surprised",
    }
    return switcher