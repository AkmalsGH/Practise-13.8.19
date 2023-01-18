total_tickets = int(input('Введите количество билетов:'))
numbers_ages = []
for i in range(0, total_tickets):
    input_value = int(input(f'Введите возраст посетителя № {i + 1}:\n'))
    numbers_ages.append(input_value)

    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390

    full_prise = sum(map(prise, numbers_ages))

discount_prise = int(full_prise * 0.9)
if total_tickets > 3:
    print('Общая стоимость билетов со скидкой:', discount_prise, "руб.")
else:
    print('Общая стоимость билетов:', full_prise, "руб.")