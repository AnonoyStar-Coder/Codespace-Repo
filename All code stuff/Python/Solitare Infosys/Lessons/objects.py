class classname:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def display(self):
        print(self.a)
        
obj = classname(10,20)
obj.display()

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

def display(a,b):
    print(a)
    print(b)
    
obj = display(10,20)

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

# **OOPS** #

# Types:

# polymorphism
# data incapsulation
# inheritence- single, multiple, multi-label, hybrid, heirarical
# encapsulation

# ------------------------------------------------------------------- #

# Single Inheritence

class parent: # type: ignore
    def talk(): # type: ignore
        print('I can talk')
        
class child(parent): # type: ignore
    def laugh(): # type: ignore
        print('I can laugh')
        
obj = child
obj.talk()
obj.laugh()

# ------------------------------------------------------------------- #

# Multi-level Inheritence

class parent: # type: ignore
    def talk(): # type: ignore
        print('I can talk')

class child(parent): # type: ignore
    def laugh(): # type: ignore
        print('I can laugh')
        
class grandchild(child): # type: ignore
    def sing(): # type: ignore
        print('I can sing')
        
obj = grandchild
obj.talk()
obj.laugh()
obj.sing()

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

# Multiple Inheritence

class parent1:
    def talk(): # type: ignore
        print('I can talk')
        
class parent2:
    def laugh(): # type: ignore
        print('I can laugh')
        
class child(parent1, parent2):
    def sing(): # type: ignore
        print('I can sing')
        
obj = child
obj.talk()
obj.laugh()
obj.sing()

# ------------------------------------------------------------------- #

# Hierarical Inheritence

class parent: # type: ignore
    def talk(): # type: ignore
        print('I can talk')
        
class child1(parent): # type: ignore
    def laugh(): # type: ignore
        print('I can laugh')
        
class child2(parent): # type: ignore
    def sing(): # type: ignore
        print('I can sing')
        
class grandchild1(child1):
    def dance(): # type: ignore
        print('I can dance')
        
class grandchild2(child1):
    def dance(): # type: ignore
        print('I can dance')
        
class grandchild3(child2):
    def dance(): # type: ignore
        print('I can dance')
        
obj = grandchild1
obj.talk()
obj.laugh()
obj.sing()# type: ignore
obj.dance()

obj = grandchild2
obj.talk()
obj.laugh()
obj.sing() # type: ignore
obj.dance()

obj = grandchild3
obj.talk()
obj.laugh() # type: ignore
obj.sing()
obj.dance()

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

# Hybrid Inheritence

class parent:
    def talk(): # type: ignore
        print('I can talk')
        
class child1(parent):
    def laugh(): # type: ignore
        print('I can laugh')
        
class child2(parent):
    def sing(): # type: ignore
        print('I can sing')
        
class grandchild(child1):
    def dance(): # type: ignore
        print('I can dance')
        
obj = grandchild
obj.talk()
obj.laugh()
obj.sing() # type: ignore
obj.dance()

# ------------------------------------------------------------------- #
# ------------------------------------------------------------------- #

# Encapsulation: The binding of data members, methods and member functions in a single unit.

# Other names include: data binding, data wrapping, encapsulation