# Nitrate program

# -------------------------
# Subprograms
# -------------------------
def calculate_dose(nitrate):
  if nitrate > 10 :
    carbon_dose = 3
    return carbon_dose
  elif nitrate > 2.5 :
    carbon_dose = 2
    return carbon_dose
  elif nitrate > 1  :
    carbon_dose =  1
    return carbon_dose
  elif nitrate > 0.5 :
    carbon_dose = 0.5
    return carbon_dose
  else:
    print("invalid")



# -------------------------
# Main program
# -------------------------

nitrate = float(input("Enter the nitrate level from the test:"))
carbon_dose = calculate_dose(nitrate)
print("For", nitrate, "nitrate dose", carbon_dose, "ml of carbon.")
