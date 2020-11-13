# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    
    evacuation = []
    for k,v in enumerate(source_array):
        if v % 2 != 0:
            evacuation.append(v)
            source_array[k] = 'odd'
            
    evacuation = sorted(evacuation)
    for k,v in enumerate(source_array):
        if v == 'odd':
            source_array[k] = evacuation.pop(0)

    return source_array