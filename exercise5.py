"""2 sonining qandaydir darajasini bildiruvchi n butun soni berilgan n > 0. n = 2**k. k ni
aniqlovchi programma tuzilsin."""


n = int(input("n sonini kiriting: "))
k = 0
current = 1
text = ""

if n <= 0:
    print('0 dan katta son kiriting: ')
else:
    while current < n:
        print(k)
        current += current
        k += 1
    if current == n:
        print(f"{n} ning {k} darajasi")
    else:
        print(f"{n} ning {k} darajasi emas")