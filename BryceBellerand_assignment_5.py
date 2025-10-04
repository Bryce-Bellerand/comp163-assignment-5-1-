print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: Sequence: "))
step_count = 0
prime_number = False

while current_number != 1:
    print(current_number, end=" ")
    if current_number % 2 == 0:
        current_number //= 2
    else:
        current_number = current_number * 3 + 1
    step_count += 1
if step_count == 1:
    print(current_number, end=" ")
else:
    print(current_number)

print(f"Steps: {step_count}")
print("=== Challenge 2: Prime Number Checker ===")
prime_user = int(input())
print(f"Enter a number: Testing divisors from 2 to {prime_user - 1}...")

for i in range(2,17): 
    if prime_user % i == 0:
        prime_number = False
        break
    else:
        prime_number = True
if prime_user == 1 or prime_user == 2:
    prime_number = True

if prime_number == True:
    print(f"{prime_user} is prime!")
else:
    print(f"{prime_user} is not prime (divisible by {i})")

    print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

# print header row
print("    ", end="")  # empty top-left corner
for j in range(1, 11):
    print(j, end="     ")
print()
for i in range(1, 11):
    print(f"{i}", end="    ")  # row label
    for j in range(1, 11):
        print(f"{i*j}", end="    ")
    print()