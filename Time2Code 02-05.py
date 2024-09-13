# Largest number program

# -------------------------
# Subprograms
# -------------------------
def http_status(status):
    if status == "400":
        return "Bad request"
    elif status == "401" or status == "403":
        return "Authentication error"
    elif status == "404":
        return "Not found"
    else:
        return "Unknown error"


# -------------------------
# Main program
# -------------------------
status = input("Enter an error code:")
print(http_status(status))
