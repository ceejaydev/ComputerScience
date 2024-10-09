# Periodic table program

# -------------------------
# Subprograms
# -------------------------
def periodic_table(name):
  if name == "Li" or name == "Lithium" :
    print("Symbol is Li")
    print("Name is Lithium")
    print("Atomtic weight is 6.94")
    print("Lithim (Li) is an Alkali metal")
  elif name == "Na" or name == "Sodium" :
    print("Symbol is Na")
    print("Name is Sodium")
    print("Atomtic weight is 22.99")
    print("Sodium(Na) is an Alkali metal")
  elif name == "K" or name == "Potassium" :
    print("Symbol is K")
    print("Name is Lithium")
    print("Atomtic weight is 39.098")
    print("Potassium(K) is an Alkali metal")
  elif name == "F" or name == "Fluorine" :
    print("Symbol is F")
    print("Name is Fluorine")
    print("Atomtic weight is 18.998")
    print("Fluorine (F) is an Halogen")
  elif name == "Cl" or name == "Chlorine" :
    print("Symbol is Cl")
    print("Name is Chlorine")
    print("Atomtic weight is 34.45")
    print("Chlorine (Cl) is a Halogen")
  elif name == "Br" or name == "Bromine" :
    print("Symbol is Br")
    print("Name is Bromine")
    print("Atomtic weight is 79.904")
    print("Bromine(Br) is a Halogen")
  else:
    print("Element is not the catalouge")
      

    
  
              


# -------------------------
# Main program
# -------------------------
name = input("Enter the symbol or name of an elememnt")
periodic_table(name)
