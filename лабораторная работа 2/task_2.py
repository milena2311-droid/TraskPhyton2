salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_deficit = 0.0
current_spend = spend

for _ in range(months):
    deficit = max(0.0, current_spend - salary)
    total_deficit += deficit
    current_spend *= (1 + increase)

required_cushion = round(total_deficit)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_cushion)
