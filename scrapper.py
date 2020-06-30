

import requests
from bs4 import BeautifulSoup
import smtplib
import time


# url for Apple MacBook Pro (16-inch, 16GB RAM, 512GB Storage, 2.6GHz 9th Gen Intel Core i7) - Silver
# Change URL according to product
URL = 'https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i9/dp/B081JXDZFM?ref_=ast_sto_dp&th=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}


def checkPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    price = price[1:10].replace(',', '')
    price_f = float(price)

    my_threshold = 100000
    if price_f < my_threshold:
        print(price_f)
        sendMail('anyEmail', 'password')


def sendMail(anyEmail, passw):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(anyEmail, passw)
    subject = 'Price fell down'
    body = f'Check the amazon link : {URL}'
    msg = f"Subject : {subject} \n\n {body}"
    server.sendmail(
        f'from {anyEmail}',
        'to <yourEmail@domainname.com>',  # Enter your email in placeholder
        msg
    )
    print('Hey an Email has been sent :)')
    server.quit()


while (True):
    checkPrice()
    time.sleep(43200)  # checkPrice() every 12 hour
