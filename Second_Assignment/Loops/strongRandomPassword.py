from nine import random_password,check
count = 0


while True:
    generated_password = random_password()
    count = count + 1
    if check(generated_password):
        break
print(f"The generated password is {generated_password} with count of {count}")




