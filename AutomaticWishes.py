# Run the below command on the terminal to install selenium
# Python -m pip install -U Selenium  


from selenium import webdriver
import getpass
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')

driver.get('https://en-gb.facebook.com/')  # To open the page in English(hindi opens up by default)

usernameBox = driver.find_element_by_id('email')
passwordBox = driver.find_element_by_id('pass')

# We need to take id and password(atleast) so that it is not visible to others. So we will use the getpass module getpass function
my_id = getpass.getpass()
my_password = getpass.getpass()

usernameBox.send_keys(my_id)
passwordBox.send_keys(my_password)

loginButton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

loginButton.click()

eventsBtn = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a/div[1]/div[2]/div/div/div/div/span/span')

eventsBtn.click()

birthdays = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[3]/a')

birthdays.click()

todaysBirthdays = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div')

all_friends = todaysBirthdays.find_elements_by_tag_name('form')   # we have used find_elements so that we can get all forms available i.e. for each friend

for my_f in list(all_friends):
    messageBox = my_f.find_element_by_class_name('_1mf')
    messageBox.send_keys("Happy Birthday..!!")
    messageBox.send_keys(Keys.RETURN)
    time.sleep(3)

driver.quit()