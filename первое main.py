import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
nado = int(input("Введите длину пароля"))

password = ""

for i in range(nado):
    password += random.choice(symbols)

print(password)

