# class Person:
#     def __init__(self, _name, _age):
#         self.name = _name
#         self.age = _age

#     def greet(self, _time):
#         print(f'Good {_time}, My name is {self.name}')

# obj = Person('Karen', 28)

# print(obj.name) #'Karen'
# obj.age #28
# print(obj.__dict__) #{'name' : 'Karen', 'age': 28}
# print(obj.__dict__["name"]) #'Karen'
# obj.greet('Evening')

# Number One
# def wordRev
# Buatlah sebuah function yang menerima sebuah kata
# Reverse huruf setiap kata

# Contoh:
#   Hello my friend --> olleH ym dneirf
#   abc de efg --> cba ed gfe


# Number Two
# def sum01
# Buat function yang menerima list of number
# Jumlahkan semua angka, kecuali angka yang ada diantara angka 0 - 1

# def sum01(lis):
#     nol = lis.index(0)
#     satu = lis.index(1) + 1

#     del lis[nol:satu]

#     result = sum(lis)
#     print(result)

# sum01([7, 0, 3, 1, 7, 9])

# [2, 4, 0, 1, 11] -- > 17 (0, 1 tidak masuk hitungan)
# [7, 0, 3, 1, 7, 9] --> 23 (0, 3, 1 tidak masuk hitungan)
# [5, 0, 3, 2, 1] --> 5 (0, 3, 2, 1 tidak masuk hitungan)

def solveMeFirst(a,b):
	# Hint: Type return a+b below
    res = a + b
    print(res)
    
solveMeFirst(2,3)