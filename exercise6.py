"""n natural soni berilgan n > 0. Quyidagi ifodani hisoblovchi programma tuzilsin. n!! = n * (n-2) * (n - 4)
Agar n juft bo'lsa oxirgi ko'payuvchi 2, toq bo'lsa 1 bo'ladi"""

n = int(input("n sonini kiriting: "))

result = 1

if n > 0: 
    if n % 2 == 0:
        lastnum = 2
    else:
        lastnum = 1

    while lastnum <= n:
        result *= n
        n -= lastnum
    print(result)
else:
    print("0 dan katta son kiriting: ")