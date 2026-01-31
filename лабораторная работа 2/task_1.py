money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
current_capital = money_capital
current_spend = spend

while True:
    budget = salary + current_capital
    if budget >= current_spend:
        months += 1
        # Потратили из бюджета, обновили подушку
        current_capital = budget - current_spend
        # Увеличение расходов для следующего месяца
        current_spend *= (1 + increase)
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", months)
