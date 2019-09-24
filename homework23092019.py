# 1 task

s = input('Write something:')
a = int(len(s)/2-1)
b = int(len(s)/2+2)
cut_s = s[a:b]
if len(s) < 7:
    print('Error')
else:
    print(cut_s)

# 2 task

sent = str(input('Write a sentence:'))
word = input('Write a word')
print(sent.count(word))

# 3 task

num1 = input('Write a number')
def is_palendrome(num1):
    return num1 == num1[::-1]
print(is_palendrome(num1))

# 4 task 

message = input('Write someting:')
num = int(input('What to delete?'))
new_message = message.replace(message[num],'')
print(new_message)

# 5 task

num1 = int(input('Write a first number:'))
num2 = int(input('Write a second number:'))
sum = num1 + num2
if num2 == 10 or num1 == 10:
    print('True')
elif sum == 10:
    print('True')
else:
    print('False')
