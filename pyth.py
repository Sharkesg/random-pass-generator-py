import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

while True:
    pass_size = input("Enter the size of your password: ")
    try:
        char_num = int(pass_size)
        if char_num < 8:
            print("Your password size should be at least 8")
        else:
            break
    except ValueError:
        print("Please enter a valid number")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

p1 = round(char_num * 0.3)
p2 = round(char_num * 0.2)

result = []
for x in range(p1):
    result.append(s1[x])
    result.append(s2[x])
for x in range(p2):
    result.append(s3[x])
    result.append(s4[x])

if len(result) < char_num:
    result.extend(random.choices(s1 + s2 + s3 + s4, k=char_num - len(result)))

random.shuffle(result)
password = "".join(result)
print("Password:", password)









