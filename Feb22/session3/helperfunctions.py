from urllib.parse import parse_qs
# This is writing expressions directly
# from urllib.parse import parse_qs
# my_values = parse_qs('name=python&topic=effective&batch=1')
# my_values.get('name')[0] + ' ' + my_values.get('topic')[0]

def get_first_value(qs_dict, key, default=""):
    """
    This method will parse the qs dictionary are returns the first value
    """
    all_values = qs_dict.get(key, default)
    return all_values[0]



if __name__ == "__main__":
    qs = 'name=python&topic=effective&batch=1'
    qs_dict = parse_qs(qs)
    print(f"{get_first_value(qs_dict, key='name')} {get_first_value(qs_dict, key='topic')}")
    

