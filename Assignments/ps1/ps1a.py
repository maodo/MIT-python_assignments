#******House hunting part A ************



portion_down_payment = 0.25
r = 0.04
#Getting user input
annual_salary = float(input("Enter your annual salary : "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
#Computing the number of months
monthly_savings = (annual_salary/12) * portion_saved
down_payment = total_cost * portion_down_payment
current_savings = 0.0
number_of_months = 0
#invest_income = current_savings * r/12
while current_savings < down_payment:
	current_savings += monthly_savings + ((current_savings * r) / 12)
	number_of_months += 1

print("Number of months: {} ".format(int(number_of_months)))