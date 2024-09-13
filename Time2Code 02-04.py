# States of water program

# -------------------------
# Subprograms
# -------------------------
def water_state(centigrade):
  if centigrade > "100":
    return "gaseous"
  elif centigrade > "0" and centigrade < "100":
    return "liquid"
  elif centigrade < "0" :
    return "solid"
    
    


# -------------------------
# Main program
# -------------------------

centigrade = input("Enter the temperature in °C:")

state = water_state(centigrade)
print("The water is in a", state, "state.")
