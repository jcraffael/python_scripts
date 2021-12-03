from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os


#opt = Options()
#opt.add_argument(r'user-data-dir=$(pwd)/messenger_profile')
#msnger_url = r'https://www.facebook.com/messages/t/100046711267726'
msnger_url = r'https://www.facebook.com/messages/t/100046711267726'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(r'/home/cjiang/Downloads/chromedriver', chrome_options=chrome_options)

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

dic_time_str = {0:'1. ni 7',
1.5:'2. 4', 2.5:'3', 10:'3. 1234567890 13', 6.5:'4. $$$$$$$$$$$$$$$$$$$$$$$$$$ 29', 8.5:'5. abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz 85'
, 4:'6. ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ 127',
7:'7. ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ 168',
8:'8.123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890 336',
9:'9. 8. ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ 1689.123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890 336'
, 11:'1. ni 7 2. 4 3. 1234567890 13 4.$$$$$$$$$$$$$$$$$$$$$$$$$$ 29 5. abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyz 85 6. ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳ 1277.    158. ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ 1689.123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890 33610. 8. ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ ABCDEFGHIJKLMNOPQRSTUVWXYZ 1689.123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳123456789012345678901234567890 336'
, 7.5:'11. aadffdff ][[ll;l;l[l[l[l[l', 9.5:' ssshaode#####777&&&&&&', 12.5:'https://transparencyreport.google.com/https/overview?time_os_region=chrome-usage:2;series:time;groupby:os&lu=time_os_region Guardate landamento dell"encryption" in rete... In particolare, il grafico verso fine pagina: "Percentuale di tempo trascorso su pagine HTTPS in Chrome per paese/area geografica"..',
10:'Secondo me vale la pena fare dei test a largo spettro, ovvero fare delle catture da 100 post (tanto abbiamo gli script automatici) e fare delle catture SENZA post ma facendo navigazione a casa su facebook/messenger '}

count = 100
chat_box_css = 'div[aria-describedby]'
action = ActionChains(driver)

try:
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Message"][role="textbox"]')))
except TimeoutException:
    driver.refresh()
    time.sleep(5)
