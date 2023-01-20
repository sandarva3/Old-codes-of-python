import pyinputplus as pyip
while True:
  text = "Do you want to know how to make an idiot busy for hours ? "
  response = pyip.inputYesNo(text)
  if response == "no":
      print("The idiot is quite clever !")
      break