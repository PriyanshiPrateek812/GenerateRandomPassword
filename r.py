import random
import string
pass_len = int(input("Enter the length of your random password: "))
charValues = string.punctuation + string.digits + string.ascii_letters
password=""
for i in range(pass_len):
    password+=random.choice(charValues)

print("Your random generated password is: ", password)

# List comprehension
res = [random.choice(charValues) for i in range(pass_len)]
print(res)
res2 = "".join(random.choice(charValues) for i in range(pass_len))
print(res2)