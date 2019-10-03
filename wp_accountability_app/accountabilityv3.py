from selenium import webdriver
from bs4 import BeautifulSoup
import time
import imaplib
import email
import os
import time
import re


def saveGmailAttachments():
    
    svdir = 'C:\\Users\\x97275\\Desktop\\myPythonScripts\\Accountability Notes'

    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
    mail.login("<email_addr>@gmail.com", "<password>") 

    print("[+] "+"Authenticated\n")

    mail.select("Inbox")


    typ, msgs = mail.search(None, 'FROM ##########') 
    msgs = msgs[0].split()


    for emailid in msgs:
        print("Processing an email with attachments... \n")
        resp, data = mail.fetch(emailid, "(RFC822)")
        email_body = data[0][1]
        m = email.message_from_bytes(email_body)

        if m.get_content_maintype() != 'multipart':
            continue

        for part in m.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            print("[+] "+'A ' + part.get_content_type() + ' file was found.\n') # Gives me filetype. "text/plain" and "image/jpeg" are possible options
            filename = part.get_filename()
            if filename and part.get_content_type() == "text/plain":
                sv_path = os.path.join(svdir, filename)
                print(sv_path + "\n")
                fp = open(sv_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
                return sv_path

def clearInbox():

    mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
    mail.login("<email_addr>@gmail.com", "<password>") 

    print("[+] "+"Clearing Inbox\n")

    mail.select("Inbox")


    typ, msgs = mail.search(None, 'FROM ##########') 
    for num in msgs[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')
        mail.expunge()

def seperateNameAndLetter(pathToText):
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
    
    # for each person, figure out the @name= thing. Need to do this here, only want 1 instance of selenium webdriver
    for nameLtrPair in nameLtrList:
        nameString = getName(nameLtrPair[0],nameLtrPair[1])
        # click the correct radio button
        python_buttons = driver.find_elements_by_xpath("//*[@type='radio' and @name=" + nameString + "]")
        print(a[nameLtrPair[1]])
        index = a[nameLtrPair[1]]
        python_buttons[index].click()



#================================================================================================
# Main Function
#================================================================================================


def main():

    
    # Login to Gmail and iterate over every email, and pull down all text files from my phone number.
    txtFilePath = saveGmailAttachments()
    
    # Prevent issues with further texts by deleting the file
    clearInbox()
    
    # Iterate over every line of the text file, seperate out the name and letter, sanitize the inputs. Give back a list of lists.
    nameLtrList = seperateNameAndLetter(txtFilePath)

    
    # Find the tag with the name variable in it. Maybe this is something I call from within clickButton? give the names and letter list to click button, to avoid multiple instances of selenium driver.
    clickButton(nameLtrList)


if __name__ == '__main__':
    main()

#================================================================================================
# Current Challenges
#================================================================================================        

# this script right now will pull everything that I ever sent from my phone number.
# I want to only take the ones that I sent within the past hour. Maybe just delete the message after I get the attachment?
# I will also need to handle this when it comes to writing the CIS script.
# My CIS script is for chrome and I need it for IE.
# I need a way to deal with admin not liking my extensions. (run clicker, you'll see what I mean.)
# need functionality for them making comments after lines designated with "O"
# Write this as a function and then call main()

#Do the clicking of the buttons and the functionality/for loops that are in main in the clickButton function.

#================================================================================================
# Solved Challenges
#================================================================================================

# I will also need to configure a gmail account for the Buff accountability to use. DONE.
# I also just want to take txt files. Not anything else I send. GOT IT.
# With filename collision (default name is text_0.txt), it will overwrite the previous file.














