# Get the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Ensure the start number is even
if start % 2 != 0:
    start += 1

# Display the range of numbers with a difference of two
print(f"Numbers with a difference of two from {start} to {end}:")
for num in range(start, end + 1, 2):
    print(num)
