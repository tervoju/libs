from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# XPath selectors
NEW_CHAT_BTN = '//div[@class=\'sbcXq\']//div[2]//div[1]//span[1]'
INPUT_TXT_BOX = '//div[@class=\'_1KDYa _14Mgc copyable-area\']//div//input[@class=\'_2zCfw copyable-text selectable-text\']'
ONLINE_STATUS_LABEL = '//span[@class=\'_315-i _F7Vk\']'

# Replace below with the list of targets to be tracked
TARGETS = {'"Person"': '+35 40 555555', '"Person too"': '+35 40 555555'}

# Replace below path with the absolute path
browser = webdriver.Chrome(r'/usr/lib/chromium-browser/chromedriver')

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

while True:
    # Clear screen
    os.system('clear')

    # For each target
    for target in TARGETS:
        tryAgain = True

        # Wait until new chat button is visible
        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

        while (tryAgain):
            try:
                # Click on new chat button
                new_chat_title.click()

                # Wait untill input text box is visible
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))

                time.sleep(0.5)

                # Write phone number
                input_box.send_keys(TARGETS[target])

                time.sleep(1)

                # Press enter to confirm the phone number
                input_box.send_keys(Keys.ENTER)

                time.sleep(5)
                tryAgain = False

                try:
                    try:
                        browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
                        print(target + ' is online')
                    except:
                        print(target + ' is offline')
                    time.sleep(1)
                except:
                    print('Exception 1')
                    time.sleep(10)
            except:
                print('Exception 2')
                time.sleep(4)