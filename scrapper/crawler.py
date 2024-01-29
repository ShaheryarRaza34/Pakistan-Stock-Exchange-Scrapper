import requests
import re


def get(url)-> float:
    text = requests.get(url).text
    price_element = re.search('<div class="quote__close">([^<]+)</div>', text)
    price = float(str(text[price_element.start(1):price_element.end(1)])[3:])
    return price


def transaction(price:float, average_price:float)-> str:
    message = f"Average price of your stock is {average_price} "
    if price > average_price:
        return message+f"Now it is {price}  so: SELL"
    elif price < average_price:
        return message+f"Now it is {price}  so: HOLD"
    else:
        return  message+f"Now it is {price}  so: BUY"
