def average(array):
    k = set(array)
    # your code goes here
    return round(sum(k)/len(k), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)