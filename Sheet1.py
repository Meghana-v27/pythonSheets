#1. Swap Two Numbers Without Third Variable
# Task: Swap using arithmetic operators and bitwise XOR. 
# Example Input: A=15, B=25 Example Output: A=25, B=15
A=15
B=25
A=A^B
B=A^B
A=A^B
print(f'A={A} B={B}')
#2. Convert Seconds Into Hours, Minutes and Seconds
# Task: Find hours, minutes and remaining seconds. Example Input: Total seconds=7384 
# Example Output: Hours=2, Minutes=3, Seconds=4
seconds=7384
hours=seconds//3600
seconds=seconds%3600
minutes=seconds//60
seconds=seconds%60
print(f'Hours={hours}, Minutes={minutes}, Seconds={seconds}')
#3. Temperature Conversion System
# Task: Convert Celsius to Fahrenheit and Fahrenheit to Celsius. Example Input: Celsius=30 
# Example Output: Fahrenheit=86
celsius=int(input('Celsius='))
fahrenheit=int((celsius*9/5)+32)
print(f'Fahrenheit={fahrenheit}')
Cel=int((fahrenheit-32)*5/9)
print(f'Celsius={Cel}')
#4. Calculate Compound Amount
# Calculate Compound Amount Definition: Compound interest calculates interest on both the original amount and 
# previously earned interest. Task: Calculate final amount using the compound interest formula. 
# Formula: Amount = P × (1 + R/100)^T Where: P = Principal amount R = Rate of interest T = Time period 
# Example Input: Principal = 10000 Rate = 10 Time = 2 years Example Output: Final Amount = 12100
p=int(input('Principal ='))
r=int(input('Rate = '))
t=int(input('Time = '))
Amount=p*(1+r/100)**t
print(int(Amount))
#5. Split Bill Among Friends Definition: Divide a total bill equally among people. 
# Task: Find each person's share and remaining amount.Example Input: Bill=2455, Friends=5 
# Example Output: Each pays=491, Remaining=0
Bill=2455
Friends=5
pay=Bill//5
remains=Bill%5
print(f'Each pays={pay}, Remaining={remains}')
#6. Convert Distance Units Definition: Convert kilometers into smaller units. 
# Task: Convert km into meters, centimeters and millimeters. 
# Example Input: Distance=5 km Example Output: Meters=5000, Centimeters=500000, Millimeters=5000000
Distance=5
Meters=Distance*1000
Cmeters=Meters*100
Mmeters=Cmeters*10
print(f'Meters={Meters}, Centimeters={Cmeters}, Millimeters={Mmeters}')
#7. Digital Storage Conversion Definition: Convert storage units from GB to smaller units. 
# Task: Convert GB into MB, KB and Bytes. Example Input: Storage=2 GB 
# Example Output: MB=2048, KB=2097152, Bytes=2147483648 
GB=2
MB=GB*1024
KB=MB*1024
bytes=KB*1024
print(f"MB = {MB}  KB = {KB}  Bytes = {bytes}")
#8. Minimum Currency Notes Definition: Find the number of currency notes required for an amount. 
# Task: Use 500, 200, 100 and 50 denomination notes. Example Input: Amount=1850 
# Example Output: 500 notes=3, 200 notes=1, 100 notes=1, 50 notes=1
Amount=1850 
five_100=Amount//500
balance=Amount-(five_100*500)
print(f"500 notes={five_100}")
two_100=balance//200
balance2=balance-(two_100*200)
print(f"200 Notes={two_100}")
one_100=balance2//100
balance3=balance2-(one_100*100)
print(f"100 Notes={one_100}")
Fiftes=balance3//50
print(f"50 Notes={Fiftes}")
#9. Salary Calculation System Definition: Calculate final salary after adding bonus and deducting tax. 
# Task: Calculate the final salary. Example Input: Salary=40000, Bonus=5000, Tax=10% 
# Example Output: Final Salary=40500
salary=40000 
bonus=5000 
tax=10
tax_payable=(salary+bonus)*(tax/100)
print(f"Total Salary= {int(salary+bonus-tax_payable)}")
#10. Travel Time Calculator Definition: Calculate travel duration using distance and speed. 
# Task: Find time for two journeys and total time. Formula: Time = Distance / Speed 
# Example Input: Distance1=120, Speed1=60, Distance2=100, Speed2=50 
# Example Output: Journey1=2 hours, Journey2=2 hours, Total=4 hours
Distance1=120
Speed1=60
Distance2=100
Speed2=50
Time1=Distance1//Speed1
Time2=Distance2//Speed2
print(f"Journey1={Time1} hours")
print(f"Journey2={Time2} hours")
print(f"Total={Time1+Time2} hours")
