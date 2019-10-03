
# element2 = driver.find_element_by_xpath("//div[@title='div2']") this defines a parent tag
# element2.find_element_by_xpath(".//p[@class='test']").text  this defines the desired child tag.

from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time

def getTagOfName(name): # last name.
    
    # open the CIS page. 
    htmlFile = "C:\\Users\\x97275\\Desktop\\thingy.html"
    html = open(htmlFile, "r")
    
    soup = BeautifulSoup(html, 'html.parser')

    lastName = name

    for elem in soup(text=re.compile(lastName)): # successfully gets me the parent tag containing the last name. Now I need to get the to right radio button and click it.
        print(str(elem.parent))
        # close the CIS page.
        html.close()
        return elem.parent


    
    

def clickButton(parentTag, ltr): #need to edit this to also take a name so that we can click the button just for that one person.


    driver = webdriver.Chrome() #chrome_options=options
    driver.get('C:\\Users\\x97275\\Desktop\\thingy.html') # http://codepad.org
     
    # click radio button
    #ltr = "'O'"
    name = parentTag
    button
    python_buttons = driver.find_elements_by_xpath("//"+ str(name) +"[@type='radio' and @value="+ "'" + ltr + "'" +"]") # ("//*[@type='radio' and @value="+ "'" + ltr + "'" +"]")
    for pyButton in python_buttons: #right now this makes it click every single button in that column. Needs to only pick one.
        print(str(pyButton.element)) #only click ones where the name resolves to the right number. (allen is 1, and so on.)
       # pyButton.click()

def main():
    parentTag = getTagOfName("AHN")
    
    clickButton(parentTag, 'O')

if __name__ == '__main__':
    main()
























