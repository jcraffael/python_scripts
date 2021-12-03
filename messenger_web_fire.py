from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time


profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(executable_path=r"/home/cjiang/Downloads/geckodriver", firefox_profile=profile)

#opt = Options()
#opt.add_argument(r'user-data-dir=$(pwd)/messenger_profile')
msnger_url = r'https://www.facebook.com/messages/t/100046711267726'
#System.setProperty("webdriver.gecko.driver",Path_of_Firefox_Driver"); // Setting system properties of FirefoxDriver
#WebDriver driver = new FirefoxDriver(); //Creating an object of FirefoxDriver
# opts = Options()
# opts.log.level = "trace"
# driver = Firefox(options=opts)
#driver = webdriver.Firefox() #r'/home/cjiang/Downloads/geckodriver'

driver.get(msnger_url)

# Accept cookies #
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="1"][data-cookiebanner="accept_button"]'))).click()
time.sleep(2)
#user = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[id="email"][class="inputtext"]')))
user = driver.find_element_by_css_selector('input[data-testid="royal_email"]')
password = driver.find_element_by_css_selector('input[data-testid="royal_pass"]')

user.send_keys("oppotest02.it@gmail.com")
password.send_keys("oppotest")
time.sleep(1)
driver.find_element_by_css_selector('input[data-testid="royal_login_button"]').click()

target = 'Iphonexr Apple' #Contact name
#WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.LINK_TEXT, target))).click()



dic_time_str = {0:'1. ni 7',
1.5:'2. 4', 5:'3', 10:'3. 1234567890 13', 2:'4. $$$$$$$$$$$$$$$$$$$$$$$$$$ 29', 1:'5. abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz 85'
, 4:'6. ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ 127',
7:'7. ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ 168',
8:'8.123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890 336',
9:'9. 8. ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ 1689.123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890 336'
, 10:'1. ni 7 2. 4 3. 1234567890 13 4.$$$$$$$$$$$$$$$$$$$$$$$$$$ 29 5. abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz 85 6. ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ 1277.    158. ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ 1689.123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890 33610. 8. ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ 1689.123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890 336'
}

count = 100
chat_box_css = 'div[aria-describedby]'
#chat_box_css = 'div[aria-label="Messenger"]'
action = ActionChains(driver)
#time.sleep(10)
try:
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Message"][role="textbox"]')))
except TimeoutException:
    driver.refresh()
    time.sleep(5)


for i in range(count):
    if i % 4 == 0:
        j = i // 4
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-hidden="false"][aria-label="Choose a GIF"][role="button"][tabindex="0"]'))).click()
        time.sleep(2)
        search_bar = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[dir="ltr"][aria-label="GIF search"]')))
        search_bar.send_keys(Keys.TAB * (j + 1))
        time.sleep(1)
        GIF = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'img[height][width="274"][alt][referrerpolicy][src]')))
        GIFs = driver.find_elements_by_css_selector('img[width="274"]')
        while j >= 0:
            try:
                print("GIF: ", j)
                action.move_to_element(GIFs[j]).click(GIFs[j]).perform()
                break
            except IndexError:
                print("Exception in line 69 with j", j)
                j = j - 5
            except MoveTargetOutOfBoundsException:
                print("Exception in line 88 with j", j)
                search_bar.click()
                search_bar.send_keys(Keys.TAB * (j + 1))

    elif i % 4 == 1:
        j = i // 4

        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-hidden="false"][aria-label="Choose a sticker"][role="button"][tabindex="0"]'))).click()
        time.sleep(2)
        try:
            sticker_icon = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[class][type="submit"][value="1"][style]')))
        except TimeoutException:
            continue

        
        action.move_to_element(sticker_icon).click(sticker_icon).perform()
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[class="_5r8i"][role="img"]')))
        time.sleep(1)
        stickers = driver.find_elements_by_css_selector('div[class="_5r8i"][role="img"]')
        while j >= 0:
            try:
                #action.move_to_element(stickers[j]).click(stickers[j]).perform()
                stickers[j].click()
                break
            except IndexError:
                print("Exception in line 98")
                j = i // 10
            except ElementClickInterceptedException:
                print("Exception in line 117")
                j = j - 1

    elif i % 4 == 2:       
        j = i // 4
        
        while j>=0:
            try:
                time.sleep(list(dic_time_str.keys())[j])
                chatbox = driver.find_element_by_css_selector(chat_box_css)
                chatbox.send_keys(list(dic_time_str.values())[j]+ Keys.ENTER)
                break
            except IndexError:
                print("Exception in line 110:", j)
                j = j - 10
    else:
        j = i // 4
        if j > 10:
            j = j - 10
        time.sleep(2)
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Choose an emoji"][role="button"]'))).click()
        WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Smileys & people"]')))
        time.sleep(3)
        emojis = driver.find_elements_by_css_selector('img[height="30"]')
        while j>=0:
            try:
                action.move_to_element(emojis[j]).click(emojis[j]).perform()
                break
            except IndexError:
                print("Exception in line 129:", j)
                j = j - 10
        
        chatbox = driver.find_element_by_css_selector(chat_box_css)
        chatbox.click()
        chatbox.send_keys(Keys.RETURN)