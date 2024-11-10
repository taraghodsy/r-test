class Book :
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def  full_name(self):
       return f'{self.name}\n{self.price}'
    

class ChildrenBook (Book):
    def __init__(self,name,price,title):
        Book.__init__(self,name,price)
        self.title=title
    def full_name(self):
         return f'{self.name}\n{self.price}\n{self.title}'
        
    

class AdultsBook (Book):
    def __init__(self,name,price,genre):
        Book.__init__(self,name,price)
        self.genre=genre
    def full_name(self):
         return f'{self.name}\n{self.price}\n{self.genre}'
        
        
           
childrenBook= ChildrenBook("anesherli",345,"kodakaneh") 
adultsBook= AdultsBook("bof kor",200,"adabiat modern") 



print(childrenBook.full_name())
print(f'name:{childrenBook.name}price:{childrenBook.price}')


print(adultsBook.full_name())
print(f'name:{adultsBook.name}price:{adultsBook.price}')




    





        
        


      
