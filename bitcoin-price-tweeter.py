from splinter import Browser

browser = Browser('chrome')

browser.visit('https://google.com')
browser.fill('q','currency converter usd to inr')
browser.find_by_name('btnK').click()
if browser.is_text_present('www.xe.com › XE Currency Converter - Live Rates'):
    browser.click_link_by_text('Currency Converter: USD to INR - XE.com')
else:
    browser.quit()
inr = browser.find_by_css('.uccResultAmount').first.value
inr = float(inr)

browser.visit('https://charts.bitcoin.com')
bitcoin_price = browser.find_by_id('bb-price').value
bitcoin_price = int("".join( [ x for x in bitcoin_price if x != '$' ] ))

bit_inr = float(bitcoin_price) * inr
print(bit_inr)



browser.visit('https://twitter.com')

browser.find_link_by_href('/login').click()

browser.fill('session[username_or_email]', 'xxxxxxxxx')
browser.fill('session[password]', '**********')

browser.find_by_value('Log in').click()
browser.find_by_id('global-new-tweet-button').click()

