import re

pattern= "is "
text= '''The Beulé Gate is a fortified 
gate leading to the Propylaia of the Acropolis 
of Athens, Greece. It was constructed largely
of repurposed material taken from the 4th-century BCE
Choragic Monument of Nikias and integrated into the Post-Herulian Wall,
a late Roman fortification built around the Acropolis in the years following 
the city's sack by the Germanic Heruli people in 267 or early 268 CE. Its 
construction marked the beginning of a new phase in the Acropolis's use, 
in which it came to be seen more as a defensive position than a religious
sanctuary. During the medieval period, the gate was further fortified, before being built
over with a bastion in Ottoman times. The monument was discovered by the French archaeologist Charles Ernest 
Beulé on 29 May 1852, and excavated in 1852 and 1853. Archaeologists and Greek commentators criticised
the aggressive excavation
– particularly the use of explosives. In modern times, the gate has served primarily 
as an exit for tourists from the Acropolis. '''

match=re.finditer(pattern,text)
for m in match:
  print(m)