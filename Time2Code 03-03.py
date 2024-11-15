# Adder program

# -------------------------
# Subprograms
# -------------------------
def adder():
    total = 0
    top = 0
    bottom = 0
    count = 0
    ave = 0
    complete = False
    while not complete:
        data = input("Enter number: ")
        if data != "e":
            number = float(data)
            total = total + number
            count = count + 1
            # set the highest number
            if number > top:
                top = number
            # set the lowest number
            if count == 1 or number < bottom :
              bottom = number
        else:
            # Prevent a division by zero error
            complete = True
            if count > 0:
                ave = total / count
            else:
                ave = 0
    print("Total:", total, "Top:", top, "Bottom:", bottom, "Ave:", ave)


# -------------------------
# Main program
# -------------------------
adder()
