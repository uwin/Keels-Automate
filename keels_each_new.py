from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get("https://keellssuper.com/welcome/Login")


def login():
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"UserName\"]").send_keys("fb.uwin@gmail.com")
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"Password\"]").send_keys("&A05!or8jX*q")
    sleep(1)
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[2]/div[1]/div[2]/button").click()

def others(driver):
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div/div[5]/div[1]/div/div/div[1]/div[2]/div/input").send_keys("Thalahena")
    sleep(1)
    sleep(1)
    driver.find_element_by_name("Value").send_keys(Keys.ENTER)
    sleep(1)
    sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div[5]/div/div[2]/div/div[5]/div[2]/div/div/div[1]/div[2]/div/input").send_keys("Thalahena - Malabe RD")
    sleep(1)
    sleep(1)
    driver.find_element_by_name("Value").send_keys(Keys.ENTER)
    sleep(1)
    sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[3]/div[5]/div/div[2]/div/div[5]/div[3]/div/div/div[1]/div[2]/div/input").send_keys("Thalahena - Malabe RD")
    sleep(1)
    sleep(1)
    driver.find_element_by_name("Value").send_keys(Keys.ENTER)
    sleep(1)
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[5]/div/div[2]/div/div[6]/button").click()
    

def loop(driver):
    try:
        login()
    except:
        sleep(1)
        driver.refresh()
        loop(driver)

loop(driver)
others(driver)

def checkout():
    sleep(3)
    driver.get("https://int.keellssuper.net/checkout")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_DeliName\"]").send_keys("Uwin Vidanage")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_DeliTele\"]").send_keys("0776573743")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_txtHome\"]").send_keys("44/A, Himbutana Road,",
                                                                                   "Thalahena, Malabe")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_txtDelMsg\"]").send_keys("house is near udyana mawatha")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_btnHSBCVM\"]").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"btnRefundAccept\"]").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"Visa\"]").click()
    sleep(1)


def grocery():
    driver.get("https://int.keellssuper.net/grocery/g")
    # 0 Mackerel
    # 1 chick pea      1
    # 2 green gram(loc)
    # 3 haris chandra noodless
    # 4 kirisamba
    # ---------------
    # 5 brown sugar    3
    # 6 chile pieces
    # 7 chille power   3
    # 8 curry powder R
    # 9 fenel seeds
    # ---------------
    # 10 goraka        1
    # 11 maldive fish
    # 12 mustard seeds
    # 13 peper powder  1
    # 14 peper seeds
    # ---------------
    # 15 curry power   3
    # 16 red cowpea    1
    # 17 soya sauce    1
    # 18 white cowpea  2
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
    # 30 cream craker sm munchee  2
    # 31 dhal                        2
    # 32 prima kottume
    # 33 cooking salt           1
    # 34 nadu rice
    # ---------------
    # 35 red kekulu               3
    # 36 samba
    # 37 supiri keerisamba
    # 38 white kekulu           1
    # 39 samaposha              2
    # ---------------
    # 40 coconut milk
    # 41 white sugar

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_1\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_1\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_1\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_5\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_5\"]").send_keys("3")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_5\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_7\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_7\"]").send_keys("3")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_7\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_10\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_10\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_10\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_13\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_13\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_13\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_15\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_15\"]").send_keys("3")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_15\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_16\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_16\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_16\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_17\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_17\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_17\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_18\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_18\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_18\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_24\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_24\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_24\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_26\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_26\"]").send_keys("3")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_26\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_27\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_27\"]").send_keys("3")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_27\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_28\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_28\"]").send_keys("2")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_28\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_31\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_31\"]").send_keys("2")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_31\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_33\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_33\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_33\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_35\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_35\"]").send_keys("3")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_35\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_38\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_38\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_38\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_39\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_39\"]").send_keys("2")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_39\"]").click()
    sleep(3)


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
    # 1 carrot
    # 2 coconut
    # 3 cucumber
    # 4 garlic            1
    # --------------
    # 5 ginger
    # 6 green beans
    # 7 green chilies
    # 8 lime
    # 9 potatoes
    # -------------
    # 10 red onions
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_4\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_4\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_4\"]").click()
    sleep(3)


def beverages():
    driver.get("https://int.keellssuper.net/beverages/b")
    # 0 ambewala freshmilk    2
    # 1 anchor milk           1
    # 2 harischanhra coffe    2
    # 3 apple juice
    # 4 milo drink
    # ---------------
    # 5 milo power
    # 6 nescafe
    # 7 nestamolt 1
    # 8 watawala
    # 9 zesta
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_2\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_2\"]").send_keys("2")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_2\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_1\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_1\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_1\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_7\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_7\"]").send_keys("1")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_7\"]").click()
    sleep(3)

    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_0\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_0\"]").send_keys("2")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_0\"]").click()
    sleep(3)


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
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_18\"]").clear()
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_txtQty_18\"]").send_keys("2")
    sleep(1)
    driver.find_element_by_xpath("//input[@id=\"BodyContent_RptItemList_btnBuyNow_18\"]").click()
    sleep(3)
