# 1. Count Frequency of Each Character
# str=input()
# d={}
# for ch in str:
#     if ch not in d:
#         d[ch]=1
#     else:
#         d[ch]+=1
# for key,val in d.items():
#     print(f'{key}:{val}')


# 2. Find the First Repeating Character
# str=input()
# d={}
# for ch in str:
#     if ch not in d:
#         d[ch]=1
#     else:
#         d[ch]+=1
# for key,val in d.items():
#     if val>1:
#         print(key)
#         break



# 3. Group Students by Grade
# n=int(input())
# d={}
# for i in range(n):
#     name,grade=input().split()
#     if grade not in d:
#         d[grade]=name
#     else:
#         d[grade]+=" "+name
# for key,value in d.items():
#     print(f'{key}:{value}')



# 4. Find the Most Frequent Word
# sentence=input()
# word=""
# words={}
# for str in sentence+" ":
#     if str!=" ":
#         word+=str
#     else:
#         if word!="":
#             if word not in words:
#                 words[word]=1
#             else:
#                 words[word]+=1
#             word=""
# max_val=0
# max_key=''    
# for key,val in words.items():
#     if val>max_val:
#         max_val=val
#         max_key=key
# print(max_key)


# 5. Merge Two Dictionaries
# d1=input().split(",")
# d2=input().split(",")
# dict1={}
# dict2={}
# res={}
# for d,e in d1,d2:
#     key,val=d.split()
#     key1,val1=e.split()
#     dict1[key]=int(val)
#     dict2[key1]=int(val1)
# for key,val in dict1.items():
#     res[key]=val
# for key,val in dict2.items():
#     if key in res:
#         res[key]+=val
#     else:
#         res[key]=val
# for key,val in res.items():
#     print(f'{key}:{val}')




# 6. Find Employees Having the Same Salary
# n=int(input())
# d={}
# for i in range(n):
#     name,sal=input().split()
#     if sal not in d:
#         d[sal]=name
#     else:
#         d[sal]+=" "+name
# for sal,names in d.items():
#     if " " in names:
#         print(f'{sal}:{names}') 


# 7. Build an Inverted Dictionary


# 8. Count the Frequency of Each Number
# n=int(input())
# nums=input().split()
# d={}
# for num in nums:
#     num=int(num)
#     if num not in d:
#         d[num]=1
#     else:
#         d[num]+=1
# for key,val in d.items():
#     print(f'{key}:{val}')



# 9. Find Keys Having the Maximum Value
# n=int(input())
# d={} 
# for i in range(n):
#     key,val=input().split()
#     d[key]=int(val)
# max_val=0
# for key,val in d.items():
#     if val>max_val:
#         max_val=val
# for key,val in d.items():
#     if val==max_val:
#         print(key)


# 10. Build a Phone Directory
# n=int(input())
# d1={}
# for i in range(n):
#     name,phone=input().split()
#     d1[name]=phone
# target=input()
# for i in d1:
#     if i==target:
#         print(d1[i])
#         break
