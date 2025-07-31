#   В Python одна функция может использовать другую функцию, вызывая её внутри
#   своего тела. В вашем конкретном случае, функция check_sleep может использовать
#   функцию time_to_wake_up, вызывая её внутри цикла while.

#   Примерно так это может выглядеть в вашем коде:

def time_to_wake_up(hours_slept):
    if hours_slept > 8:
        return True
    else:
        return False


def check_sleep():
    hours = 0
    while not time_to_wake_up(hours):
        hours += 1
    return hours


#   Вызов функции check_sleep
hours_slept = check_sleep()
print(f"Мы спали {hours_slept} часов, пока не проснулись.")

#   Таким образом, функция check_sleep использует функцию time_to_wake_up, чтобы определить, когда пора просыпаться.
