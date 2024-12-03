inp = 5

for i in range(1,inp+1):
    for j in range(1,i+1):
        print(inp - (i-1), end=" ")
        

# o/p: 544333222211111
        

for i in range(5):
    x="* "
    x=x*i
    print(x)

print("")
for i in range(5):
    x="* "
    x=x*(5-i)
    print(x)
    

def print_number_triangle(rows):
    current_number = 1
    for i in range(1, rows + 1):
        num = current_number
        for j in range(1, i + 1):
            print(num, end=" ")
            # print(num,rows,j)
            num += rows - j
        current_number += 1
        print()


rows = 5  # Define the number of rows for the number triangle
print_number_triangle(rows)

def print_number_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

rows = int(input("Enter the number of rows for the number triangle: "))
print_number_triangle(rows)


def print_pattern(n):
    for i in range(n):
        # Print leading spaces
        for j in range(i):
            print(" ", end="")
        
        # Print stars
        for j in range(2 * (n - i) - 1):
            print("*", end="")
        
        # Move to the next line
        print()

# Define the number of rows
rows = 6

# Call the function to print the pattern
print_pattern(rows)



def print_star_pyramid(n):
    for i in range(n):
        # Printing spaces
        for j in range(n - i - 1):
            print(' ', end='')
        # Printing stars
        for k in range(2 * i + 1):
            print('*', end='')
        # Move to the next line
        print()

# Example usage:
n = 5

print_star_pyramid(n)
