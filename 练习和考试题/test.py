import concurrent.futures


def some_function(x):
    return x * x


with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(some_function, i) for i in range(10)]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

print(results)
