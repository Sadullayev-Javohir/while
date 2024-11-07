"""n natural soni berilgan (n > 0). Kvadrati n dan katta bo'lmagan eng katta butun
k sonni (k ** 2 <= n) aniqlovchi programma tuzilsin. Ildizdan chiqaruvchi funksiyadan
foydalanmang."""

n = int(input("n sonini kiriting: "))
k = 0
if n > 0:
    while (k + 1) ** 2 <= n:
        k += 1
    print(k)    
else:
    print("0 dan katta son kiriting: ")