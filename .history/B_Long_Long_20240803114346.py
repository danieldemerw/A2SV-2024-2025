import sys
input = sys.stdin.read

# Read all input at once
data = input().strip().split()

# Index to track the current position in the input data
index = 0

# Number of test cases
t = int(data[index])
index += 1

results = []

for _ in range(t):
    # Length of the array
    n = int(data[index])
    index += 1
    
    # Array elements
    arr = list(map(int, data[index:index + n]))
    index += n
    
    # Calculate maximum possible sum (sum of absolute values)
    max_sum = sum(abs(x) for x in arr)
    
    # Calculate minimum number of operations
    operations = 0
    in_negative_segment = False

    for i in range(n):
        if arr[i] < 0:
            if not in_negative_segment:
                operations += 1
                in_negative_segment = True
        else:
            in_negative_segment = False

    results.append(f"{max_sum} {operations}")

# Print all results
print("\n".join(results))
