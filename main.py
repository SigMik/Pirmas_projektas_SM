# temperaturos = [20, 25, 22, 18, 12]
#
# suma = sum(temperaturos)
#
# kiekis = len(temperaturos)
#
# vidutine_temp = suma / kiekis
#
# print("Vidutine temperatura yra: ", vidutine_temp)


# lietuvos_pilietis = {
#     'id': 1,
#     'Vardas': 'Jonas',
#     'Amzius': 34,
#     'Miestas': 'Klaipėda'}
# print('Prieš:')
# print('Vardas: ', lietuvos_pilietis['Vardas'])
# print ('Po:')
# lietuvos_pilietis['Vardas']  = 'Giedrius'
# print ('Vardas: ',lietuvos_pilietis['Vardas'])
# print ('Amzius: ',lietuvos_pilietis['Amzius'])
# print ('Gyvenamoji vieta: ',lietuvos_pilietis['Miestas'])
# lietuvos_pilietis['Miestas'] = 'Alytus'
# print ('Gyvenamoji vieta: ', lietuvos_pilietis['Miestas'])

# Uzduotis = {
#     'vardas': 'Sigita'}
#
# print('Sveikinu su kursų pradžia,', Uzduotis['vardas'])
# Uzduotis['vardas'] = 'Jonas'
# print ('Sveikinu su kursų pabaiga,', Uzduotis['vardas'])

# 2. Sukurkite kintamuosius skaicius1 ir skaicius2, ir priskirkite jiems du skaičius. Parašykite programą,
# kuri juos sudeda ir išspausdina sumą.
import random

# Uzduotis 2023-09-05 (1)

# for b in range(5, 0, -1):
#     print(b)

# Uzduotis 2023-09-05 (2)

# skaiciai = [100, 23, 135, 24]
# maziausias_skaicius = skaiciai[3]
# for skaicius in skaiciai:
#     if skaicius < maziausias_skaicius:
#         maziausias_skaicius = skaicius
# print("Maziausias skaicius yra: ", maziausias_skaicius)



# skaicius = int(input("Iveskite skaiciu: "))
# suma = 0
#
# for i in range(1, skaicius +1):
#     suma += i
# print("Skaiciu suma nuo 1 iki", skaicius, "yra", suma)

# Is saraso isfiltruoti lyginius skaicius

# sarasas = [2,5,11,25,9]
# lyginiai_skaiciai = []
#
# for skaicius in sarasas :
#     if skaicius %2 ==0:
#         lyginiai_skaiciai.append(skaicius)
# print("lyginiai_skaiciai ", lyginiai_skaiciai)

# Ispausdinti piramide su zvaigzdutemis

# eiluciu_sk = int(input("iveskite sveika skaiciu"))
# for eilute in  range(1,eiluciu_sk+1):
#     tarpas = eiluciu_sk - eilute
#     luna = 2 * eilute -1
#     print(" " * tarpas + "*" * luna )

# Surasti pirminius skaicius is intervalo tarp 10 ir 50 pirminiai skaiciai

# pradzia = 10
# pabaiga = 15
#
# print(f"pirminiai skaiciai tarp {pradzia} ir {pabaiga} yra: ")
# for skaicius in range(pradzia, pabaiga +1):
#     if skaicius > 1:
#         for daliklis in range(2,skaicius):
#             if (skaicius % daliklis) ==0:
#                 break
#         else:
#             print(skaicius)

# Patikrinti zodzius is saraso. Rasti ir palikti tuos zodzius, kurie prasideda raide a.

# zodziai_is_a = ["as", "tu", "jis", "ji", "asta", "marius"]
# raide = "a"
# for zodis in zodziai_is_a:
#     if zodis[0].lower()==raide.lower():
#         print(zodis)

# 5. Sudaryti ir isvesti daugybos lentele.

# print("daugybos lentele nuo 1 iki 10")
# for i in range(1,11):
#     for j in range (1,11):
#         rezultatas = i*j
#         print (f"{i} * {j} = {rezultatas}")
#     print()

# 6. Parasyti ir patikrinti, ar skaicius, kuri ivede vartotojas yra teigiamas, neigiamas, nulis. Ir ismesti koks

