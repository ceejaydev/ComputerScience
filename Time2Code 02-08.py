# Exam grade program

# -------------------------
# Subprograms
# -------------------------
def grade(mark):
  if mark < 3 :
    grade == "U"
    return grade
  elif mark == 2:
    grade == "1"
    return grade
  elif mark < 3 and  mark > 5:
    grade == 2
    return grade
  elif mark > 2 and  mark< 14:
    grade == 3
    return grade 
  elif mark > 13 and  mark< 23:
    grade == 4
    return grade 
  elif mark > 22 and mark < 32:
    grade == 5 
    return grade
  elif mark > 31 and mark < 42:
    grade == 6
    return grade
  elif mark > 41 and mark < 55:
    grade == 7
    return grade 
  elif mark >  54 and mark < 68:
    grade == 8
    return grade
  elif mark > 80:
    grade == "9"
    return grade
  else:
    print("Invalid")
  
  

# -------------------------
# Main program
# -------------------------

mark = int(input("Enter a mark 0-100"))
print("A mark of", mark, "is grade", grade)
