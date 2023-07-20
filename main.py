print("welcome user!")
company_name = input("Hello !what is your company's name?")
feet = int(input("Please enter the number feet of fiber optic to be installed"))
if feet > 500:
 rate = 0.50
elif feet > 250:
 rate = 0.70
elif feet > 100:
  rate = 0.80
else:
  rate = 0.87
total_cost = feet * rate
print("feet requested:", feet)
print ("the total cost is:",total_cost)
print("Thank you", company_name)