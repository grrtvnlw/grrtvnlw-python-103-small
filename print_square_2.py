# print a square of * characters based on user input
# set counter variable
counter = 0

# ask user for dimensions and convert input to int
size = int(input("How big is the square? "))

# Logic
while counter < size:
    print("*" * size)
    counter += 1