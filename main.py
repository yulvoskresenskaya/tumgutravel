msc_price = 13_000
spb_price = 10_000
ecb_price = 8_000

dist = input("Введите пункт поездки (msc, spb, ecb): ")
adults = int(input("Ведите количество взрослых: "))
kids = int(input("Ведите количество детей: "))

if dist == "msc":
    dist_price = msc_price
elif dist == "spb":
    dist_price = spb_price
else:
    dist_price = ecb_price

total = dist_price * (2 * adults + kids) // 2

print("Цена поездки:", total)

