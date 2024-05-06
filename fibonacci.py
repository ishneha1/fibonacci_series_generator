#module 

def get_fibonacci_series(num):
    if not isinstance(num,int):
        return None

    if num<=0:
        return None
    if num==1:
        return [0]
    
    fibonacci_series=[0,1]

    for i in range (num-2):
        next_time=fibonacci_series[-1]+fibonacci_series[-2]
        fibonacci_series.append(next_time)

    return fibonacci_series