# skaicius = int(input("iveskite skaiciu_> "))
# if skaicius >0:
#     print("ivestas skaicius teigiamas")
# elif skaicius <0:
#     print("ivestas skaicius neigiamas")
# else:
#     print("ivestas skaicius = 0")

# 7. Sukurti programa, kuri isveda fizz skaiciams, kurie dalinasi is 3, buzz skaiciams, kurie dalinasi is 5, fizzbuzz
# skaiciai, kurie dalinasi ir is 10 ir is 3. Iki 100.

# for skaicius in range(1,101):
#     if skaicius %3 ==0 and skaicius %5 ==0:
#         print("fizzbuzz")
#     elif skaicius %3 ==0:
#         print("fizz")
#     elif skaicius %5 ==0:
#         print("buzz")
#     else:
#         print(skaicius)

# 8. Sukurkite skaiciu atspejimo zaidima


# pasleptas_skaicius = random.randint(1,100)
# bandymai = 0
# maksimalus_bandymu_skaicius = 5
# while bandymai < maksimalus_bandymu_skaicius:
#     spejimas = int(input("atspekite paslepta skaiciu nuo 1 iki 100: "))
#     bandymai += 1
#     if spejimas == pasleptas_skaicius:
#         print(f"Valio! Atspejote skaiciu per {bandymai} bandymus")
#         break
#     elif spejimas < pasleptas_skaicius:
#         print("Bandykite didesni skaiciu")
#     else:
#         print("Bandykite mazesni skaiciu")
# if bandymai >= maksimalus_bandymu_skaicius:
#     print(f"Jus pasiekete maksimalu bandymu skaiciu. pasleptas skaicius buvo {pasleptas_skaicius}")

# Sukurti sarasa zodziu, ju ilgi ir isvesti zodzius, kurie ilgesni nei 6 raides

# zodziai = ["uosis", "pipiras", "kibiriukas", "telefonas", "kompiuteris","mama"]
# zodynas = {}
# for zodis in zodziai:
#     zodynas[zodis] = len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}: {ilgis} simboliai")

# from random import randint
#
# # skaicius = random.randint(1,100)
# # print(skaicius)
#
# atsitiktinis = randint(1, 5)
#
# spejimas = int(input('Spekite skaiciu nuo 1 iki 5: '))
#
# if spejimas == atsitiktinis:
#     print('Sveikiname, atspejote skaiciu')
# else:
#     print('Neatspejote')

# vardas = input('Iveskite savo varda: ')
#
# if vardas:
#     print('Labas ' + vardas + '!')
# else:
#     print('Nieko neivedete')

# pazymys = 9
# ivertinimas = 'Puikiai' if pazymys ==10 else 'Galima geriau'
# print(ivertinimas)

# pazymys = 10
# ivertinimas = 'Galima geriau!'
# if pazymys ==10:
#     print('Puikiai')
# else:
#     print(ivertinimas)


# taskai = 90
# tipas = 'Auksinis' if taskai > 100 else 'Sidabrinis'
# print(tipas)


# taskai = 110
# tipas = 'Auksinis' if taskai > 100 else 'Sidabrinis'
# print(taskai, tipas)
#
# taskai = 50
# tipas = 'Auksinis' if taskai > 100 else 'Sidabrinis'
# print(taskai, tipas)


# patikrinimas = True if 10*2 > 0 else False
# print(patikrinimas)


# marke = 'Citroen'
# modelis = 'Xsara'
# metai = 2002
# rida = 702000
#
# # print(f'{marke} {modelis} buvo pagaminta {metai} ir nuvaziavo {rida} km')
#
# sakinys = f"""
# {marke} {modelis}
# buvo pagaminta {metai}
# ir nuvaziavo {rida} km
# """
# print(sakinys)

# print(f'skaiciavimu atsakymas yra: {8*2+5}')

# vardas = input('Iveskite varda: ')
# print(vardas)

# skaicius = input('Iveskite skaiciu:  ')
#
# if skaicius.isdigit():
#     skaicius = int(skaicius)
#
# print('Ivestas skaicius: ', skaicius, type(skaicius))

