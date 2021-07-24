import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    print(f"Arguments passed are {args}")
    if args[0] == 'add':
        result = int(args[1]) + int(args[2])
        print(result)
    elif args[0] == 'mul':
        result = int(args[1]) * int(args[2])
        print(result)
    elif args[0] == 'div':
        result = int(args[1]) / int(args[2])
        print(result)
    elif args[0] == 'sub':
        result = int(args[1]) - int(args[2])
        print(result)
    elif args[0] == '--help' or args[0] == 'help':
        print("Usage is <operation> arg1 arg2")
        print("Supported operations are add, mul, div, sub")
    



