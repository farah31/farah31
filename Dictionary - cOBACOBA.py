#MAP
# def times2(num):
#     return num * 2

# numList = [1, 2, 3 ,4 , 5]

# mapObj = map(times2, numList)
# result = list(mapObj)

# Or untuk persingkat

# result = list(map(times2,numList))

#DICTIONARY
# price = {
#     'apple' : 10000,
#     'grape' : 15000,
#     'orange' : 15000
# }

# print (price['grape'])

# d = {
#     'numInt' : 123,
#     'numList' : [0, 1, 2],
#     'numStr' : 'Hello',
#     'numDict' : {'insidekey' : 100}
# }

# print (d['numList'])
# print (d['numDict'])
# print (d['numDict']['insidekey'])

# keys = d.keys()

# print(keys)

# values = d.values()

# print(values)

#Cara Ubah dict dalam tupl
# interesting = (
#     {'name' : 'A', 'usia' : 27, 'intrst' : 'reading'},
#     {'name' : 'B', 'usia' : 32, 'intrst' : 'singing'},
#     {'name' : 'C','usia' : 30, 'intrst' : 'swimming'}
# )

# interesting[0]['intrst'] = 'dancing'

# print(interesting[0])

# fruits = ['Apel', 'Anggur', 'Jeruk']
# stock = [5, 7, 8]
# price = [1000, 15000, 20000]

# Upgrade :
#      Memiliki menu utama :
#       1. Melihat list buah (name | stock | price)
#       2. Menambahkan list buah
#       3. Belanja buah
#
#     - Hanya boleh ada satu while dalam input qty semua buah
#     - Setiap selesai menambahkan buah, tampilkan list buah terbaru

# wordList = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari ayam']
# search = input("masukkan kata: ")
# filter = []

#method 1
# for i in wordList: 
#     low = i.lower() 
#     upp = i.upper()
#     if search in low:
#         filter.append(i) 
#     if search in upp:
#         filter.append(i)

# print(filter)

#method 2
# for i in wordList:
#     res = search.lower() in i.lower()

#     if res == True:
#         filter.append(i)

# print(filter)

# HOMEWORK
# Buat duplicate function untuk map dan filter

# numList = [1, 2, 3 ,4 , 5]

# def times2(num):
#     return num * 2

# def myMap(func, lis):
#     mapList = []

#     for i in lis:
#         res = func(i)
#         mapList.append(res)

#     return mapList

# myMapRes = myMap(times2, numList)
# print(numList)
# print(myMapRes)

# numList = [11, 12, 13 ,14 , 15, 16, 17, 18, 19, 20]
# def even(num):
#     return num % 2 == 0

# def myFilter(fun, lis):
#     filterList = []

#     for i in lis:
#         res = fun(i)
#         if res == True:
#             filterList.append(i)
    
#     return filterList

# myFilterRes = myFilter(even, numList)
# print(numList)
# print(myFilterRes)

# for in
# if else
# len()
# join
# print()

# employee = [
#     {"name": 'Steve', "gender" : 'male', "hobbies" : ['Video games', 'Football']},
#     {"name": 'Lina', "gender" : 'female', "hobbies" : ['Shop', 'Cook']},
#     {"name": 'Reynald', "gender" : 'male', "hobbies" : ['Run', 'Hide', 'Jump']}
# ]

# Mr. Steve has 2 hobbies, they are Video games, Football
# Mrs. Lina has 2 hobbies, they are Shop, Cook
# Mr. Reynald has 3 hobbies, they are Run, Hide, Jump

# for i in range(0,len(employee)):
#     if employee [i]["gender"] == 'male':
#         nama = employee[i]["name"]
#         gend = "Mr." 

#     else :
#         nama = employee[i]["name"]
#         gend = "Mrs."

#     hob_tot = len(employee[i]["hobbies"])
#     s = ", "
#     hobbies_join = s.join(employee[i]["hobbies"])

#     print(f'{gend}{nama} has {hob_tot} hobbies, they are {hobbies_join}')

# for i in employee:
#     if i["gender"] == 'male':
#         i["name"] = 'Mr.' + i["name"]
#     else:
#          i["name"] = 'Mrs.' + i["name"]

#     name = i["name"]
#     hobbies = ", ".join(i["hobbies"])
#     hob_tot = len(i["hobbies"])

#     print(
#         f'{name} has {hob_tot} hobbies, they are {hobbies}'
#     )

# Jika sebuah kata diawali dengan huruf vokal 'aiueo', tambahkan huruf 'yay'
# Jika tidak, taruh huruf pertama di paling belakang, kemudian tambahkan 'ay'

# apple --> appleyay
# word --> ordway

#Method 1
# text = input('Masukkan kata:')

# text = text.split()
# for i in range(len(text)):
#     if text[i][0] in "aiueo":
#         text[i] += 'yay'
#     else:
#         text[i]=text[i][1:]+text[i][0]
#         text[i]+='ay'
# text = ' '.join(text)

# print(text)

#Method2

# def changeWord(word):
#     if word [0] in ['a', 'i', 'u', 'e', 'o']:
#         word += 'yay'

#     else :
#         word = word[1:] + word[0] +'ay'

#     print(word)

# changeWord("Friday")

# Reversed Sentence
# Hello my friend --> friend my Hello
# This is friday --> friday is This
# split()
# reverse()
# join

# word = ("Hello my friend")

#Method1
# word = word.split()
# res = []
# x = len(word) - 1
# while x >= 0:
#     res.append(word[x])
#     x = x-1

# result = " ".join(res)
# print(result)

#Method2
# wordsplit = word.split()
# wordsplit.reverse()
# result = " ".join(wordsplit)
# print(result)

#Method3

# def sentRev(word):
#     res = word.split()
#     res.reverse()
#     res = " ".join(res)
#     print(res)

# sentRev("Hello my friend")

# Has 99

#Method 1
def has99(lis):
    lisindex = lis.index(9)
    if lis[lisindex + 1] == 9:
        return True
    else:
        return False

#Method 2:
def has99(lis):
    lisindex = lis.index(9)
    return lis[lisindex + 1] == 9

print(has99([1,9,9]))
print(has99([5,9,2,9]))
print(has99([9,3,9]))
print(has99([7,9,9,6]))