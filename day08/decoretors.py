import time


def timer(func) :
    def wrapper(*args) :
        start = time.time()
        result = func(*args)
        time.sleep(3)
        end = time.time()
        run_time = end - start
        print(f"run time of your function is ==  {run_time}")
        return result
    return wrapper    


#@timer
def addition(x,y):
    num1 = x
    num2 = y
    result = num1 + num2
    return result

ans = timer(addition)
print(ans(1,2))
print(ans(4,5))
