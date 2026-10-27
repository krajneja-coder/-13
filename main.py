
# Практична робота
# Білет №13
# Тема: Паркування автомобіля

# 1. Введення даних
car_number = input("Номер автомобіля: ")
hours = int(input("Тривалість паркування (години): "))
free_places = int(input("Кількість вільних місць: "))
balance = float(input("Баланс (грн): "))
price = float(input("Ціна за годину (грн): "))
permission = input("Дозвіл на паркування (так/ні): ").lower()

# 2. Основні перевірки
valid_hours = hours >= 1 and hours <= 24
has_space = free_places > 0

total_price = hours * price
enough_money = total_price <= balance
has_permission = permission == "так"

can_park = (
    valid_hours
    and has_space
    and enough_money
    and has_permission
)

# 3. Виведення результатів
print("\n--- Результати перевірки ---")
print("Номер автомобіля:", car_number)
print("Правильна тривалість:", valid_hours)
print("Є вільне місце:", has_space)
print("Вартість паркування:", total_price, "грн")
print("Достатньо грошей:", enough_money)
print("Є дозвіл:", has_permission)
print("Можна паркуватися:", can_park)

# 4. Додаткові перевірки
long_parking = hours > 8
expensive_parking = total_price > 500
two_hours = hours == 2
no_space = free_places == 0
no_permission = not has_permission

print("\n--- Додаткові перевірки ---")
print("Понад 8 годин:", long_parking)
print("Вартість понад 500 грн:", expensive_parking)
print("Рівно 2 години:", two_hours)
print("Немає вільних місць:", no_space)
print("Немає дозволу:", no_permission)
