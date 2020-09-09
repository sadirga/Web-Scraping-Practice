from bs4 import BeautifulSoup
import requests
import json

url = 'http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
web = requests.get(url)

Out = BeautifulSoup(web.content, 'html.parser')

ultraman = Out.find_all('strong')       # Menemukan semua yang ada di <strong>

ultra_alien = {}                        # Siapkan 3 variabel berisikan 1 dictionary dan 2 list kosong
temp_list = []
final = []
for i in ultraman:                      # Loop setiap elemen dalam variabel ultraman
    temp_list.append(i.text)            # Sisipkan setiap text dalam ultraman ke temp_list

ultra_name = {}                         # Siapkan lagi 2 variabel dict kosong
alien_name = {}
for i in temp_list[2:36]:               # Loop setiap elemen di temp_list dimulai dari index ke 2 - 35 (karena yang mau diambil ada disitu)
    ultra_name[i[:2]] = i[2:]           # Memasukkan elemen ke-i dengan slicing dari awal sampai index 1 sebagai keys, lalu elemen ke - i dari index 2 dst sebagai values
    for j in temp_list[37:110]:         # Loop yang sama persis seperti loop sebelumnya, hanya slicingnya dimulai dari index ke 37-109
        alien_name[j[:2]] = j[2:]       # Sama persis seperti langkah sebelumnya
    
ultra_alien['Ultraman'] = ultra_name    # Memasukkan variabel dict ultra_name sebagai values dan 'Ultraman' sebagai keys
ultra_alien['Monster'] = alien_name     # Memasukkan variabel dict alien_name sebagai values dan 'Monster' sebagai keys
final.append(ultra_alien)               # Disisipkan ke variable list
print(final)
