from selenium import webdriver
from selenium.webdriver.common import keys
from time import sleep
driver = webdriver.Edge()
driver.get("https://int.keellssuper.net/login")
def login():
    sleep(1)
    driver.find_element_by_xpath("//select[@name='ctl00$BodyContent$ddlDeliveryCity']/option[text()='Malabe']").click()
    sleep(1)
    driver.find_element_by_xpath("//select[@name='ctl00$BodyContent$ddlSuburb']/option[text()='Thalahena']").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"ctl00$BodyContent$UserName\"]").send_keys("fb.uwin@gmail.com")
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"ctl00$BodyContent$LoginPassword\"]").send_keys("^1LoK^3hktG!^gUD")
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"ctl00$BodyContent$BtnLogin\"]").click()
    sleep(1)

def loop(driver):
    try:
        login()
    except:
        sleep(1)
        driver.refresh()
        loop(driver)
loop(driver)

def grocery():
    driver.get("https://int.keellssuper.net/grocery/g")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_0\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_0\"]").send_keys("2")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_0\"]").click()
    sleep(3)
    # 0 Mackerel
    # 1 chick pea     1
    # 2 green gram(loc)
    # 3 haris chandra noodless  3
    # 4 kirisamba
    # ---------------
    # 5 brown sugar 3
    # 6 chile pieces
    # 7 chille power   3
    # 8 curry powder R
    # 9 fenel seeds
    # ---------------
    # 10 goraka             1
    # 11 maldive fish
    # 12 mustard seeds
    # 13 peper powder 1
    # 14 peper seeds
    # ---------------
    # 15 curry power   3
    # 16 red cowpea
    # 17 soya sauce        1
    # 18 white cowpea   2
    # 19 whole Chiles
    # ---------------
    # 20 corn flakes
    # 21 oats
    # 22 instant fried rice
    # 23 soy soyameat
    # 24 coconut milk power 1
    # ---------------
    # 25 maggi nodless
    # 26 choclet cream biscuit  3
    # 27 gold mari         3
    # 28 cream craker maliban 2
    # 29 marina coconut oill
    # ---------------
    # 30 cream craker sm munchee
    # 31 dhal                        2
    # 32 prima kottume
    # 33 cooking salt           1
    # 34 nadu rice
    # ---------------
    # 35 red kekulu               3
    # 36 samba
    # 37 supiri keerisamba
    # 38 white kekulu
    # 39 samaposha              2
    # ---------------
    # 40 coconut milk
    # 41 white sugar
def pharmacy():
    driver.get("https://int.keellssuper.net/pharmacy/p")
    # 0 detol liquid
    # 1 diabetasol sweetner
    # 2 link pasanguwa
    # 3 penadol
    # 4 asamodagam
    # -------------------
    # 5 siddhalepa
def vegetables():
    driver.get("https://int.keellssuper.net/vegetables/v")
    # 0 big onion
    # 1 carrot         1
    # 2 cocnut
    # 3 cucumber
    # 4 garlic            1
    # --------------
    # 5 ginger
    # 6 breen beans
    # 7 green chilies
    # 8 lime
    # 9 potatoes
    # -------------
    # 10 red onions
def beverages():
    driver.get("https://int.keellssuper.net/beverages/b")
    # 0 ambewala freshmilk    2
    # 1 anchor milk
    # 2 harischanhra coffe       2
    # 3 apple juice
    # 4 milo drink
    # ---------------
    # 5 milo power
    # 6 nescafe
    # 7 nestamolt 2
    # 8 watawala
    # 9 zesta
def household():
    driver.get("https://int.keellssuper.net/household/h")
    # 0 bc bottle wash
    # 1 bc soap
    # 2 clogad toothpaste
    # 3 baby milk
    # 4 eva pads
    # ------------
    # 5 eva napkins
    # 6 fems napkin
    # 7 flora tissues
    # 8 kohoba soap
    # 9 life bouy soap
    # ----------------
    # 10 nan 1 milk powder
    # 11 nan 2 milk powder
    # 12 nan 3 milk powder
    # 13 nan 4 milk powder
    # 14 nan celegrow milk powder
    # -------------------
    # 15 pears body talc
    # 16 signal toothpaste
    # 17 signal toothbrush
    # 18 sunlight 2
    # 19 velona cuddles
    # --------------------
    # 20 velona cuddles
    # 21 velona cuddles
    # 22 velona cuddles
    # 23 velona cuddles
    # 24 vim bar
    # --------------------
    # 25 vim liq
    # 26 whisper flow

def checkout():
    sleep(3)
    driver.get("https://int.keellssuper.net/checkout")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_DeliName\"]").send_keys("Uwin Vidanage")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_DeliTele\"]").send_keys("0776573743")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_txtHome\"]").send_keys("44/A, Himbutana Road,","Thalahena, Malabe")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_txtDelMsg\"]").send_keys("house is near udyana mawatha")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_btnHSBCVM\"]").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"btnRefundAccept\"]").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"Visa\"]").click()
    sleep(1)
