from splinter import Browser
from selenium import common
import time

browser = Browser('chrome')
while(True):
    browser.visit('https://google.com')
    try:
        browser.fill('q','currency converter usd to inr')
        browser.find_by_name('btnK').click()
        if browser.is_text_present('www.xe.com › XE Currency Converter - Live Rates'):
            browser.click_link_by_text('Currency Converter: USD to INR - XE.com')
        else:
            browser.quit()
    except common.exceptions.WebDriverException:
        browser.quit()
    inr = browser.find_by_css('.uccResultAmount').first.value
    inr = float(inr)

    browser.visit('https://charts.bitcoin.com')
    bitcoin_price = browser.find_by_css('span.price').value
    print(bitcoin_price)
    bitcoin_price = int("".join( [ x for x in bitcoin_price if x != '$' ] ))
    bit_inr = float(bitcoin_price) * inr

    browser.visit('https://twitter.com')
    browser.find_link_by_href('/login').click()
    browser.fill('session[username_or_email]', '----------@----.com')
    browser.fill('session[password]', '*******')
    browser.find_by_value('Log in').click()
    browser.fill('tweet', '#BitcoinPriceTweeter\nLatest value of #Bitcoin is: \n${}\nINR:{}'.format(bitcoin_price, bit_inr))
    browser.find_by_css('span.button-text.tweeting-text').click()
    bitcoin_price = str(bitcoin_price)
    print(type(bitcoin_price))
    time.sleep(20)
