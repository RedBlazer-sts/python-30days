text = "racecar"
letter_counter = 0
vowel_counter = 0
uppercase_count=0
lowercase_count=0
word_count=0
digit_count=0
for char in text:
    letter_counter += 1
    if char in "aeiouAEIOU":
        vowel_counter += 1
    if ord(char)>= 65 and ord(char) <= 90:
        uppercase_count += 1
    elif ord(char) >= 97 and ord(char) <= 122:
        lowercase_count += 1
    elif ord(char)>=48 and ord(char)<= 54:
        digit_count += 1
   

for char in text:
    if char == " ":
        word_count += 1
word_count+=1
# known bug: multiple spaces between words inflates word count - fix later with .split()

reverse_text = ""
for i in range(1,letter_counter + 1):
    reverse_text += text[-i]

consonent=letter_counter - vowel_counter

if letter_counter == 0 :
    case="NO INPUT"
elif uppercase_count == letter_counter:
    case="UPPERCASE"
elif lowercase_count == letter_counter:
    case = "lowercase"
else:
    case= "mixed"

if letter_counter == 0:
    palindrome_checker = "NO input"
elif reverse_text == text :
    palindrome_checker = "Palindrome"
else :
    palindrome_checker = "not a palindrome"

max_count=0
max=""
for char in text :
    count = 0
    for i in range(letter_counter):
        if char == text[i] : count += 1
    
    if count > max_count :
        max_count = count
        max = char

special_count = letter_counter - uppercase_count - lowercase_count - digit_count

seen = ""
for char in text :
    if char not in seen:
        seen += char
  
for unique_char in seen:
    count = 0
    for i in range(letter_counter):
        if unique_char == text[i] : count +=1
    print(f"{unique_char} = {count}")

print(f"Text: {text}\ntotal words:{word_count} Letter Count : {letter_counter}\n Vowel count : {vowel_counter}\n Consonents : {consonent}\n Case : {case}\n palindrome : {palindrome_checker}")
print(f"Most frequent: {max} appears {max_count} times")
print(f"special:{special_count}\n {seen}")