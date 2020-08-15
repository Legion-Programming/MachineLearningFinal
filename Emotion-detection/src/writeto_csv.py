import csv


def writeto_csv(emotionData):
    with open("EmotionData.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(emotionData)