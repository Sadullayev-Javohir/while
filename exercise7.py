"""n natural soni berilgan. Kvadrati n dan katta bo'ladigan eng kichik butun k 
sonini (k**2 > n) aniqlovchi programma tuzilsin. Ildizdan chiqaruvchi funksiyadan
foydalanmang."""

n = int(input("n sonini kiriting: "))

if n > 0:
    k = 1
    while k * k <= n:
        k += 1
        print(f"{k}**2 > {n}")
    print(f"{k}² > {n}")