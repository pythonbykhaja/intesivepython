if __name__ == '__main__':
    n = int(input())
    if not 1 <= n <= 150:
        exit(1)
    for index in range(1, n+1):
        print(index, end='')