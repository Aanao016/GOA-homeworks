def spin_words(sentence):
    words = sentence.split()
    result = []
    
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
            
    return " ".join(result)


def capitalize(s):
    even_cap = "" 
    odd_cap = ""
    
    for i, char in enumerate(s):
        if i % 2 == 0:
            even_cap += char.upper()
            odd_cap += char.lower()
        else:
            even_cap += char.lower()
            odd_cap += char.upper()
            
    return [even_cap, odd_cap]

def reverse_words(str):
  #go for it
  newStr = []
  for i in str.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)


def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    indices = []
    
    for i, char in enumerate(word):
        if char in vowels:
            indices.append(i + 1)
            
    return indices



# 5 ვერ გავაკეთე


def solution(digits):
    max_num = 0

    for i in range(len(digits) - 4):
        current_num = int(digits[i : i+5])

        if current_num > max_num:
            max_num = current_num
            
    return max_num