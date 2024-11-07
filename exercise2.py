"""A va B butun musbat sonlar berilgan. A > B. A uzunlikdagi kesmada B kesmadan nechta
joylashtirish mumkinligini aniqlovchi programma tuzilsin. Ko'paytirish va bo'lish amallarini
ishlatmang."""

A = int(input("A kesma uzunligini kiriting: "))
B = int(input("B kesma uzunligini kiriting: "))
count = 0
length = A
while length >= B:
    count += 1
    length -= B
print(f"Kesmalar soni {count}")