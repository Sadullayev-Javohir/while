"""N va K butun musbat sonlari berilgan. Faqat ayirish va qo'shish amallarini ishlatib
N sonini K soniga bo'lgandagi qoldiq va butun qismini aniqlovchi programma tuzilsin"""

N = int(input("N sonini kiriting: "))
K = int(input("K sonini kiriting: "))

counter = 0
balance = N

while balance >= K:
    balance -= K
    counter += 1
    
print(f"Qoldiq: {balance}")
print(f"Butun qismi: {counter}")