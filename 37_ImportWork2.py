#Or can use repective function as below
#Also we can use THE "as" keyword
from math import sqrt as s
from math import pi
res=s(9)
a=res*pi
print(res)
print(a)

#can be import all  function as from math import *
#But it is not recommended because it makes harder and difficult to understand

#We can import our local program function as
from local import Kanchan, examp

Kanchan()
print(examp)

#Also we can import as 
#from local import *