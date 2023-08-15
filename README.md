Test to day-internship in Yandex

It is the Test which i pass to day internship yandex:


Вася решил обработать логи с сервера, но обнаружил, что из-за ошибки разработчиков для каждого события в логе записывается только время этого события в формате HH:MM:SS, а дата не записывается.
Известно, что все события записаны в хронологическом порядке и два события не могли произойти в одну и ту же секунду. Определите минимальное количество дней, в течение которых записывался лог.		
													(Vasya decided to process logs from the server, but found that due to a developer error, only the time of this event in HH:MM:SS format is recorded in the log, and the date is not recorded.
It is known that all events are recorded in chronological order and two events could not occur in the same second. Determine the minimum number of days during which the log was recorded.
It is known that all events are recorded in chronological order and two events could not occur in the same second. Determine the minimum number of days during which the log was recorded.)


Формат ввода:
Первая строка входных данных содержит единственное число n (1 ≤ n ≤ 100000) — количество событий в логе. Следующие n строк описывают времена событий. Каждая строка имеет формат HH:MM:SS, где HH — число от 0 до 2 3 , а MM и SS — числа от 0 до 59. Все записи чисел состоят ровно из двух цифр.

(Input format:
The first line of input data contains the singular n (1 ≤ n ≤ 1000000) - the number of events in the log. The following n lines describe the time of events. Each line has the HH:MM:SS format, where HH is a number from 0 to 2 3, and MM and SS are numbers from 0 to 59. All number records consist of exactly two digits.)

Формат вывода
Выведите одно целое число — минимальное количество дней, в течение которых записывался лог.

(Output format
Print one integer - the minimum number of days during which the log was recorded.)



Example:

Input:                      Input:                             Input:       
5                              3   		                       	4

00:00:00                  12:00:00                           00:00:00
00:01:11                   23:59:59                          00:00:00
02:15:59                   00:00:00                           00:00:00
23:59:58                                                       00:00:00
23:59:59                    

Conclusion:             Conclusion:                       Conclusion:
     1			              2			                            4























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
        min_days += 1                                                            # Увеличиваем количество дней
    prev_timestamp = timestamps[i]                                               # Обновляем предыдущую временную метку

print(min_days)  # Результат



