from crawler import get, transaction
from configs import stocks
from notification import notification


contents = []
for stock in stocks.keys():
    current_price = get("https://dps.psx.com.pk/company/"+stock)
    contents.append({stock:transaction(current_price, stocks[stock])})
stock_alert = ''.join(str(x) for x in contents)
notification(stock_alert)




