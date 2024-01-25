picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for num in picture:
    for pixel in num:
        if pixel == 0:
            print(" ", end="")
        elif pixel == 1:
            print("*", end="")
    print("")