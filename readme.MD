# WEB SCRAPING PRACTICE

## For Practice Only

[Halaman web untuk latihan](http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/)  
![ss1](/Screenshot_1.png)  

<hr>

To start our practice, we need to `import BeautifulSoup from bs4` and `import request`

```python
from bs4 import BeautifulSoup
import requests
```

On the website we want to get the Ultramen names and the monsters name like shown below:
![ss2](/Screenshot_2.png)  

To do that, we had to get/download the page source from the website using request library
```python
url = 'http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
web = requests.get(url)

Out = BeautifulSoup(web.content, 'html.parser')
print(Out.prettify())
```  
this will shown you the source code with a better format to look at
by using `prettify` method on `BeautifulSoup` object  
![ss4](/Screenshot_4.png)

Then you will find the names of ultraman and monsters are in a `<strong>` bracket
so you can take those names by using loop:
```python
ultraman = Out.find_all('strong')
for i in ultraman:
    print(i.text)
```

[Output]

```python
Note:
Ultra Hero 500/ ウルトラヒーロー５００
01 Ultraman
02 Ultra Seven
03 Zoffy
04 Ultraman Jack
05 Ultraman Ace
06 Ultraman Taro
07 Ultraman Leo
08 Ultraman Tiga (Multi-Type)
09 Ultraman Gaia (V2)
10 Ultraman Agul (V2)
11 Ultraman Ginga
12 Jean-Nine
13 Astra
14 Ultraman Dyna (Flash Type)
15 Ultraman 80
16 Ultraman Cosmos (Luna Mode)
17 Ultraman Nexus (Anphans)
18 Ultraman Max
19 Ultraman Mebius
20 Ultraman Hikari
21 Ultraman Zero
22 Ultraman Nice
23 Father of Ultra
24 Ultraman King
25 Ultraman Saga
26 Tiga Dark (Spark Doll)
27 Ultraman Dark (Spark Doll)
28 Ultraman Victory
29 Ultraman Ginga Strium
30 Ultraman Gingavictory
31 Shining Ultraman Zero
32 Ultraman Nexus Junis
33 Ultraman Cosmos Eclipse Mode
34 Ultraman Victory Knight
Ultra Monster 500/ ウルトラ怪獣５００
01 Alien Baltan
02 Gomora
03 Zetton
04 Zaragas
05 Eleking
06 Alien Godora
07 King Joe
08 Black King
09 Kemur
10 King Pandon
11 Ragon
12 Thunder Darambia
13 Antlar
14 Red King
15 Gavadon (B)
16 Seagorath
17 Bemstar
18 Barabas
19 King Crab
20 Vakishim
21 Doragory
22 Mochiron
23 Alien Magma
24 Salamandra
25 Golza
26 Dark Zagi
27 Jashrine
28 Alien Icarus
29 Alien Guts
30 Snowgon
31 Hanzagiran
32 Giant Yapool
33 Alien Valky
34 Astromons
35 Silvergon
36 Gan-Q (Code No. 1)
37 Ragorath
38 Zoa Muruchi
39 Lobelgar
40 Alien Empera
41 Zamsher
42 Fire Golza
43 Ultraman Belial
44 Hyper Zetton (Imago)
45 Dark Galberos (Spark Doll)
46 Alien Nackle Grey (Spark Doll)
47 Kanegon
48 Alien Miracle
49 Alien Akumania
50 Dorako
51 Telesdon
52 Evil Tiga
53 Super C.O.V
54 Alien Baltan (Basical Version)
55 Miclas
56 Dark Lugiel
57 EX Red King
58 Verokron
59 Twintail
60 Gudon
61 Sadora
62 Melba
63 Reigubas
64 Dino-Tank
65 Bemular
66 Shepherdon
67 Inpelaizer
68 Alien Metron
69 Birdon
70 King Joe Custom (Spark Doll)
71 Aribunta
72 Ace Killer
73 Judah Spectre
Ultra Monster DX/ ウルトラ怪獣DX
Ultra Monster 500 Series: Spark Dolls DX Utlive Tyrant Set
Super Grand King (Spark Doll)
Tyrant (SDU)
Zog (Ver. 2)
Alien Chibull Exceller (Spark Doll)
Fiveking (SDU)
```

Now you've seen the names of ultraman and monsters are marked with numbers
and you can ignore the rest of it.

