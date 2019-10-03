from selenium import webdriver
from bs4 import BeautifulSoup
import re

textFile = "C:\\Users\\x97275\\Desktop\\myPythonScripts\\Accountability Notes\\text_0.txt"

test ="C:\\Users\\x97275\\Desktop\\myPythonScripts\\Accountability Notes\\test.txt" 

def readInLines(pathToText):
    text = open(pathToText,"r")
    nameLtrTups = []
    for line in text:
        info = line.split(".")
        name = info[0].upper().strip().replace("\"", "")
        letter = info[1].upper().strip().replace("\"", "")
        nameLtrTups.append([name, letter])
    text.close()
    #print(nameLtrTups)
    return nameLtrTups
#readInLines(textFile)

a = [['WU', 'P'], ['SUAREZ', 'O'], ['GORDON, G', 'H']]

def clickButton(nameLtrList):
    a = {"D":0,
         "L":1,
         "F":2,
         "G":3,
         "S":4,
         "T":5,
         "H":6,
         "C":7,
         "CL":8,
         "SP":9,
         "P":10,
         "TB":11,
         "OP":12,
         "R":13,
         "O":14
         }

    driver = webdriver.Chrome()
    driver.get('C:\\Users\\x97275\\Desktop\\myPythonScripts\\Accountability Notes\\thingy.html')
    # for each person, figure out the @name= thing
    for nameLtrPair in nameLtrList:
        nameString = getName(nameLtrPair[0],nameLtrPair[1])
        # click the correct radio button
        python_buttons = driver.find_elements_by_xpath("//*[@type='radio' and @name=" + nameString + "]")
        index = a[nameLtrPair[1]]
        python_buttons[index].click()


def getName(name, ltr):
    htmlfile = 'C:\\Users\\x97275\\Desktop\\myPythonScripts\\Accountability Notes\\thingy.html'
    htmlcode = open(htmlfile, 'r')
    soup = BeautifulSoup(htmlcode, 'html.parser')
    cleanedSoup = soup.prettify()
    extraCleanSoup = cleanedSoup[700:]
    aList = (re.split(r'<td>',extraCleanSoup))
    finalString = ""
    i = 0
    for string in aList:
        if string.find(name) != -1:
            finalString += string
            buttonsList = []
            for buttonString in aList[i:i+17]:
                if buttonString.find("value=\"" + ltr + "\"") != -1:
                    finalString += buttonString
        i += 1
    newList = finalString.split(" ")
    uncleanString = newList[23]
    cleanString = uncleanString.split("=")[1].replace("\"", "'")
    #print(cleanString)
    return cleanString


# In this format, clickButton() calls getName.
clickButton(a)


    
