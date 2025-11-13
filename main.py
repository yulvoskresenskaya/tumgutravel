from itertools import count

msc_price = 13_000
spb_price = 10_000
ecb_price = 8_000

dist = input("Введите пункт поездки (msc, spb, ecb): ")

count = int(input("Ведите количество людей:"))

if dist == "msc":
    price = msc_price * count
elif dist == "spb":
    price = spb_price * count
else:
    price = ecb_price * count

print("Цена поездки:", price)