# skaicius = int(input('Iveskite skaiciu: '))
# skaicius_1 = int(input('Iveskite antra skaiciu: '))
# print(f'{skaicius} + {skaicius_1} = {skaicius + skaicius_1}')

# Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą,
# kur n yra vartotojo įvestas skaičius. Panaudokite "for" ciklą ir "if" sąlygos sakinį, kad tikrintumėte,
# ar įvestas skaičius yra sveikasis;

# n = int(input('Iveskite skaiciu: '))
# if n <= 1:
#     print('Ivestas skaicius turi buti sveikasis, bandykite dar')
# else:
#     suma = 0
#     for skaicius in range(2,n + 1):
#         suma +=skaicius
#     print(f'suma nuo 1 iki {n} yra {suma}')

# 2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10).
# Programa turi grąžinti mokinio vertinimą (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai").
# Naudokite "if" sąlygos sakinį;

# pazymys = int(input("Iveskite pazymi nuo 1 iki 10: "))
# ivertinimas = 'Puikiai'
# ivertinimas_1 = 'Gerai'
# ivertinimas_2 = 'Vidutiniskai'
# ivertinimas_3 = 'Silpnai'
# ivertinimas_4 = 'Neuztektinai'
# if pazymys <= 3:
#     print(f'Jusu rezultatas {ivertinimas_4}')
# elif pazymys <=5:
#     print(f'Jusu rezultatas {ivertinimas_3}')
# elif pazymys <=7:
#     print(f'Jusu rezultatas {ivertinimas_2}')
# elif pazymys <=9:
#     print(f'Jusu rezultatas {ivertinimas_1}')
# elif pazymys ==10:
#     print(f'Jusu rezultatas {ivertinimas}')
# elif: pazymys >10:
#     print(f' Pazymys negali buti didenis nei 10')

# Kitas sprendimas 1 uzduoties
# # Vartotojas įveda pažymį
# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
# #
# # Vartotojas įveda pažymį

# pazymys = int(input("Įveskite mokinio pažymį nuo 1 iki 10: "))
#
# if pazymys >= 9 and pazymys <= 10:
#     vertinimas = "Puikiai"
# elif pazymys >= 7 and pazymys < 9:
#     vertinimas = "Gerai"
# elif pazymys >= 5 and pazymys < 7:
#     vertinimas = "Vidutiniškai"
# elif pazymys >= 4 and pazymys < 5:
#     vertinimas = "Silpnai"
# elif pazymys >= 1 and pazymys < 4:
#     vertinimas = "Neužtektinai"
# else:
#     vertinimas = "Netinkamas pažymys, įveskite pažymį nuo 1 iki 10."
#
# print(f"Mokinio vertinimas: {vertinimas}")

# 3. Sukurkite programą, kuri leidžia vartotojui įvesti metus. Programa turi patikrinti, ar įvesti metai yra keliamieji
# (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą

# metai = int(input('Iveskite metus: '))
# if metai %4 == 0:
#     print('Jūsų įvesti metai yra keliamieji')
# else:
#     print('Jūsų įvesti metai yra ne keliamieji')

# 4. Turite žodyną, kuriame yra vardai ir amžius.
# Parašykite programą, kuri peržiūri žodyną ir išrenka tik tas poras, kuriose amžius yra didesnis arba lygus 18.
# Rezultatus patalpinkite naujame žodyne
#
# asmenys ={
#      'Rasa': 46,
#      'Daiva': 30,
#      'Jurga': 15,
#      'Joana': 18,
#      'Antanas': 32,
#      'Jurgis': 14,
#      'Domas': 45,
#      'Linas': 37
#      }
# asmenys_naujas = {}
# for vardas, amzius in asmenys.items():
#     if amzius >= 18:
#         asmenys_naujas[vardas] = amzius
# print(asmenys_naujas)

# 5. Leiskite vartotojui įvesti kelias prekes ir jų kainas.
# Sukurkite sąrašą, kuriame prekės yra žodynai, kuriuose yra prekės studentinimas ir kaina.
# Taip pat paskaičiuokite bendrą visų prekių kainą;

