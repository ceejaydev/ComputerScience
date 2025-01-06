names = ["taylor", "shayaan", "kevin", "eden", "diptan"]
name_to_find = input("Enter the name you are searching for: ")

found = False
index = 0 

while found == False and index < len(names):
  if names[index] == name_to_find:
    found = True
  else:
    index = index + 1
    
if found == True:
  print("Name is in the list")
else:
  print("Name is not in the list")
