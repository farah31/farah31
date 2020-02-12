# PERTAMA
# Buat sebuah function yang menerima list
# Akan me return hasil kali dua dari semua angka di dalam list

# nilaiAWal = [1, 3, 5, 7]
# hasilakhir = [2, 6, 10, 14]

#Solving
#Method 1
# def kelipatan(x):
#     ab = []
#     for i in range(0, len(x)):
#         ab.append(x[i]*2)

#     return(ab)

# x=[1,3,5,7]
# print('[1, 3, 5, 7]')
# print(kelipatan(x))

#Method 2
# listone = [1, 3, 5, 7]

# def multiTwo(data):
#     listfinal = []

#     for i in data:
#         res = i * 2
#         listfinal.append(res)

#     return listfinal

# finalresult = multiTwo(listone)

# print(listone)
# print(finalresult)

#Method 3
# listone = [1, 3, 5, 7]

# def multiTwo(data):
#     listfinal = [i * 2 for i in data]

#     return listfinal

# print(multiTwo(listone))

# KEDUA
# Sebuah function yang dapat memisahkan nilai genap dan ganjil
# [11, 22, 34, 41, 52, 63, 71, 86,]
# [[22, 34, 52, 86], [11, 41, 63 ,71]]

#Method 1
# def ganjilgenap(x):
#     genap = []
#     ganjil = []
#     ganjilgenap = []
#     for i in x:
#         if (i % 2 == 0):
#             genap.append(i)

#         else:
#             ganjil.append(i)

#     ganjilgenap.append(genap)
#     ganjilgenap.append(ganjil)
#     return ganjilgenap

# x=[11, 22, 34, 41, 52, 63, 71, 86]
# print(ganjilgenap(x))

#Method2

# starList = [11, 22, 34, 41, 52, 63, 71, 86]

# def oddEven(listnumber):
#     oddlist = []
#     evenlist = []
#     finallist = []

#     for i in listnumber:
#         if i % 2 == 0:
#             evenlist.append(i)

#         else:
#             oddlist.append(i)

#     finallist.append(evenlist)
#     finallist.append(oddlist)

#     return finallist

# result = oddEven(starList)
# print(result)

x = [40, 100, 1, 5, 25, 10]

#Method 1:
# def minMax(listNumber):
#     listNumber.sort()
#     print(f"terendah{x[0]}")
#     listNumber.sort(reverse=True)
#     print(f"tertinggi{x[0]}")
    
# result = minMax(x)
# print(result)

def minMax(listNumber):
    terendah: []
    tertinggi: []

    for i in listNumber:
        if i < min:
            min = i

        else:
            if i > max:
            max = i

    return [listNumber, min, max]

tmp = minMax(x)
print(f'listNumber : {tmp[0]}')
print(f'min : {tmp[1]}')
print(f'max : {tmp[2]}')
