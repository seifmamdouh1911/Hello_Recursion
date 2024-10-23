def recursive_sum(arr, n, res):
    if n == 0:
        return res

    # Add the current element to res and proceed with the next
    res += arr[n - 1]

    # Recursively call with the rest of the array
    return recursive_sum(arr, n - 1, res)


def main():
    T = int(input())  # Number of test cases

    for case_num in range(1, T + 1):
        data = list(map(int, input().split()))  # Read input as integers
        N = data[0]  # First number is N
        arr = data[1:]  # Remaining numbers are the array

        # Call recursive_sum starting with a sum of 0
        result = recursive_sum(arr, N, 0)
        print(f"Case {case_num}: {result}")


if __name__ == "__main__":
    main()
