import argparse

if __name__ == '__main__':
    demo_parser = argparse.ArgumentParser(description='This is parser for learning ')
    demo_parser.add_argument('number1', help="The number1 to be added", type=int)
    demo_parser.add_argument('number2', help="The number2 to be added", type=int)
    demo_parser.add_argument('-v', '--verbosity', help='Display more info', action="store_true")
    args = demo_parser.parse_args()
    if args.verbosity:
        print(f"number1 is {args.number1} and number2 is {args.number2}")
    print(args.number1+args.number2)

