import random

# Variables
end_count = 10

def task(count):
    result = count + random.randrange(10)
    print("Task #", count)
    return result


def loop_standard():
    for count in range(1, end_count+1):
        task(count)


def loop_truncation(threshold):
    condition = 0
    for count in range(1, end_count+1):
        if condition < threshold:
            condition = task(count)
            print("Condition:", condition)
        else:
            break

print("Standard Loop")
loop_standard()
print("-------------")
print("Loop Truncation")
loop_truncation(10)    
