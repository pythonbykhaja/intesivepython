def prime_numbers(start, end):
    """
    This method will print prime numbers from start to end

    arguments:
    start: This argument accepts integer and indicates start 
    end: This argument accepts integer and indicates end
    """
    def is_prime(number):
        for index in range(2, (number//2)+1):
            if number%index == 0:
                return False
        return True

    for index in range(start,end):
        if is_prime(number=index):
            print(index, end='\t')

start = int(input('Enter the start: '))
end = int(input('Enter the end: '))
prime_numbers(start,end)
