# here's a simple example demonstrating some of these magic methods:

# python
# Copy code
class MyList:
    def __init__(self, *args):
        self.data = list(args)

    def __repr__(self):
        return f"MyList({self.data})"

    def __str__(self):
        return f"{self.data}"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __del__(self):
        print("MyList instance is about to be destroyed.")

# Create a MyList instance
my_list = MyList(1, 2, 3, 4, 5)

# Test magic methods
print("Using __repr__:", repr(my_list))
print("Using __str__:", str(my_list))
print("Using __len__:", len(my_list))
print("Using __getitem__:", my_list[2])
my_list[2] = 10  # Using __setitem__
print("After __setitem__:", my_list)
del my_list[2]  # Using __delitem__
print("After __delitem__:", my_list)

# Destroying MyList instance
del my_list
# In this example:

# We define a MyList class that behaves like a list but with some additional functionality.
# We define __init__ to initialize the list with the provided arguments.
# __repr__, __str__, __len__, __getitem__, __setitem__, and __delitem__ methods are defined to provide string representations, length, indexing, setting items, and deleting items respectively.
# Finally, __del__ method is defined to print a message when the instance is about to be destroyed.
# When you run this code, you'll see how these magic methods are implicitly called in various contexts.