# prekiu_krepselis = []
# while True:
#     preke = input("Nurodyte prekę arba įrašykite žodį baigti")
#     if not preke:
#         break
#     kaina = float(input("Įveskite prekės kainą: "))
#     prekes_info = {'pavadinimas': preke, 'kaina': kaina}
#     prekiu_krepselis.append(prekes_info)
#
# Krepselio_suma = sum((prekes_info['kaina'] for prekes_info in prekiu_krepselis))
# print("prekiu sarasas: ")
# for prekes_info in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_info['pavadinimas']}, Kaina: {prekes_info['kaina']}")
# print(f"Bendra kaina: {Krepselio_suma}")

# 2023-09-07 pamokos darbai:
#
# 1. Sukurkite sąrašą temperatūros su temperatūromis.
# Patikrinkite kiekvieną temperatūrą sąraše ir išveskite "šilta" (jei temperatūra virš 20) arba "šalta"
# (jei temperatūra 20 ar mažiau)

# temperaturos = [10, -7, 25, 36]
#
# for temperatura in temperaturos:
#      if temperatura >20:
#           print('silta')
#      elif temperatura <20:
#           print('salta')

# 2. Turite žodyną su studentų vardais ir jų pažymiais. Parašykite "for" ciklą,
# kuris išveda kiekvieno studento vardą ir jo pažymį.

# studentai = {
#      'Jonas': 9,
#      'Migle': 6,
#      'Eugenijus': 10,
#      'Tomas' : 4
#  }
#
# studentas = {}
# for vardas, pazymys in studentai.items():
#     studentas [vardas] = pazymys
# print(f'Studentai ir ju pazymiai: {studentai}')

# asmenys_naujas = {}
# for vardas, amzius in asmenys.items():
#     if amzius >= 18:
#         asmenys_naujas[vardas] = amzius


# vardai = ['Jonas', 'Petras', 'Marius', 'Laura', 'Laura']
#
# pirmas_vardas = vardai.pop(2)
# print(pirmas_vardas)
# #
# vardai.insert(1,'Giedrius')
# print (vardai)
#
# vardai.append('Onute')
# print (vardai)

# vardai.sort (reverse=True)
# print(vardai)

# vardai.remove('Laura')
# print(vardai)

# vaisiai = ('obuolys', 'kriause', 'bananas', 'braske')

# touple virsuje reiksmes nekeiciamos

# vaisia1 = ['obuolys', 'kriause', 'bananas', 'braske']

# liste virsuje galima keisti reiksmes
#
# vaisiai = {
#     'obuolys',
#     'kriause'
#     'bananas'
#     'braske'
# }
#
# vaisiai2 = vaisiai[0]
# print(vaisiai2)
#
# # sitas leidzia grazinti is saraso 0 reiksme
#
# skaiciai = (3.14, 2.71)
#
# a,b = skaiciai
# print(a)
# print(b)

# vaisiai = ['obuolys', 'kriause', 'bananas', 'braske']
#
# for sarasas, vaisius in enumerate(vaisiai, start=0):
#     print(f"{sarasas}. {vaisius}")

# Zemiau sukuriame nauja faila su tekstu:

# with open("failo_pav.txt", 'w', encoding='utf-8') as file:
#     content = file.write("Kuriame nauja faila")

# with open("failo_pav.txt", 'a', encoding='utf-8') as file:
#     content = file.write("\nPapildomas tekstas")
#     print (content)

# with open("failo_pav.txt", 'w', encoding='utf-8') as file:
#     content = file.write("Kuriame nauja faila")

# Zemiau abu pavyzdziai nuskaito sukurta faila

# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
#     content = file.read()
#     print (content)
#
# with open("failo_pav.txt", 'r', encoding='utf-8') as file:
#     for eilute in file:
#         print(eilute.strip())

# vaisiai = []
#
# with open("vaisiai.txt", 'w', encoding='utf-8') as file:
#     content = file.write('obuolys, \nkriause, \nbananas, \nbraske')

# studentai = {
#      'Jonas': 9,
#      'Migle': 6,
#      'Eugenijus': 10,
#      'Tomas' : 4
#  }
#
# studentas = {}
# for vardas, pazymys in studentai.items():
#     studentas [vardas] = pazymys
# print(f'Studentai ir ju pazymiai: {studentai}')

