import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        print('DuurBara')
        some_function()
        t2 = time.time()
        print('laora bara')
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))  

if __name__ == "__main__":
   print("Value of __name__is:", __name__)
   print(my_function())
   #print(dir(__builtins__))
   