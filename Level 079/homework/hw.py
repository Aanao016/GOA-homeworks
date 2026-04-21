# 1
def multi_table(number):
    result = ""   
    for i in range(1, 11):  
        line = str(i) + " * " + str(number) + " = " + str(i * number)
        result = result + line
        
        if i < 10: 
            result = result + "\n"
    
    return result

# 2 ვერ დავწერე არვიცი რატო ვერ გავიგგეე

# 3
def first_non_consecutive(arr):   
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
        
    return None

# 4
def add_length(str_):
    answer = []
    for word in str_.split():
        answer.append(word + ' ' + str(len(word)))
    return answer

# 5
def reverse_list(l):
    return l[::-1]

# 6
def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0

    if human_years == 1:
        cat_years = 15
        dog_years = 15

    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
        
    else:

        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5
        
    return [human_years, cat_years, dog_years]

# 7
def str_count(strng, letter):
    count = 0 
    
    for char in strng:

        if char == letter:
            count = count + 1
            
    return count