import pyautogui as pt
from time import sleep
import pyperclip
import random
import re
from selenium.webdriver.common.by import By  # Import the By class

from selenium import webdriver



from selenium import webdriver

# Specify the path to the existing user data directory of Google Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:\\Users\\Toshiba\\AppData\\Local\\Google\\Chrome\\User Data")

# Initialize the Chrome WebDriver with the specified user data directory
driver = webdriver.Chrome(options=chrome_options)


sleep(3)



#gets message
def get_message():
    global x,y
   
    position1 = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x + 70, y - 40, duration = .5)
    pt.tripleClick()
    pt.hotkey('ctrl', 'c')
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)

    return whatsapp_message

#posts
def post_response(message,element):
    global x, y
   
    position1 = pt.locateOnScreen("smiley.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    if "cancel" in (message).lower():
     driver.get(f"https://prixsmm.com/api/v2?key=userApiKey&action=cancel&orders={element}")
     
     
     pt.typewrite("Order Canceled Sucessfully", interval=.01)
    
     pt.typewrite("\n", interval=.01)
    elif "refil" in(message).lower():
        driver.get(f"https://prixsmm.com/api/v2?key=userApiKey&action=refil&orders={element}")
        
        sleep(5)
        pt.typewrite("Order Refilled  Sucessfully", interval=.01)
    
        pt.typewrite("\n", interval=.01)

#process response
def process_response(message):
    pattern = r"(\d+)-/ (cancel|refil)"

    match = re.search(pattern, message)
    
    # Check if a match is found
    if match:
        order_number = match.group(1)
        status = match.group(2)
        print(order_number)
        print(status)
        

        return order_number, status
    else:
       
        return None

#new messages check
def check_for_new_messages():
    while True:
        try:
            position = pt.locateOnScreen("circle.png", confidence=0.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                processed_message = process_response(get_message())
                print(processed_message)
                if processed_message:
                    order_number, status = processed_message
                    print(order_number)
                    print(status)
                    sleep(5)
                    driver.get(f"https://usdsmm.com/admin/orders?query={order_number}&search_type=1")
                    sleep(2)
                    # Update the correct XPath
                    xpath = '//*[@id="page-wrapper"]/div[2]/div/div/table/tbody/tr[2]/td/div'
                    element = driver.find_element(By.XPATH, xpath)
                    element_value = element.text
                    print(element_value)
                    sleep(2)
                    post_response(status, element_value)
                    
                    sleep(10)
                else:
                    print("Message processing failed.")
            else:
                print("No messages")
                sleep(10)

        except Exception as e:
            print(f"No Message")



def check_whatsapp_open():
    input("Make sure WhatsApp is open. Press Enter when ready...")
    sleep(3)


check_whatsapp_open()
sleep(5)
check_for_new_messages()
