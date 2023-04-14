#A function named concatenate_args that takes any number of string arguments
# in positional arguments format and concatenates them into a single string
def concatenate_args(*words):
    get = ""
    for x in words:
       get += x  
    return get  

#A function named concatenate_kwargs that takes any number of string arguments 
# in keyword arguments  format and concatenates them into a single string
def  concatenate_kwargs (**kwargs):
    result = ""
    for i in kwargs.values():
        result += i
    return result