#1. Count Numbers Whose Last Digit is Greater Than First Digit
n=int(input())
count=0
while n>0:
    num=int(input())
    last_digit=num%10
    while num>10:
        num//=10
    if last_digit>num:
        count+=1  
    n-=1
print(count)


#2. Print Common Factors of Two Numbers
n1=int(input())
n2=int(input())
if n1<n2:
    for i in range(1,n1):
        if n1%i==0 and n2%i==0:
            print(i)


#3. Count Numbers Having Exactly Three Digits
n=int(input())
count=0
while n>0:
    num=int(input())
    digit_count=0
    while num>0:
        digit_count+=1
        num//=10
    if digit_count==3:
        count+=1
    n-=1
print(count)

#4. Print Numbers Whose Digit Sum is Even
n=int(input())
for i in range(1,n+1):
    digit_sum=0
    temp=i
    while i>0:
        digit=i%10
        digit_sum+=digit
        i//=10
    if digit_sum%2==0:
        print(temp)
    n-=1


#5. Count Factors That Are Even
n=int(input())
count=0
for i in range(1,n+1): 
    if n%i==0 and i%2==0: 
        count+=1
print(count)


#6. Reverse Only Even Numbers
n=int(input())
for i in range(1,n+1):
    num=int(input())
    if num%2==0:
        rev=0
        while num>0:
            digit=num%10
            rev=rev*10+digit
            num//=10
        print(rev)
    else:
        print(num)
    n-=1


#7. Find the Smallest Multiple of 7 Greater Than N
n=int(input())
for i in range(n+1,9999):
    if i%7==0:
        print(i)
        break


#8. Count Numbers Having Equal Even and Odd Digits
n=int(input())
count=0
while n>0:
    even_count,odd_count=0,0
    num=int(input())
    while num>0:
        digit=num%10
        if digit%2==0:
            even_count+=1
        else:
            odd_count+=1
        num//=10
    if even_count==odd_count:
        count+=1
    n-=1
print(count)



# 9. Print Factors Between 5 and 20
n=int(input())
for i in range(1,n):
    if n%i==0 and 5<=i<=20:
        print(i)




#10. Read Numbers Until Their Sum Exceeds 100
sum=0
while sum<=100:
    n=int(input())
    sum+=n
print(sum)
