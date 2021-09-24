# generator is a type of iterator
# instead of using next() you have to use yield to access the next value

nameList = ['Adam', 'Bob', 'Ron', 'Jack', 'Oliver', 'Tom', 'Alan', 'Jemmy', 'Carl', 'Robert']


def next_obj_gen(n):
    count = 0
    while count < len(n):
        yield count
        count = count + 1


for temp in next_obj_gen(nameList):
    print(nameList[temp])
