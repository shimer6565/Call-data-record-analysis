# PYTHON PACKAGE
# CDR Analysis
# by shimer [20pd17] & shakthi [20pd10]

from CDR_Analysis import *

print("This is a program for Call Detail Record analysis")
name = "input.csv"   # demo CSV file

# reading the demo CSV file
myList = readCSV(name)
data = [makecall(i) for i in myList]

# Analysis options
print("There are four data analysis are available\n")
print("A: The amount and ratio of Network ERROR analysis")
print("B: The amount and ratio of Network ERROR analysis by timezone")
print("C: The amount of call time analysis by timezone")
print("D: Call time and cost analysis in different days\n")
end = "y"
while end == "y":
    ans = input("Please Enter your option [A/B/C/D] :")
    if ans == "A":
        networkERR(data)
    elif ans == "B":
        networkERRbyzone(data)
    elif ans == "C":
        call_by_time(data)
    elif ans == "D":
        call_by_day(data)

    end = input("\n Keep Analyzing (yes-y / no-n) : ")
print("\n        Thank you")



















