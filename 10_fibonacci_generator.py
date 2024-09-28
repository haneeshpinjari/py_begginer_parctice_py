def fibonacci(n):
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series
n = int(input("Enter hopw many fibonacci numbers to generate: "))
print(fibonacci(n))
    