def emp_traget(hours, target):
    count = 0
    for i in range(len(hours)):
        if hours[i] >= target:
            count = count + 1
    print(count)


emp_traget([98], 5)
