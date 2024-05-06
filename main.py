#script
import fibonacci

def main():
    print('starting main....')
    number=int(input("enter the length of fibonacci series:"))
    
    series = fibonacci.get_fibonacci_series(number)

    if series is None:
        print('invalid input,please enter valid data type')

    print (series)


main()