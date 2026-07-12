class fruit:
    taste = 'sweet'

    def __init__(self,name,color):
     self.name = name
     self.color = color

    
apple = fruit('Apple','red')
banana = fruit('Banana','Yellow')

print(apple.taste)
print(apple.name,apple.color)
print(banana.name,banana.color)
     
    