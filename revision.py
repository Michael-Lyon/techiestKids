# python to accept 10 numbers from a user and print out the avareage of the values

max_numbers = 10
count = 1
total_sum = 0
while count <= max_numbers:
    user_number = int(input("Enter a number: "))
    total_sum += user_number # we add every number we collect from a user to the total_sum
    count += 1

avg = total_sum / max_numbers
print(avg)