"""n butun soni berilgan n > 0. Agar n soni 3 ning darajasi bo'lsa 3 ning darajasi, aks
holda 3 ning darajasi emas degan natija chiqaruvchi programma tuzilsin. Qoldiqli bo'lish
va bo'lish amallarini ishlatmang"""

n = int(input("n sonini kiriting: "))

if n <= 0:
    print(f"{n} 3 ning darajasi emas")
else:
    power = 1
    while power < n:
        power *= 3
    if power == n:
        print(f"{n} 3 ning darajasi")
    else:
        print(f"{n} 3 ning darajasi emas")