salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
for months in range(10, 0, -1):  # Запускаем цикл
    # Находим разность между тратами и зарплатой в конкретном месяце (с учетом инфляции)
    delta = spend - salary

    months -= 1
    spend *= 1 + increase

    # Складываем значения разностей для получения величины подушки безопасности
    money_capital += delta
print(round(money_capital))
