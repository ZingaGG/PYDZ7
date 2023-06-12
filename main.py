# Task 1

vowels = {"а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"}

song = list(input().split(' '))

check = set()

for i in range(len(song)):
    k = 0
    for j in range(len(song[i])):
        if song[i][j] in vowels:
            k+=1
    check.add(k)

print(song)

if len(check) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")

