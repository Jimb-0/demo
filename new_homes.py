#this program calculates how many months it will take you to save up enough money for a down
#payment on a house 
total_cost = float(input('Please type the cost of your dream home: '))
current_savings,num_of_months,portion_down_payment,r = 0,0,.25,.04
annual_salary = float(input('Please type your starting salary: '))
portion_saved = float(input('Please type the percentage you want saved as a decimal: '))
monthly_salary = annual_salary/12
semi_annual_raise = float(input('Please enter your desired semi annual raise: '))

while portion_down_payment * total_cost >= current_savings:
    current_savings += monthly_salary*portion_saved + (current_savings*r)/12
    num_of_months += 1
    #every 6 months month you get a raise
    if num_of_months%6 == 0:
        monthly_salary *= (semi_annual_raise+1)

print('Down payment:',portion_down_payment * total_cost,'Savings:',current_savings)
print('Congratulations! You can now purchase your home in',num_of_months,'months')
