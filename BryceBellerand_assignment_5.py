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