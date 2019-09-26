test = 'test1, test2, test3, test4, test5'
index = int(input('Type a number:'))
test2 = test.split(', ')
del test2[index-1]
test3 = ', '.join(test2)
print(test3)

str = 'test1, test2, test3, test4, test5'
index = int(input('Type a number:'))
todel = f'test{index}, '
print(str.replace(todel,''))

# 2 task
url = input('Put the URL:')
dom = url.split('/')
print(dom[2])
