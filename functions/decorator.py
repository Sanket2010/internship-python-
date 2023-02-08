#decorator
def div(a,b):
    
    return a/b

def smart_div(func):
    
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart_div(div)

result = div(2,4)
print(result)


# a=2
# b=4
# if a<b:
#     a,b=b,a
# r= div(a,b)
# print(r)