# 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius.
# Naudojant "while" ciklą, pridėkite kiekvieną įvestą skaičių prie sąrašo. Ciklą nutraukite, kai vartotojas įveda 0.
# NEBAIGTA

# def pasisveikinimas(vardas):
#     sveikinimas = f"Sveiki, {vardas}"
#     return sveikinimas
#
# vardas = input('Iveskite savo varda: ')
# sveikinimas = pasisveikinimas(vardas)
# print(sveikinimas)

# def pasisveikinimas(vardas):
#     sveikinimas = f'Bukite pasveikinti,{vardas}'
#     return  sveikinimas
#
# vardas = 'Jonas'
# sveikinimas = pasisveikinimas(vardas)
# print(sveikinimas)

# def ar_lyginis(skaicius):
#     if skaicius %2 == 0:
#         return True
#     else:
#         return False
#
# skaicius = 9
# if ar_lyginis(skaicius):
#     print(f'{skaicius} yra lyginis')
# else:
#     print(f'{skaicius} yra nelyginis')
#
# def suma(a,b):
#     rezultatas = a+b
#     return rezultatas
#
# x=5
# y=3
# sumos_rezultatas = suma(x,y)
# print(f'{x}+{y} = {sumos_rezultatas}')
#
# def main():
#     print('Sveikas pasauli')
#
# if __name__ == "__main__":
#     main()

# def vidurkis(skaiciai):
#     suma = sum(skaiciai)
#     avg = suma / len(skaiciai)
#     return avg
#
# sarasas = [10,15,20,25,30]
# sio_sraso_vidurkis = vidurkis(sarasas)
# print(f"saraso vidurkis: {sio_sraso_vidurkis}")

# Uzduotis. Patikrinti, ar skaicius yra teigiamas ar neigiamas.

# def ar_teigiamas(skaicius):
#     if skaicius >0:
#         return True
#     else:
#         return False
#
# skaicius = 4
# if ar_teigiamas (skaicius):
#     print(f'{skaicius} yra teigiamas')
# else:
#     print(f'{skaicius} yra neigiamas')

# Parasyti funkcija, kuri suras max sarase

# def didziausias_skaicius(skaicius):
#     didziausias = skaicius[0]
#     for i in skaicius:
#         if i>didziausias:
#             didziausias = i
#     return didziausias
#
# sarasas =[10,658,12,-2]
# didziausias=didziausias_skaicius(sarasas)
# print(f'didziausias yra {didziausias}')

# def sujungimas_saraso(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
#
# s = [10,15,12,15]
# d = [12,15,25,36]
# rezultatas = sujungimas_saraso(s,d)
# print(rezultatas)

# Funkcija, kuri suras didesni skaiciu nei sarase:

# def didesnis(end, skaicius):
#     didesni = [sk_1 for sk_1 in end if sk_1>skaicius]
#     return didesni
#
# end = [1,2,15,101,1005]
# n = 8
# didesni_sk = didesnis(end, n)
# print(f'sarase skaiciai didesni uz {n}: yra {didesni_sk}')

# ilgas_tekstas = 'Ilgas tekstas ir \
# ilgas pasakojimas'
# print(ilgas_tekstas)

# kiek = 5
# for i in range(kiek):
#     print(i)

# for skaicius in range(1,13):
#     if skaicius %2==0 or skaicius %5==0:
#         print(f'patekes {skaicius} dalinasi is 2 arba 5')

# pradzia = 7
# pabaiga = 20
# for i in range(pradzia, pabaiga+1):
#     print(f'skaicius{i}')

# pradzia, pabaiga = 7,10
# for i in range(pradzia, pabaiga+1):
#     print(f'skaicius {i}')

# vardas = str(input('Iveskite savo varda: '))
# kiek = int(input('Iveskite kiek kartu norite pakartoti ivesta varda: '))
# for vaziuojam in range(kiek):
#     print(vardas)

# print(0)
# print(1)
# print(2)
# print(3)

# for i in range(4):
#     print(i)

