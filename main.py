# Task 1

# vowels = {"а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"}

# song = list(input().split(' '))

# check = set()

# for i in range(len(song)):
#     k = 0
#     for j in range(len(song[i])):
#         if song[i][j] in vowels:
#             k+=1
#     check.add(k)

# print(song)

# if len(check) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# Task 2

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_columns+1):
#         for j in range(1, num_rows+1):
#             print(operation(i,j), end='\t')
#         print()
            
# op = lambda x, y: x * y
# print(print_operation_table(op))
