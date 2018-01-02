from splinter import Browser

browser = Browser('chrome')
browser.visit('http://google.com')

browser.fill('q', 'Basit Hamid twitter')
button = browser.find_by_name('btnK').click()

if browser.is_text_present('twitter.com/basithamid'):
    browser.click_link_by_text('Basit Hamid (@basithamid) | Twitter')
else:
    browser.quit()



