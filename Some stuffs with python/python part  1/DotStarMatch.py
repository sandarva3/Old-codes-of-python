#Greedy mode 
import re
pattern = re.compile(r"<.*>")
text = "<This is the greedy mode> So this may also be printed>"
greedy = pattern.search(text)
# output1 = output.group(1)
# output2 = output.group(2)

print(greedy.group())

#Non greedy mode
#In non greedy mode we should also use '?' after '*'
pattern2 = re.compile(r"<.*?>")
text2 = "<It is the non greedy mode> So this may not be printed>"
non_greedy = pattern2.search(text2)
print(non_greedy.group())