# visi_teigiami = True
# for skaicius in [6,1,5,-1,4,5]:
#     if skaicius <0:
#         visi_teigiami = False
#         break
#     print('Visi teigiami:', visi_teigiami)

# 2023-09-06 3 namų darbas:
# 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius. Naudojant "while" ciklą,
# pridėkite kiekvieną įvestą skaičių prie sąrašo. Ciklą nutraukite, kai vartotojas įveda 0. NEBAIGTA


# 2023-09-06 4 namų darbas:
# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos. Vartotojas įveda gėrimo pavadinimą,
# o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne. Jei taip, išveskite jo kainą; jei ne,
# išveskite pranešimą "Gėrimas nerastas". NEBAIGTAS:
#
# drinkas=input('Iveskite gerimo pavadinima: ')
#
# gerimai={
#     'Cola':3,
#     'Fanta': 3,
#     'Arbata':2,
#     'Kava':6
# }
# if drinkas in gerimai:
#     kaina = gerimai[drinkas]
#     print(kaina)
# else:
#     print('Tokio gerimo neturime')
#
# studentai = {
#      'Jonas': 9,
#      'Migle': 6,
#      'Eugenijus': 10,
#      'Tomas' : 4
#  }
#
# studentas = {}
# for vardas, pazymys in studentai.items():
#     studentas [vardas] = pazymys
# print(f'Studentai ir ju pazymiai: {studentas}')


#
# pradzia = 10
# pabaiga = 15
#
# dabartinis = pradzia
#
# while dabartinis<=pabaiga:
#     print(dabartinis)
#     dabartinis +=1

# print(pradzia, pabaiga)

# tekstas = 'Sita teksta isvedame'
# kiek_liko = 10
#
# while kiek_liko >0:
#     print(tekstas)
#     kiek_liko -= 1

# from random import randint

# skaicius = 1
#
# while skaicius <10:
#     skaicius = randint(1,20)
#     print(skaicius)
#
# kiekis = 15
#
# while kiekis >0:
#     print('Kiekis pries pirkima:',kiekis)
#     nupirkta = randint(1,20)
#     print('Nupirkta:', nupirkta)
#     if nupirkta>kiekis:
#         nupirkta = kiekis
#     kiekis -= nupirkta
#     print('Likutis:', kiekis)
#     print()

# from random import randint
#
# kiekis = 20
#
# while kiekis >0:
#     nupirkta = randint(1,10)
#     print(f'Kiekis pries pirkima: {kiekis:<5} | Nupirkta: {nupirkta} | Liko: {kiekis-nupirkta}')
#     kiekis -=nupirkta

#
# prekiu_kiekis = 24
#
# while prekiu_kiekis >0:
#     print(f'Turimas prekiu kiekis: {prekiu_kiekis}')
#     pirkimo_kiekis = int(input('Kiek norite nupirkti? '))
#     if pirkimo_kiekis>prekiu_kiekis:
#         pirkimo_kiekis = prekiu_kiekis
#     print(f'Nupirkote {pirkimo_kiekis}')
#     print()
#     prekiu_kiekis -=pirkimo_kiekis

# from random import randint

# while True:
#     skaicius = random.randint(1,100)
#     print(skaicius)

    # if skaicius %7 ==0 and skaicius %2 ==0:
    #     print(f'Skaičius {skaicius} dalinasi iš 7 ir iš 2')
    #     break

# ar_dar_ieskoti = True
#
# while ar_dar_ieskoti:
#     skaicius = randint(1,30)
#     print(skaicius)
#
#     if skaicius % 7== 0 and skaicius %2 ==0:
#         print (f'skaicius {skaicius} dalinasi is 7 ir 2')
#         ar_dar_ieskoti = False
#
# skaiciai = [7,5,6,8]
# print(skaiciai)

# zmones = ['Audija', 'Tomas', 'Juozas', 'Jonas']
# print(zmones)

# skaiciai = [1,2,3,4]
# # skaiciai.append(20)
# # skaiciai.append(10)
# # print(skaiciai)
#
# # skaiciai.extend ([7,8,9])
# # print(skaiciai)
# papildymas = [7,8,9]
# skaiciai.extend(papildymas)
# print(skaiciai)

