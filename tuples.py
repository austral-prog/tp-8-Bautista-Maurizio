def get_coordinate(record):
    return record [1]




import re
def convert_coordinate(coordinate):
    result = tuple(re.findall(r"[0-9]+|\w",coordinate))
    return result



def create_record(azara_record, rui_record):
    a = get_coordinate(azara_record)
    b = get_coordinate(rui_record)
    c= convert_coordinate(a)
    if c == b:
        result=azara_record+rui_record
        return result
    else:
        return "not a match"
