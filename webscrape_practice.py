from bs4 import BeautifulSoup
import requests
import json

# url = 'http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
# web = requests.get(url)

# Out = BeautifulSoup(web.content, 'html.parser')

# ultraman = Out.find_all('strong') # menemukan semua yang ada di <strong>

# ultra_alien = {}
# temp_list = []
# for i in ultraman:              # 
#     temp_list.append(i.text)    # tampung ke dalam list semua text dalam <strong> tadi

# no1 = []
# ultra_name = []
# for i in temp_list[2:36]:       # karena di text sudah ada nomor maka slicing sesuai kebutuhan
#     no1.append(i[:2])           # append k list kosong no dari index 0 - 1
#     ultra_name.append(i[2:])    # append k list kosong ultra_name dari index 2 sampe abis
# x = dict(zip(no1,ultra_name))   # seteleah loop selesai di zip ke dict lalu tampung k x
# ultra_alien['Ultraman'] = x     # masukkan dict x ke dict ultra_alien dengan key Ultraman

# no2 = []
# alien_name = []
# for i in temp_list[37:110]:
#     no2.append(i[:2])
#     alien_name.append(i[2:])
# y = dict(zip(no2,alien_name))
# ultra_alien['Monster'] = y

# final = []
# final.append(ultra_alien) # masukkan ke list
# print(final)

# menulis file json
# with open ('final.json','w') as file:
#     json.dump(final,file)

# membaca file json
with open ('webscrap_practice.json','r') as file:
    Tampil = json.load(file)

print(Tampil)