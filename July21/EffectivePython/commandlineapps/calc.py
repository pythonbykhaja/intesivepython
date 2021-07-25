import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="This will be number 1", type=float)
    parser.add_argument("number2", help="This will be number 2", type=float)
    parser.add_argument("-v","--verbosity", help="increase output verbosity", action='store_true')
    args = parser.parse_args()
    number1 = float(args.number1)
    number2 = float(args.number2)
    if args.verbosity:
        print(f"number1 = {number1}")
        print(f"number2 = {number2}")
    print(number1, number2)
    