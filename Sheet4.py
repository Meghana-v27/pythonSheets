num=int(input())
even_count=0
odd_count=0
while num>0:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
    num-=1
print(f'Even Numbers = {even_count}')
print(f'Odd Numbers = {odd_count}')


num=int(input())
sum=0
while num>0:
    if num%3==0:
        sum+=num
    num-=1
print(sum)

start_year=2000
end_year=2020
while start_year<=end_year:
    if (start_year%400==0 or (start_year%4==0 and start_year%100 !=0)):
        print(start_year)
    start_year+=1


num=int(input())
div_5_count=0
div_7_count=0
both_count=0
while num>0:
    if num%5==0:
        div_5_count+=1
    if num%7==0:
        div_7_count+=1
    if (num%5==0 and num%7==0):
        both_count+=1
    num-=1
print(f'5={div_5_count}')
print(f'7={div_7_count}')
print(f'Both={both_count}')



num=int(input())
factors_count=0
i=1
n=num
while num>0 and i<=n: #11>0 and 2=12
    if n%i==0: # 12%1==0 
        print(i,end=" ")  #1 
        factors_count+=1 #1
    num-=1 # 12-1 = 11
    i+=1 # 1 + 1 = 2
print()
print(f"Total Factors = {factors_count}")

num=int(input())
largest=0
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
    num//=10
print(f'Largest Digit = {largest}')


num=int(input())
smallest=9
while num>0:
    digit=num%10
    if digit<smallest:
        smallest=digit
    num//=10
print(f'Smallest Digit = {smallest}')


num=int(input())
greater_5_count=0
while num>0:
    digit=num%10
    if digit>5:
        greater_5_count+=1
    num//=10
print(greater_5_count)


num=int(input())
sum=0
while num>0:
    digit=num%10
    if digit%2==0:
        sum+=digit
    num//=10
print(sum)


num=int(input())
n=1
while n<=num:
    if n%3==0 and n%5!=0:
        print(n,end=" ")
    n+=1
