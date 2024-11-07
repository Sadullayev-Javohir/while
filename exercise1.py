"""A va B butun musbat son berilgan A > B. A uzunlikdagi kesmada maksimal darajada B kesma
joylashtirilgan. A kesmaning bo'sh qismini aniqlovchi programma tuzilsin. Ko'paytirish va 
bo'lish amallarini ishlatmasdan."""

A = int(input("A uzunlikni kiriting: "))
B = int(input("B uzunlikni kiriting: "))

balance = A
counter = 0
    
while balance >= B:
    balance -= B
    counter += 1
    
print(f"Kesmaning bo'sh joyi {balance}")
print(f"Kesmalar soni {counter}")