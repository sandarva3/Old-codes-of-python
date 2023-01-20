import re
pattern  = re.compile(r"Nepal \w+")
b = pattern.sub("India", "Nepal is located in SouthAsia")
print(b)

pattern2 = re.compile(r"Agent (\w)\w", re.I)
c = pattern2.sub(r"\1****", "Agent name will not be shown because agent name should be secret")
print(c)        