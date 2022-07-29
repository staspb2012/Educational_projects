# Use the time module to perform time operations
import datetime as dt


# Range 1 from 2 to 100

# Script start time
start_prog = dt.datetime.now()

prime_number = []

# Go through the given range
for i in range(2, 100):
    # Use j for divisor, range: 2 to previous digit of i to check → i-1,
    # if it's divisible by the number in it, it's not a prime number
    # Use break to exit the current loop and execute the next loop,
    # i.e. continue moving backwards
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # If none of the for statements is passed (no divisible condition),
        # else will be executed
        prime_number.append(i)

print('Range 1 from 2 to 100')

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)

# Script start time
start_prog = dt.datetime.now()

# Go through the given range
numbers2_100 = list(range(2, 100))

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)


# Range 2 from 100 to 500

# Script start time
start_prog = dt.datetime.now()

prime_number = []

# Go through the given range
for i in range(100, 500):
    # Use j for divisor, range: 2 to previous digit of i to check → i-1,
    # if it's divisible by the number in it, it's not a prime number
    # Use break to exit the current loop and execute the next loop,
    # i.e. continue moving backwards
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # If none of the for statements is passed (no divisible condition),
        # else will be executed
        prime_number.append(i)
print('Range 2 from 100 to 500')

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)

# Script start time
start_prog = dt.datetime.now()

# Go through the given range
numbers2_1000 = list(range(100, 500))

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)


# Range 3 from 500 to 1000

# Script start time
start_prog = dt.datetime.now()

prime_number = []

# Go through the given range
for i in range(500, 1000):
    # Use j for divisor, range: 2 to previous digit of i to check → i-1,
    # if it's divisible by the number in it, it's not a prime number
    # Use break to exit the current loop and execute the next loop,
    # i.e. continue moving backwards
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # If none of the for statements is passed (no divisible condition),
        # else will be executed
        prime_number.append(i)

print('Range 3 from 500 to 1000')

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)

# Script start time
start_prog = dt.datetime.now()

# Go through the given range
numbers2_10000 = list(range(500, 1000))

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)


# Range 4 from 1000 to 5000

# Script start time
start_prog = dt.datetime.now()

prime_number = []

# Go through the given range
for i in range(1000, 5000):
    # Use j for divisor, range: 2 to previous digit of i to check → i-1,
    # if it's divisible by the number in it, it's not a prime number
    # Use break to exit the current loop and execute the next loop,
    # i.e. continue moving backwards
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # If none of the for statements is passed (no divisible condition),
        # else will be executed
        prime_number.append(i)

print('Range 4 from 1000 to 5000')

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)

# Script start time
start_prog = dt.datetime.now()

# Go through the given range
numbers2_100000 = list(range(1000, 5000))

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)


# Range 5000 from 2 to 10000

# Script start time
start_prog = dt.datetime.now()

prime_number = []
# Go through the given range
for i in range(5000, 10000):
    # Use j for divisor, range: 2 to previous digit of i to check → i-1,
    # if it's divisible by the number in it, it's not a prime number
    # Use break to exit the current loop and execute the next loop,
    # i.e. continue moving backwards
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # If none of the for statements is passed (no divisible condition)
        # , else will be executed
        prime_number.append(i)

print('Range 5 from 5000 to 10000')

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)

# Script start time
start_prog = dt.datetime.now()

# Go through the given range
numbers2_1000000 = list(range(5000, 10000))

# Script end time
end_prog = dt.datetime.now()

# Subtract start and end time of script execution
print(end_prog - start_prog)
