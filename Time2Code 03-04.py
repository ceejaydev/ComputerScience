# Compound interest program

# -------------------------
# Subprograms
# -------------------------
def compound(balance, interest_rate, target_balance):
  
  year = 1
  interest_rate = interest_rate / 100
  
  while balance < target_balance:
    interest = balance * interest_rate
    balance = int(balance + interest)
    print("Year", year,": Balance £", balance)
    year = year + 1


# -------------------------
# Main program
# -------------------------

balance = int(input("Enter balaance to the nearest pound:"))
interest_rate = float(input("Enter the % interest rate:"))
target_balance = int(input("Enter the target balaance to the nearest pound:"))


compound(balance, interest_rate, target_balance)
