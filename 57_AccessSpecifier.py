# public : can be access outside from 49_ObjectClass
# private(__...):can't be access from outside


class employee:
    def __init__(self):
        self.__name="Kanchan"

a=employee()
# print(a.__name)can not be accessed as it is private
#can be access indirectly as
print(a._employee__name)

#Name Mangling: a technoque used to protect class private and superclass private
#Names of class private and superclass private attributes are transformed by single leading underscore
#And double leading underscore resp.

#Protected :single underscore
#It is just a naming and does not provide any protection or restriction in python 