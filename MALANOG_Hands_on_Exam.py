def main():
    
    print("""
****************************
| Number System Conversion |
****************************
By: Aubrey Malanog
""")

    i1 = int(input("Enter a number: "))
    
    print("""
\b********************************************
[1] Decimal Number to Binary Number
[2] Decimal Number to Octal Number
[3] Decimal Number to Hexadecimal Number
********************************************
""")

    i2 = input("How do you want to convert 5? Enter from [1-3]: ")

    if i2 == '1':
        # Convert to Binary
        print(f"""
************************************************
Decimal {i1} Converted to Binary Number is {dbin(i1)}
************************************************""")
    
    elif i2 == '2':
        # Convert to Octal
        print(f"""
************************************************
Decimal {i1} Converted to Octal Number is {doct(i1)}
************************************************""")
    
    elif i2 == '3':
        # Convert to Hexadecimal
        print(f"""
************************************************
Decimal {i1} Converted to Hexadecimal Number is {dhex(i1)}
************************************************""")

    else:
        print("\nInvalid input. Please try again.")
        main()
    
def dbin(b):
    return bin(b).strip('0b')

def doct(o):
    return oct(o).strip('0o')

def dhex(h):
    return hex(h).strip('0x').upper()
    
main()
