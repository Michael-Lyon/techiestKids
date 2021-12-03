

# A PROGRAM TO ACCEPT THE LENGHT AND BREADTH OF A RECTANGLE AND CHECK IF IT MIGHT BE A SQUARE

lenght = float(input("Enter the lenght: "))
breadth = float(input("Enter the breadth: "))

if lenght == breadth:
    print("This is a square")
else:
    print("This is a rectangle")