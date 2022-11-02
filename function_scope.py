salary = 650

def salary_bonus(bonus):
    global salary
    salary += bonus
    print(salary)
    return salary

salary_bonus(50) # 700