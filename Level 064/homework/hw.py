# 1
def greet(name):
    return f"გამარჯობა, {name}!"

print(greet("Ana"))
print(greet("Giorgi"))
print(greet("Nika"))


# 2
def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers(3, 5))
print(sum_numbers(10, 20))
print(sum_numbers(-2, 7))


# 3
def square(num):
    return num ** 2

print(square(2))
print(square(5))
print(square(10))


# 4
def check_age(age):
    if age >= 18:
        return "სრულწლოვანი ხარ"
    else:
        return "არ ხარ სრულწლოვანი"

print(check_age(20))
print(check_age(16))
print(check_age(18))


# 5
def string_length(text):
    print(len(text))

string_length("Python")
string_length("გამარჯობა")
string_length("Hello World")


# 6
def nums(num1,num2):
    return num1*num2
print(nums(2,4))



# 7
def check_score(score):
    if score >= 90:
        return "შესანიშნავი ქულა"
    elif score >= 70 and score <= 89:
        return "კარგი ქულა"
    elif score >= 50 and score <= 69:
        return "დამაკმაყოფილებელი ქულა"
    else:
        return "ჩაჭრილი"

print(check_score(95))
print(check_score(75))
print(check_score(55))
print(check_score(30))


# 8
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_or_odd(4))
print(even_or_odd(7))
print(even_or_odd(10))


# 9
def first_letter(name):
    return name[0]

print(first_letter("Giorgi"))
print(first_letter("Ana"))
print(first_letter("Nika"))


# 10)
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average(3, 6, 9))
print(average(10, 20, 30))
print(average(5, 7, 8))