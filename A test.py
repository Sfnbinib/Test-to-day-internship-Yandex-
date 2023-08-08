
from datetime import datetime, timedelta

n = int(input())                                        # Вводим количество временных меток (Логов)
timestamps = []                                         # Создаем пустой список для хранения временных меток (Логов)



for _ in range(n):                                                                              # Начинаем цикл для ввода n временных меток (Логов)
    timestamp_str = input()                                                                     # Вводим строку Лога (временной метки)
    timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")                                  # Преобразуем строку в объект datetime
    timestamps.append(timestamp)                                                              # Добавляем объект datetime в список временных меток




min_days = 1                                                                                    # Начальное количество дней
prev_timestamp = timestamps[0]                                                                # Возвращение 1 лого из списка для сравнения

for i in range(1, n):                                                                        # Проходим по всем индексам в списке временных меток (начиная со второй)
    diff = timestamps[i] - prev_timestamp                                                        # Вычисляем разницу между текущей и предыдущей меткой
    if diff.total_seconds() >= 24 * 60 * 60 or timestamps[i].strftime("%H:%M:%S") == "00:00:00":      # Если разница больше или равна 24 часам или начинается новый день
        min_days += 1                                    # Увеличиваем количество дней
    prev_timestamp = timestamps[i]                       # Обновляем предыдущую временную метку

print(min_days)  # Результат









# 00:00:00
# 00:01:11
# 02:15:59
# 23:59:58
# 23:59:59


# 12:00:00
# 23:59:59
# 00:00:00

# 00:00:00
# 00:00:00
# 00:00:00
# 00:00:00
