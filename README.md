# UDSM_AI_Second_session


## A Simple course examples for python classes & QABot for demonstration


# main class of the project (DOG)
```python
class Dog:

    def __init__(self, name):
        """
        class constructor

        Parameters
        ----------
        name : str
            The name of the dog
        """
        self.name = name  # public attribute
        self.__age = 20  # private attribute

    def bark(self):
        """
        Class method describing the behavior of the dog (class)
        """
        print("Woof 🐶🐶!")

    def get_age(self):
        """
        Class method to get the age of the dog
        Because the age of the dog is private, we need a method to get it
        """
        return self.__age

    def set_age(self, age):
        """
        Class method to set the age of the dog
        Because the age of the dog is private, we need a method to set it
        """
        self.__age = age

    def __str__(self):
        """
        Class method to get the name of the dog
        it is invoked when we print the object withouth calling the name attribute or a specific method
        """
        return self.name
```

# demonstrating class inheritance
```python

class Puppy(Dog):
    pass


class Fox(Dog):
    def bark(self):
        print("Ring-ding-ding-ding-dingeringeding 🐺🐺🐺!")

```

# creating a dog object```python

greek_hound = Dog("Greek Hound")

# print dog name (public attribute)
```python
print("public Dog Name: ", greek_hound.name)
```

# calling the bark method of the dog object
```python
greek_hound.bark()
```

# print dog age (private attribute)
```python
print("Private Dog Age: ", greek_hound.get_age())
```

# set dog age (private attribute)
```python
greek_hound.set_age(3)
```

# get the updated dog age
```python
print("Updated Dog Age: ", greek_hound.get_age())
```

# updating dog age publicly
```python
greek_hound.__age = 4  # this will not change the age of the dog
print("Failed Attempt to update age: ", greek_hound.get_age())
```

# creating a puppy object
```python
puppy = Puppy("Puppy")
```

# print puppy name (public attribute)
```python
print("public Puppy Name: ", puppy.name)
```

# calling the bark method of the puppy object
```python
puppy.bark()
```

# print puppy age (private attribute)
```python
print("Private Puppy Age: ", puppy.get_age())
```

# set puppy age (private attribute)
```python
puppy.set_age(1)
```

# get the updated puppy age
```python
print("Updated Puppy Age: ", puppy.get_age())
```

# updating puppy age publicly
```python
puppy.__age = 2  # this will not change the age of the puppy
print("Failed Attempt to update age: ", puppy.get_age())
```

# creating a fox object
```python
fox = Fox("Fox")
```

# print fox name (public attribute)
```python
print("public Fox Name: ", fox.name)
```

# calling the bark method of the fox object
```python
fox.bark()
```

# For 🤖 QABot Check the main.py file
## Explore the code

# Credits
## All attedees