So, with that in mind, what we need to do next is to get the names and the numbers
```python
ultra_alien = {}                        # Prepare 3 empty variable with 1 dictionary and 2 list type
temp_list = []
final = []
for i in ultraman:                      # Loop every element in variable of ultraman
    temp_list.append(i.text)            # Append every text in ultraman to temp_list

ultra_name = {}                         # Prepare 2 more empty dict variable
alien_name = {}
for i in temp_list[2:36]:               # Loop every element in temp_list starts from index ke 2 - 35 (because thats the text that we need)
    ultra_name[i[:2]] = i[2:]           # Put the element i with slicing from start till index 1 as keys, then i element from index 2 till end as values
    for j in temp_list[37:110]:         # Loop exatcly the same as the previous loop, just change the slice from index 37 to 109
        alien_name[j[:2]] = j[2:]       # Do exactly the same after the first loop
    
ultra_alien['Ultraman'] = ultra_name    # Put the variable of dict ultra_name as values and add 'Ultraman' as keys
ultra_alien['Monster'] = alien_name     # Put the variable of dict alien_name as values and add 'Monster' as keys
final.append(ultra_alien)               # append to the empty list in final variable 
print(final)
```
[Output]

```python
[{'Ultraman': {'01': ' Ultraman',
   '02': ' Ultra Seven',
   '03': ' Zoffy',
   '04': ' Ultraman Jack',
   '05': ' Ultraman Ace',
   '06': ' Ultraman Taro',
   '07': ' Ultraman Leo',
   '08': ' Ultraman Tiga (Multi-Type)',
   '09': ' Ultraman Gaia (V2)',
   '10': ' Ultraman Agul (V2)',
   '11': ' Ultraman Ginga',
   '12': ' Jean-Nine',
   '13': ' Astra',
   '14': ' Ultraman Dyna (Flash Type)',
   '15': ' Ultraman 80',
   '16': ' Ultraman Cosmos (Luna Mode)',
   '17': ' Ultraman Nexus (Anphans)',
   '18': ' Ultraman Max',
   '19': ' Ultraman Mebius',
   '20': ' Ultraman Hikari',
   '21': ' Ultraman Zero',
   '22': ' Ultraman Nice',
   '23': ' Father of Ultra',
   '24': ' Ultraman King',
   '25': ' Ultraman Saga',
   '26': ' Tiga Dark (Spark Doll)',
   '27': ' Ultraman Dark (Spark Doll)',
   '28': ' Ultraman Victory',
   '29': ' Ultraman Ginga Strium',
   '30': ' Ultraman Gingavictory',
   '31': ' Shining Ultraman Zero',
   '32': ' Ultraman Nexus Junis',
   '33': ' Ultraman Cosmos Eclipse Mode',
   '34': ' Ultraman Victory Knight'},
  'Monster': {'01': ' Alien Baltan',
   '02': ' Gomora',
   '03': ' Zetton',
   '04': ' Zaragas',
   '05': ' Eleking',
   '06': ' Alien Godora',
   '07': ' King Joe',
   '08': ' Black King',
   '09': ' Kemur',
   '10': ' King Pandon',
   '11': ' Ragon',
   '12': ' Thunder Darambia',
   '13': ' Antlar',
   '14': ' Red King',
   '15': ' Gavadon (B)',
   '16': ' Seagorath',
   '17': ' Bemstar',
   '18': ' Barabas',
   '19': ' King Crab',
   '20': ' Vakishim',
   '21': ' Doragory',
   '22': ' Mochiron',
   '23': ' Alien Magma',
   '24': ' Salamandra',
   '25': ' Golza',
   '26': ' Dark Zagi',
   '27': ' Jashrine',
   '28': ' Alien Icarus',
   '29': ' Alien Guts',
   '30': ' Snowgon',
   '31': ' Hanzagiran',
   '32': ' Giant Yapool',
   '33': ' Alien Valky',
   '34': ' Astromons',
   '35': ' Silvergon',
   '36': ' Gan-Q (Code No. 1)',
   '37': ' Ragorath',
   '38': ' Zoa Muruchi',
   '39': ' Lobelgar',
   '40': ' Alien Empera',
   '41': ' Zamsher',
   '42': ' Fire Golza',
   '43': ' Ultraman Belial',
   '44': ' Hyper Zetton (Imago)',
   '45': ' Dark Galberos (Spark Doll)',
   '46': ' Alien Nackle Grey (Spark Doll)',
   '47': ' Kanegon',
   '48': ' Alien Miracle',
   '49': ' Alien Akumania',
   '50': ' Dorako',
   '51': ' Telesdon',
   '52': ' Evil Tiga',
   '53': ' Super C.O.V',
   '54': ' Alien Baltan (Basical Version)',
   '55': ' Miclas',
   '56': ' Dark Lugiel',
   '57': ' EX Red King',
   '58': ' Verokron',
   '59': ' Twintail',
   '60': ' Gudon',
   '61': ' Sadora',
   '62': ' Melba',
   '63': ' Reigubas',
   '64': ' Dino-Tank',
   '65': ' Bemular',
   '66': ' Shepherdon',
   '67': ' Inpelaizer',
   '68': ' Alien Metron',
   '69': ' Birdon',
   '70': ' King Joe Custom (Spark Doll)',
   '71': ' Aribunta',
   '72': ' Ace Killer',
   '73': ' Judah Spectre'}}]
   ```
