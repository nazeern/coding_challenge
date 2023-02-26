from timeit import default_timer as timer

array = []
for i in range(1000): 
    array.append(i)

start = timer()

count = 0
for num in array:
    count += 1

end = timer()

print(f"Built-in iteration: {end - start}")

start = timer()

count = 0
for i in range(len(array)):
    count += array[i]
    

end = timer()

print(f"Iteration with range and len: {end - start}")


start = timer()

count = 0
for i, num in enumerate(array):
    count += num

end = timer()

print(f"Iteration with enumerate: {end - start}")

