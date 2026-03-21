# 1) შექმენით რიცხვებით სავსე სია, ამ სიიდან იპოვეთ და დაპრინტეთ მეორე ყველაზე დიდი რიცხვი, გამოიყენეთ for ციკლი.

numbers = [10, 5, 8, 20, 15]

max1 = numbers[0]
max2 = numbers[0]

for num in numbers:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num

print("მეორე ყველაზე დიდი რიცხვი არის:", max2)
# ------------------------------------------------------
# 2) მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თუ ამ წინადადებაში რამდენი სიტყვის სიგრძე არის 4-ზე მეტი, დაპრინტეთ ასეთი სიტყვების რაოდენობა, მაგალითად 4. გამოიყენეთ while ციკლი.
# მომხმარებელისგან წინადადების მიღება

sentence = input("შეიყვანეთ წინადადება: ")
words = sentence.split()

count = 0
i = 0

while i < len(words):
    if len(words[i]) > 4:
        count += 1
    i += 1

print("სიტყვების რაოდენობა, რომლის სიგრძე 4-ზე მეტია:", count)
# -------------------------------------------------------
# 3) მომხმარებელს შემოატანინეთ სიტყვა და გაიგეთ ეს სიტყვა არის თუ არა პალინდრომი - ანუ ეს სიტყვა წინიდანაც და უკნიდანაც თუ ზუსტად იგივენაირად იკითხება. თუ კი მაშინ დაპრინტეთ True, თუ არა დაპრინტეთ False, გამოიყენეთ for ციკლი, არ გამოიყენოთ slicing - [::-1].

word = "level"
is_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False
        break

print(is_palindrome)
# -----------------------------------
# 4) შექმენით არეული რიცხვებით სავსე გრძელი სია და 2 ცარიელი სია, ერთ სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, ხოლო მეორე სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, გამოიყენეთ for ციკლი.

import random

numbers = [random.randint(1, 100) for _ in range(20)]

even_index_even_numbers = []  
odd_index_even_numbers = []   

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:  
        if i % 2 == 0:
            even_index_even_numbers.append(numbers[i])
        else:
            odd_index_even_numbers.append(numbers[i])

print("მთავარი სია:", numbers)
print("ლუწი რიცხვები ლუწ ინდექსებზე:", even_index_even_numbers)
print("ლუწი რიცხვები კენტ ინდექსებზე:", odd_index_even_numbers)

# 5) შექმენით ყველანაირი მონაცემთა ტიპების ელემენტებით სავსე სია, ამოშალეთ ყველა დუპლიკატები - ყველაფერი რაც მეორდება 2-ზე მეტჯერ, გამოიყენეთ remove() ფუნქცია და while ციკლი.

my_list = [1, 2, 2, 3, 3, 3, "hello", "hello", "world", True, True, False, 2.5, 2.5, 2.5]

print("მთავარი სია:", my_list)

i = 0
while i < len(my_list):
    element = my_list[i]  


    if my_list.count(element) > 2:
      
        while element in my_list:
            my_list.remove(element)
    else:
       
        i += 1

print("სია დუპლიკატების წაშლის შემდეგ:", my_list)


# 6)  მომხმარებელს შემოატანინეთ წინადადება და დაპრინტეთ ამ წინადადებაში მყოფი ყველაზე გრძელი სიტყვა, გამოიყენეთ while ციკლი, არ გამოიყენოთ max() ფუნქცია.

sentence = input("შეიყვანეთ წინადადება: ")
words = sentence.split()

i = 0
longest_word = "" 

while i < len(words):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]  
    i += 1  

print("ყველაზე გრძელი სიტყვა:", longest_word)

# 