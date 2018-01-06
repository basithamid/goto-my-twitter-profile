from splinter import Browser
import time

browser = Browser('chrome')
while(True):
    try:
        browser.visit('https://google.com')

        try:
            browser.fill('q','currency converter usd to inr')
            browser.find_by_name('btnK').click()
            if browser.is_text_present('www.xe.com › XE Currency Converter - Live Rates'):
                browser.click_link_by_text('Currency Converter: USD to INR - XE.com')
                inr = browser.find_by_css('.uccResultAmount').first.value
                inr = float(inr)

                browser.visit('https://charts.bitcoin.com')
                bitcoin_price = browser.find_by_css('span.price').value
                print(bitcoin_price)
                bitcoin_price = int("".join([x for x in bitcoin_price if x != '$']))
                bit_inr = float(bitcoin_price) * inr

                browser.visit('https://twitter.com')
                if not browser.find_link_by_href('/login').is_empty():
                    browser.find_link_by_href('/login').click()
                    browser.fill('session[username_or_email]', 'email@email.com')
                    browser.fill('session[password]', '********')
                    browser.find_by_value('Log in').click()
                else:
                    pass
                browser.fill('tweet',
                             '#BitcoinPriceTweeter\nLatest value of #Bitcoin is: \n${}\nINR:{}'.format(bitcoin_price,
                                                                                                       bit_inr))
                browser.find_by_css('span.button-text.tweeting-text').click()
                bitcoin_price = str(bitcoin_price)
                print(type(bitcoin_price))
            else:
                browser.quit()
        except:
            print("Can't find button")
            browser.quit()
            browser = Browser('chrome')
            continue
    except ConnectionRefusedError:
        browser.quit()
        print("Closing browser")
        browser = Browser('chrome')
        continue
    time.sleep(3600)