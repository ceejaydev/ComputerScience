# Currency converter program

# -------------------------
# Subprograms
# -------------------------
def exchange(gbp, currency):
  if currency == "USD" or "usd"  :
    money = gbp * 1.3
    return money
  elif currency == "Euro" or "euro" :
    money = gbp * 1.11
    return money
  elif currency == "Yuan" or "yaun" :
    money = gbp * 8.92 
    return money
  elif currency == "Yen" or "yen" :
    money = gbp * 138.44
    return money 
  else:
    print("invalid")


# -------------------------
# Main program
# -------------------------

gbp = int(input("Enter the number of Great British Pounds:"))
currency = input("Enter the currency (USD, Euro , Yuan, Yen )")

money = exchange(gbp, currency)
print(gbp, "GBP =", money, currency)
