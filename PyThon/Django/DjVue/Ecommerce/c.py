import urllib, json
import urllib.request


url = "https://shopee.vn/api/v2/item/get?itemid=6858113768&shopid=324557412"



response= urllib.request.urlopen(url)
data = json.loads(response.read())
print(data['item']['name'])



url = "https://shopee.vn/api/v4/product/get_purchase_quantities_for_selected_model?itemId=6858113768&modelId=51446825386&quantity=1&shopId=324557412"

response= urllib.request.urlopen(url)
data = json.loads(response.read())
x =data['available_price_and_stocks'][0]['display_price']
print(x)