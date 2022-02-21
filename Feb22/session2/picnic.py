def food_items(*args):
    """ This function will solve the following question
    Function Call                               Sample Output
    food_items('salad')                     => You are bringing salad
    food_items('salad', 'chips')            => You are bringing salad and chips
    food_items('salad', 'chips', 'cake')    => You are bringing salad, chips and cake
    """
    item_punctuaded = ""
    if len(args) == 1:
        item_punctuaded = args[0]
    elif len(args) == 2:
        item_punctuaded = f"{args[0]} and {args[1]}"
    elif len(args) > 2:
        last_two = f"{args[-2]} and {args[-1]}"
        other_than_last_two = ", ".join(args[0:-2])
        item_punctuaded = f"{other_than_last_two}, {last_two}"
    else:
        return ""
        
    message = f"You are bringing {item_punctuaded}"
    return message