# skaiciai = [5,2,3,5,4]
# print(len(skaiciai))
# papildymas=[54,12,36]
# skaiciai.extend(papildymas)
# print(skaiciai)
# skaiciai.append(1025)
# print(skaiciai)
# print(len(skaiciai))

# tekstas = 'obelis'
# print(len(tekstas))

# skaiciai =[101,254,2,25,56,154]
# print(f'Paskutinis saraso skaicius: {skaiciai[-1]}')

# pazymiai =[8,6,5,8]
# suma = pazymiai[0] +pazymiai[1]+pazymiai[2]+pazymiai[3]
# vidurkis = suma/len(pazymiai)
# print(vidurkis)

# suma = 0
# for pazymys in pazymiai:
#     suma = suma +pazymys
# print(suma)

# print (sum(pazymiai))

# vardai = ['Agne', 'Tomas']
# print(vardai)
# vardai[0] = 'Jonas'
# # print(vardai)
# print(*vardai)

# skaicius = int ('35')
# tekstas = str(45)
# rinkinys = {'Kaunas', 'Vilnius'}
# sarasas =list(rinkinys)
# print(skaicius)
# print(tekstas)
# print(sarasas)

# skaiciai = []
# print(skaiciai)
# skaiciai.append(2)
# skaiciai.append(52)
# print(skaiciai)

# skaiciai =[5,4,2,3]
# skaiciai.pop(0)
# print(skaiciai)

# skaiciai =[5,6,8,9]
# # print(skaiciai)
# # skaiciai.clear()
# # print(skaiciai)
# print(skaiciai.index(9))

# tekstas = ['mano', 'batai', 'buvo', 'du', 'kompiuteris']
# # print(tekstas.index('batai',1,4))
# print('batai'in tekstas)

# miestai = 'Kaunas', 'Birzai', 'Kaunas'
# # if 'Kaunas' in miestai:
# #     print('Kaunas tarp miestu rastas')
# # else:
# #     print('Kaunas tarp miestu nerastas')
# print(miestai.count('Kaunas'))

# zodziai =['lapas', 'medis', 'kamienas']
# zodziai.sort()
# print(zodziai)

# skaiciai = [10,5,4,8]
# skaiciai.sort()
# print(skaiciai)
# skaiciai.reverse()
# print(skaiciai)

# 2023-09-07 4 namų darbas:
# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos. Vartotojas įveda gėrimo pavadinimą,
# o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne. Jei taip, išveskite jo kainą; jei ne,
# išveskite pranešimą "Gėrimas nerastas".

# ivestas_gerimas=input('Iveskite gerimo pavadinima: ')
#
# gerimai={
#     'Cola':3,
#     'Fanta': 3,
#     'Arbata':2,
#     'Kava':6
# }
# if ivestas_gerimas in gerimai:
#     kaina = gerimai[ivestas_gerimas]
#     print(kaina)
# else:
#     print('Tokio gerimo neturime')

# 2023-09-06 5 namų darbas:
# 5. Patikrinkite, ar skaičiai sąraše yra lyginiai arba nelyginiai. Sukurkite du tuščius sąrašus:
# vienas lyginiams ir kitą nelyginiams skaičiams, išrūšiuokite lyginius
# ir nelyginius skaičius iš skaičiai sąrašo.

# sarasas = [2,5,11,25,9, 103, 254, 16]
#
# lyginiai_skaiciai = []
# nelyginiai_skaiciai =[]
#
# for skaicius in sarasas:
#     if skaicius %2 ==0:
#         lyginiai_skaiciai.append(skaicius)
# lyginiai_skaiciai.sort()
# print(lyginiai_skaiciai)
# for skaicius in sarasas:
#     if skaicius %2>0:
#         nelyginiai_skaiciai. append(skaicius)
# nelyginiai_skaiciai.sort()
# print(nelyginiai_skaiciai)


# sarasas = [2,5,11,25,9]
# lyginiai_skaiciai = []
#
# for skaicius in sarasas :
#     if skaicius %2 ==0:
#         lyginiai_skaiciai.append(skaicius)
# print("lyginiai_skaiciai ", lyginiai_skaiciai)

