# 1. Find the Largest of N Numbers
n=int(input())
largest=0
while n>=0:
    num=int(input())
    if num>largest:
        largest=num
    n-=1
print(f'Largest = {largest}')

# 2. Find the Smallest of N Numbers
n=int(input())
smallest=999
while n>0:
    num=int(input())
    if num<smallest:
        smallest=num
    n-=1
print(f"Smallest = {smallest}")


# 3. Find the Second Largest Number
n=int(input())
largest=0
second_largest=0
while n>0:
    num=int(input())
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
    n-=1
print(f'Second Largest = {second_largest}')

# 5. Count Positive, Negative and Zero Values
n=int(input())
positive_c=0
Negative_c=0
zero_c=0
while n>0:
    num=int(input())
    if num>0:
        positive_c+=1
    if num<0:
        Negative_c+=1
    if num ==0:
        zero_c+=1
    n-=1
print(f"Positive = {positive_c}")
print(f'Negative = {Negative_c}')
print(f'Zero = {zero_c}')

# 6. Find the Missing Number
n=int(input())
actual_sum=0
expected_sum=0
count=1
while count<=n:
    expected_sum+=count
    count+=1
count=1
while count<n:
    num=int(input())
    actual_sum+=num
    count+=1
missing=expected_sum-actual_sum
print(f'Missing Number = {missing}')

# 7. Check Whether a Number is Perfect
num = int(input("Enter a number: "))
count = 1
total = 0
while count < num:
    if num % count == 0:
        total += count
    count += 1
if total == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# 8. Find the GCD of Two Numbers
n1 = int(input())
n2 = int(input())
count = 1
gcd = 1
while count <= n1 and count <= n2:
    if n1 % count == 0 and n2 % count == 0:
        gcd = count
    count += 1
print("GCD:", gcd)

# 10. Power Without Using **
base = int(input("Base ="))
exponent = int(input("Exponent ="))
count = 1
result = 1
while count <= exponent:
    result = result * base
    count+=1
print("Result:",result)