#time.sleep(5)
for i in range(count):
    if i % 6 == 0:
        j = i // 6
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-hidden="false"][aria-label="Choose a GIF"][role="button"][tabindex="0"]'))).click()
        time.sleep(2)
        search_bar = WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[dir="ltr"][aria-label="GIF search"]')))
        search_bar.send_keys(Keys.TAB * (j + 1))
        time.sleep(1)
        GIF = WebDriverWait(driver, 15).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'img[height][width="274"][alt][referrerpolicy][src]')))
        GIFs = driver.find_elements_by_css_selector('img[width="274"]')
        while j >= 0:
            try:
                #action.move_to_element(GIFs[j]).click(GIFs[j]).perform()
                GIFs[j].click()
                break
            except IndexError:
                print("Exception in line 69 with j", j)
                j = j - 5

    elif i % 6 == 1:
        j = i // 6
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-hidden="false"][aria-label="Choose a sticker"][role="button"][tabindex="0"]'))).click()
        time.sleep(2)
        try:
            sticker_icon = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[class][type="submit"][value="1"][style]')))
        except TimeoutException:
            continue

        #action.move_to_element(sticker_icon).click(sticker_icon).perform()
        sticker_icon.click()
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[class="_5r8i"][role="img"]')))

        time.sleep(1)
        stickers = driver.find_elements_by_css_selector('div[class="_5r8i"][role="img"]')
        while j >= 0:
            try:
                #action.move_to_element(stickers[j]).click(stickers[j]).perform()
                try:
                    stickers[j].click()
                except ElementClickInterceptedException:
                    action.move_to_element(stickers[j]).click(stickers[j]).perform()
                break
            except IndexError:
                print("Exception in line 98")
                j = j - 5
    elif i % 6 == 2:
        j = i // 6

        time.sleep(2)
        WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Choose an emoji"][role="button"]'))).click()
        WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Smileys & people"]')))
        time.sleep(3)
        emojis = driver.find_elements_by_css_selector('img[height="30"]')
        while j>=0:
            try:
                #action.move_to_element(emojis[j]).click(emojis[j]).perform()
                emojis[j].click()
                break
            except IndexError:
                print("Exception in line 116:", j)
                j = j - 5
        
        chatbox = driver.find_element_by_css_selector(chat_box_css)
        chatbox.click()
        chatbox.send_keys(Keys.RETURN)
    elif i % 6 == 3:
         # Reply msgs
         time.sleep(2)
         #reply_but = driver.find_elements_by_css_selector('g[fill-rule="evenodd"]')
         message = driver.find_elements_by_css_selector('div[data-scope="messages_table"]')
         action.move_to_element(message[len(message) - 1]).perform()
         time.sleep(1)
         reply_but = driver.find_elements_by_css_selector('div[aria-label="Reply"]')
         print("The length is ", len(reply_but))
         print("Now click reply in line 131")
         j = len(reply_but) - 1
         while j >= 0:
            try:
                if reply_but[j].is_enabled() and reply_but[j].is_displayed():
                    action.move_to_element(reply_but[j]).click(reply_but[j]).perform()
                    time.sleep(2)
                    chatbox = driver.find_element_by_css_selector(chat_box_css)
                    chatbox.click()
                    chatbox.send_keys("haha" + Keys.RETURN)
                    print("Msg replied")
                    break
            except StaleElementReferenceException:
                j = j - 1
         time.sleep(2)
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
         print("Scrolled down")
    elif i % 6 == 4:
        # Foward msgs
         time.sleep(3)
         message = driver.find_elements_by_css_selector('div[data-scope="messages_table"]')
         action.move_to_element(message[len(message) - 1]).perform()
         time.sleep(1)
         three_dots_but = driver.find_elements_by_css_selector('circle[stroke-width="1px"]')
         print("The length is ", len(three_dots_but))
         print("Now click more in line 156")
         j = len(three_dots_but) - 1
         while j >= 0:
            try:
                if three_dots_but[j].is_enabled() and three_dots_but[j].is_displayed():
                    action.move_to_element(three_dots_but[j]).click(three_dots_but[j]).perform()
                    try:
                        WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Forward"]'))).click()
                    except TimeoutException:
                        print("Exception in line 169")
                        break
                    time.sleep(2)
                    contact = driver.find_element_by_css_selector('div[aria-label="Send to Huawei Pventi"]')
                    if contact.is_displayed():
                        contact.click()
                        WebDriverWait(driver, 10).until(ec.invisibility_of_element((contact)))
                        print("Msg forwarded.")
                    time.sleep(1)
                    close = driver.find_element_by_css_selector('div[aria-label="Close"]')
                    close.click()
                    break
            except StaleElementReferenceException:
                print("Exception in line 181:", j)
                j = j - 1
         time.sleep(2)
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
         print("Scrolled down")
    else:
        j = i 
        chatbox = driver.find_element_by_css_selector(chat_box_css)
        while j>=0:
            try:
                time.sleep(list(dic_time_str.keys())[j])
                chatbox.send_keys(list(dic_time_str.values())[j]+ Keys.ENTER)
                break
            except IndexError:
                print("Exception in line 192:", j)
                j = j - 10

    if i % 10 == 9:
    # Remove msg
         time.sleep(2)
         message = driver.find_elements_by_css_selector('div[data-scope="messages_table"]')
         action.move_to_element(message[len(message) - 1]).perform()
         time.sleep(1)
         three_dots_but = driver.find_elements_by_css_selector('circle[stroke-width="1px"]')
         print("The length is ", len(three_dots_but))
         print("Now click more in line 203")
         j = len(three_dots_but) - 1
         while j >= 0:
            try:
                if three_dots_but[j].is_enabled() and three_dots_but[j].is_displayed():
                    action.move_to_element(three_dots_but[j]).click(three_dots_but[j]).perform()
                    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Remove Message"]'))).click()
                    WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Remove"]'))).click()
                    try:
                        WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="OK"]'))).click()
                    except TimeoutException:
                        break
                    print("Msg removed.")
                    break
            except StaleElementReferenceException:
                j = j - 1
         time.sleep(2)
         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
         print("Scrolled down")