# 2023-09-08 1 namų darbai:
# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;

# def pazymiu_vidurkis(pazymiai):
#     suma = sum(pazymiai)
#     pazymiu_kiekis = len(pazymiai)
#     vidurkis = suma/pazymiu_kiekis
#     return vidurkis
#
# studento_pazymiai = [8,5,9,10,10,10,9]
# studento_pazymiu_vidurkis = pazymiu_vidurkis(studento_pazymiai)
# print(f'Studento pazymiu vidurkis yra {studento_pazymiu_vidurkis}')

# 2023-09-08 2 namų darbai:
# 2. Sukurkite funkciją pirminiai_skaiciai(n), kuri priima sveikąjį skaičių n
# ir grąžina visus pirminius skaičius nuo 2 iki n;

# def grazinimas_pirminiu_skaiciu(pradzia, pabaiga):
#     for skaicius in range(pradzia, pabaiga +1):
#         if skaicius > 1:
#             for daliklis in range(2,skaicius):
#                 if (skaicius % daliklis) ==0:
#                     break
#             else:
#                 print(skaicius)
#     pirminiai_skaiciai = skaicius
#     return pirminiai_skaiciai
#
# skaiciai = [4,11]
# siu_skaiciu_pirminiai_skaiciai = grazinimas_pirminiu_skaiciu(4,11)
# print(f'Pirminiai skaiciai nurodyti auksciau')


# 2023-09-08 3 namų darbai:
# 3. Sukurkite funkciją zodziu_kiekis(tekstas), kuri priima tekstą ir grąžina žodžių skaičių tekste. Ž
# odžius galite laikyti atskirtais tarpais; NEBAIGTA

# def zodziu_skaiciavimas(tekstas):
#     zodziai = tekstas.split()
#     zodziu_kiekis = len(zodziai)
#     return zodziu_kiekis
#
# tekstas = ('Marija planuoja atostogas vasarą')
# sio_teksto_zodziu_kiekis = zodziu_skaiciavimas(tekstas)
# print(f'Zodziu kiekis siame tekste yra {sio_teksto_zodziu_kiekis}')

# Paprastas bandymas del zodziu kiekio iskaiciavimo:
#
# tekstas = ('Marija planuoja atostogas vasarą')
# zodziai= tekstas.split()
# kiekis = len(zodziai)
# print(f'Zodziu kiekis siame tekste yra {kiekis}')

# 2023-09-08 4 namų darbai:
# 4. Sukurkite funkciją didziausias_elementas(sarasas), kuri priima sąrašą skaičių ir grąžina didžiausią elementą;

#1 bandymas (NEPAVYKSTA ISSIAISKINTI, KODEL NEMATO MAX SKAICIAUS 80000)

# def didziausias_elementas(elementas):
#     didziausias = elementas[0]
#     for el in elementas:
#         if el >didziausias:
#             didziausias = el
#             return didziausias
#
# sarasas = [100, 2, 52365, 300, 10, 11, 1000, 80000]
# didziausias = didziausias_elementas(sarasas)
# print(f'Didziausias elementas pateiktame sarase yra {didziausias}')

# 2 BANDYMAS PAMOKOJE BAIGTA
# def didziausias_skaicius(skaicius):
#     didziausias = skaicius[0]
#     for i in skaicius:
#         if i>didziausias:
#             didziausias = i
#     return didziausias
#
# sarasas =[100, 2, 52365, 300, 10, 11, 1000, 80000]
# didziausias=didziausias_skaicius(sarasas)
# print(f'didziausias yra {didziausias}')

# 2023-09-08 4 namų darbai:
# 4. Sukurkite funkciją didziausias_elementas(sarasas), kuri priima sąrašą skaičių ir grąžina didžiausią elementą;

def didziausias_elementas(elementas):
    didziausias = elementas[0]
    for i in elementas:
        if i>didziausias:
            didziausias = i
    return didziausias

sarasas =[100, 2, 52365, 300, 10, 11, 1000, 80000]
didziausias = didziausias_elementas(sarasas)
print(f'Didziausias elementas sarase yra {didziausias}')






