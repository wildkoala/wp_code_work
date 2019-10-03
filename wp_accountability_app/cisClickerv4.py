
# element2 = driver.find_element_by_xpath("//div[@title='div2']") this defines a parent tag
# element2.find_element_by_xpath(".//p[@class='test']").text  this defines the desired child tag.


from selenium import webdriver
import time

# read the text file, returns a list of lists, where every list within is a person and their letter.
def readTxtFile():
    namesList = []
    file = open('C:\\Users\\x97275\\Desktop\\myPythonScripts\\Accountability Notes\\text_0.txt')
    fileLines = file.readlines()
    for line in fileLines:
        words = line.strip()
        cleanWords = words.split(" ")
        namesList.append(cleanWords) #this gets me the name at index 0 and then the letter that they need clicked in CIS at index 1.
    #print(str(namesList))
    return namesList


def clickButton(ltr): #need to edit this to also take a name so that we can click the button just for that one person.


    driver = webdriver.Chrome() #chrome_options=options
    driver.get('C:\\Users\\x97275\\Desktop\\thingy.html') # http://codepad.org
     
    # click radio button
    #ltr = "'O'"
    python_buttons = driver.find_elements_by_xpath("//*[@type='radio' and @value="+ "'" + ltr + "'" +"]")
    for pyButton in python_buttons: #right now this makes it click every single button in that column. Needs to only pick one.
        pyButton.click()


def main():

    # get all the people who's status will be updated in CIS.
    people = readTxtFile()
'''
    # for every person in the "people" list, get their
    for person in people:
        name = person[0]
        ltr = person[1]
        
        clickButton(name, ltr) # click on the radio button identified by a name and letter.
'''

if __name__ == '__main__':
    main()
