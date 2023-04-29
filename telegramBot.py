import requests
adress="https://finans.truncgil.com/today.json"
datasample=statue.json()

tarih=datasample["Update_Date"]
gbp=datasample["GBP"]
alis=gbp["Alış"]
satis=gbp["Satış"]
message="Günaydın, {} tarihine ait GBP kur bilgileri şöyledir: \n Alış Bilgileri:{} \n Satış Bilgileri:{} \n İyi Günler..." .format(tarih,alis,satis)
print(message)


requests.post(url='https://api.telegram.org/bot<token>/sendMessage', data={'chat_id': 502828076, 'text': 'SomeTextHere...'}).json()
requests.post(url='https://api.telegram.org/bot<token>/sendMessage', data={'chat_id': 502828076, 'text': message}).json()