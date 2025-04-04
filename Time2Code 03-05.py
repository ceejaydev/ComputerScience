# Valid month program

# -------------------------
# Subprograms
# -------------------------
def validate_month(month):
  if month > 0 and month < 13:
    return True
  else:
    return False
    


# -------------------------
# Main program
# -------------------------
valid_month = False
while not valid_month:
  month = int(input("Enter a month 1-12"))
  valid_month = validate_month(month)
print("Thank you. Input accepted.")
