"""n natural soni berilgan (n > 1). (1 + 2 + 3 + ... + k) >= n shart bajariladigan
eng kichik k sonini aniqlovchi programma tuzilsin. 1 dan k gacha bo'lgan yig'indi
ham ekranga chiqarilsin."""

n = int(input("n sonini kiriting: "))

add = 0
k = 0

if n > 1:
    while add <= n:
        print(k)
        k += 1
        add += k
    print(f"Eng kichik k: {k}")
else:
    print("1 dan katta son kiriting: ")