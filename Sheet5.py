# 1. Print Numbers Divisible by Both 3 and 5
n=int(input())
num=1
while num<=n:
    if num%3 ==0 and num%5==0:
        print(num)
    num+=1


# 2. Count Numbers Ending with 5
n=int(input())
num=1
count=0
while num<=n:
    if num%10 ==5:
        count+=1
    num+=1
print(count)


# 3. Sum Numbers Whose Last Digit is Even
n=int(input())
num=1
sum=0
while num<=n:
    digit=num%10
    if digit%2==0:
        sum+=num
    num+=1
print(sum)

# 4. Print Numbers Whose Square is Less Than N
n=int(input())
num=1
while num<=n:
    if (num**2)<n:
        print(num)
    num+=1


# 5. Count Numbers Divisible by 4 but Not by 6
n=int(input())
i=1
count=0
while i<=n:
    if i%4 ==0 and i%6!=0:
        count+=1
    i+=1
print(count)


# 6. Reverse Every Alternate Number
n=int(input())
number=1
nums=[]
while number<=n:
    num=int(input())
    rev=0
    if number%2==0:
        while num>0:
            digit=num%10
            rev=rev*10+digit
            num//=10
        nums+=[rev]
    else:
        nums+=[num]
    number+=1
for number in nums:
    print(number)


# 7. First Number Divisible by Both 7 and 9
n=int(input())
num=1
while num<=n:
    if n%7==0 and n%9==0:
        print(n)
        break
    else:
        n+=1
        continue


# 8. Count Numbers Having More Even Digits Than Odd Digits
n=int(input())
count=0
while n>0:
    num=int(input())
    even_count=0
    odd_count=0
    while num>0:
        digit=num%10
        if digit%2==0:
            even_count+=1
        else:
            odd_count+=1
        num//=10
    if even_count>odd_count:
        count+=1
    n-=1
print(count)


# 9. Print Factors Greater Than 5
n=int(input())
f=1
num=1
while num<=n and f<=n:
    if n%f==0 and f>5:
        print(f)
    num+=1
    f+=1


#10. Sum Until a Negative Number Appears
sum=0
while True:
    n=int(input())
    if n>=0:
        sum+=n
    else:
        print(sum)
        break
