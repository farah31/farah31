# import math
# X = 4
# Y = 3
# Z = 2
# S = X + Y * Z
# T = X * Y
# U = S / T
# V = math.pow(U,2)
# print(V)

# import math
# X = 5
# Y = math.pow(X,2)
# print(Y)

# days = 35

# year = int(days/360)
# days = days % 360

# month = int(days/30)
# days = days % 30

# week = int(days/7)
# days = days % 7

# print(f"{year} tahun")
# print(f"{month} bulan")
# print(f"{week} minggu")
# print(f"{days} hari")

# seconds = 5980

# hour = int(seconds/3600)
# seconds = seconds % 3600

# minute = int(seconds/60)
# seconds = seconds % 60

# print(f"{hour} jam")
# print(f"{minute} menit")
# print(f"{seconds} detik")

# hours = 5

# minute = int(hours*60)
# seconds = int(hours*3600)

# print(f"{minute} menit")
# print(f"{seconds} detik")

# totalAndiBudi = 49
# rasioAndi = 4
# rasioBudi = 10
# totalrasio = rasioAndi + rasioBudi

# umurAndi = totalAndiBudi * (rasioAndi / totalrasio) + 2
# umurBudi = totalAndiBudi * (rasioBudi / totalrasio) + 2

# print(f"{umurAndi} tahun")
# print(f"{umurBudi} tahun")

# x = 'halo dunia'
# find = 'a'
# result = x.count(find)
# print(f"Pada \"{x}\" terdapat {result} buah huruf \"{find}\"")

# AB = 300
# speedA = 60
# speedB = 100
# totalspeed = speedA + speedB
# timecrash = AB / totalspeed
# timeinHour = int(timecrash)
# timeinMinute = int((timecrash * 60) % 60)
# print(f"{timeinHour} jam {timeinMinute} menit")

# X = 7
# def ganjilgenap(X):
#     ganjil = []
#     genap = []
#     if X % 2 == 0:
#         genap.append(i)
    
#     else:
#         ganjil.append(i)
# print(ganjilgenap(X))

def get_sum(a,b):
    n2 = range(b-1, a)
    if a == b:
        res = a
        
    elif a < b:
        x1 = range(a-1, b)
        for n in x1:
        res = a + n1 + b
        
    elif b < a:
        res = b + n2 + a
    
    print(res)

get_sum(-1, 9)