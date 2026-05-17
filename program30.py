def cube(number):
    return number*number*number

def by_tree(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
print(by_tree(9))
print(by_tree(4))
        