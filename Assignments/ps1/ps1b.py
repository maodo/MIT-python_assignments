#******Part B: Saving, with a raise*******



#******House hunting part A ************
portion_down_payment = 0.25
r = 0.04
#Getting user input
annual_salary = float(input("Enter your annual salary : "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal : "))
#Computing the number of months
month_salary = annual_salary/12
down_payment = total_cost * portion_down_payment
current_savings = 0.0
number_of_months = 0
#invest_income = current_savings * r/12
while current_savings < down_payment:

	monthly_savings = month_salary * portion_saved
	current_savings += monthly_savings + ((current_savings * r) / 12)
	number_of_months += 1
	if (number_of_months%6==0):
		month_salary += month_salary * semi_annual_raise

print("Number of months: {} ".format(int(number_of_months)))