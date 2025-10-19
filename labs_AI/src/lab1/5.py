fio = input("ФИО: ").split()
clean_fio = ' '.join(fio).strip()

initials = ''.join([word[0].upper() for word in fio if word])
length = len(clean_fio)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {length}")