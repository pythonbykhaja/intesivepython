import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--principal",action="store", type=float, 
    help="Principal", default=10000, required=True)
    parser.add_argument("-r", "--rate", action="store", type=float, 
    help="rate of interest", default=10, required=True)
    parser.add_argument("-t", "--time", action="store", type=int, 
    help="time in years", default=1, required=True)
    args = parser.parse_args()
    principal = float(args.principal)
    rate = float(args.rate)
    time = int(args.time)
    si = principal * time * rate / 100
    ci = principal * ( 1 + (rate/100))**time
    print(f"Simple Interest = {si} \nCompound Interest = {ci}")
