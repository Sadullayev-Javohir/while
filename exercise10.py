"""n natural soni berilgan. 3**k <= n shartni qanoatlantiruvchi eng kichik butun k
sonini aniqlovchi programma tuzilsin."""

n = int(input("n sonini kiriting: "))
k = 0
if n > 0:
    while 3 ** (k + 1) <= n:
        k += 1
    print(k)    
else:
    print("0 dan katta son kiriting: ")