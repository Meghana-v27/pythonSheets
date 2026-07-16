# 1. Print Numbers from 1 to N
# Definition: Loops allow a program to repeat the same task multiple times.
# Task: Read a number N and print all numbers from 1 to N using a loop.
# Example Input: N = 5
# Example Output: 1 2 3 4 5
Num=int(input("Enter N value: "))
n=1
while n<=Num:
    print(n,end=" ")
    n+=1

# 2. Print Numbers from N to 1
# Definition: Reverse counting is useful in many programming problems.
# Task: Read a number N and print numbers from N to 1 using a loop.
# Example Input: N = 5
# Example Output: 5 4 3 2 1
N=5
while N>0:
    print(N,end=" ")
    N-=1

# 3. Sum of First N Natural Numbers
# Definition: Natural numbers start from 1.
# Task: Find the sum of numbers from 1 to N using a loop.
# Example Input: N = 5
# Example Output: 15
N=5
sum=0
while N>0:
    sum+=N
    N-=1
print(sum)

# 4. Factorial of a Number
# Definition: The factorial of a number is the product of all positive integers from 1 to that number.
# Task: Calculate the factorial using a loop.
# Example Input: N = 5
# Example Output: 120
N=5
fact=1
while N>0:
    fact=fact*N
    N-=1
print(fact)

# 5. Multiplication Table
# Definition: A multiplication table shows the multiples of a number.
# Task: Print the multiplication table of a given number up to 10.
# Example Input: N = 3
# Example Output: 3 x 1 = 3 ... 3 x 10 = 30
N=3
i=1
while i<=10:
    print(f'{N} X {i} = {N*i}')
    i+=1

# 6. Count Digits
# Definition: Every number contains one or more digits.
# Task: Count the total number of digits using a loop.
# Example Input: 45892
# Example Output: 5
Num=45892
digit_count=0
while Num>0:
    digit_count+=1
    Num//=10
print(digit_count)


# 7. Reverse a Number
# Definition: Reversing digits is a common number problem.
# Task: Reverse the given number using a loop.
# Example Input: 1234
# Example Output: 4321
Num=1234
RevNum=0
while Num>0:
    digit=Num%10
    RevNum=RevNum*10+digit
    Num//=10
print(RevNum)

# 8. Sum of Digits
# Definition: Add all digits present in the number.
# Task: Calculate the sum of digits using a loop.
# Example Input: 572
# Example Output: 14
Num=572
sum=0
while Num>0:
    digit=Num%10
    sum+=digit
    Num//=10
print(sum)


# 9. Product of Digits
# Definition: Multiply all digits present in the number.
# Task: Calculate the product of digits using a loop.
# Example Input: 572
# Example Output: 70
Num=572
product=1
while Num>0:
    digit=Num%10
    product*=digit
    Num//=10
print(product)


# 10. Count Even and Odd Digits
# Definition: Separate digits based on whether they are even or odd.
# Task: Count even digits and odd digits using a loop.
# Example Input: 583920
# Example Output: Even Digits = 3 Odd Digits = 3
Num=583920
even,odd=0,0
while Num>0:
    digit=Num%10
    if digit%2==1:
        odd+=1
    else:
        even+=1
    Num//=10
print(f'Even Digits = {even} Odd Digits = {odd}')
