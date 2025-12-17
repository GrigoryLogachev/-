salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

current_spend = spend
total_spend = 0
max_deficit = 0

for i in range(1, months + 1):
    total_spend += current_spend
    deficit = total_spend - i * salary
    if deficit > max_deficit:
        max_deficit = deficit
    current_spend *= (1 + increase)

money_capital = max(0, max_deficit)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(money_capital)}")
