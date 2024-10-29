def kilo_to_pounds(kilos):
    # Use the precise conversion factor
    return kilos * 2.20462

# Main part of the program starts here. Do not remove the line below.
if __name__ == '__main__':
    kilos = float(input())
    
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')
