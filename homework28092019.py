sentence ='Hello! My name is Alla!'
symbol = '!'
print(sentence.replace(symbol,''))


sentence = 'Hello! My name is Alla!'
symbol = '!'
new_sent = []
for item in sentence:
    if item !=  symbol:
        new_sent.append(item)
print(''.join(new_sent))


names = ['John',  'Kate',  'Dave',  'Den', 'Adele']
name =input('Write your name:')
if name not in names:
    print('not found')
elif name == names[2] or name == names[4]:
    print("it's good")
else :
    names.remove(name)
    print(names)


