# # 1. diamond pattern

# rows = int(input("Enter the number of rows for the diamond: "))

# # Top half of the diamond
# for i in range(1, rows + 1):
#     print(" " * (rows - i), end="")
#     print("*" * (2 * i - 1))

# # Bottom half of the diamond
# for i in range(rows - 1, 0, -1):
#     print(" " * (rows - i), end="")
#     print("*" * (2 * i - 1))


# # 2. right half pyramid

# rows = int(input("Enter the number of rows for the right half pyramid: "))

# for i in range(1, rows + 1):
#     print("*" * i)

# # 3. lefy half pyramid

# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows + 1):
#     # Print leading spaces
#     for j in range(rows - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(i):
#         print("*", end="")

#     # Move to the next line
#     print()

# # 4. full pyramid

# def print_full_pyramid(n):
#     for i in range(n):
#         # Print leading spaces
#         for j in range(n - i - 1):
#             print(" ", end="")
        
#         # Print stars
#         for k in range(2 * i + 1):
#             print("*", end="")
        
#         # Move to the next line
#         print()

# # Number of rows in the pyramid
# n = 5
# print_full_pyramid(n)

# 5. inverted right half pyramid

rows = int(input("Enter the number of rows for the right half pyramid: "))

for i in range(rows,0,-1):
    print("*" * i)

# 6. inverted left half

rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):
    # Print stars
    for j in range(i):
        print("*", end="")
    
    # Move to the next line
    print()

# 7.full inverted

n = 5

for i in range(n - 1, -1, -1):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line
    print()

# 8. hallow square 

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 9. hallow trinagle

rows = int(input("Enter the number of rows: "))

# Print upper triangle
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Print lower triangle
for i in range(rows - 2, -1, -1):
    for j in range(rows - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 10. hallow diamond

# Define the size of the diamond
size = 7

# Upper half of the diamond
for i in range(size):
    for j in range(size - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half of the diamond
for i in range(size - 2, -1, -1):
    for j in range(size - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 11. hollow parallelogram

# Define the height and width of the parallelogram
height = 6
width = 10

# Loop through each row
for i in range(height):
    # Print spaces for indentation
    for j in range(height - i - 1):
        print(" ", end="")
    
    # Print '*' for the first and last row
    # For other rows, print '*' only for the first and last column
    for j in range(width):
        if i == 0 or i == height - 1 or j == 0 or j == width - 1:
            print("*", end="")
        else:
            print(" ", end="")
    
    # Move to the next line after printing each row
    print()
#

# 12. parallelogram

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(1, i):
        print(" ", end="")
    
    # Print stars
    for k in range(1, cols + 1):
        print("*", end="")
    
    print()

# 13. hourglass 

def print_hourglass_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(2, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = 5  # Change the value of n for different sizes of the hourglass
print_hourglass_pattern(n)


# 14. hallow hourglass

def print_hollow_hourglass_pattern(size):
    # Upper half of hourglass
    for i in range(size, 0, -1):
        for j in range(size - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower half of hourglass
    for i in range(2, size + 1):
        for j in range(size - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            if j == 0 or j == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Size of the hourglass pattern
size = 5

# Print the hollow hourglass pattern
print_hollow_hourglass_pattern(size)
