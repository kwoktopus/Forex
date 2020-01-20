import time

def runtime(function):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = function(*args, **kwargs)
        print("function", function.__name__,"has runtime:", time.time() - startTime, "seconds")
        return result

    return wrapper



