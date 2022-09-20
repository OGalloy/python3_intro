
values = [0, 2, 10, 6]

def same_by(characteristic, objects):
    truth_list = [True for object in objects if not characteristic(object)]
    if objects == []:
        return True
    if len(objects) == len(truth_list):
        return True
    else:
        return False 
        
print(same_by(lambda x: x % 2, values))