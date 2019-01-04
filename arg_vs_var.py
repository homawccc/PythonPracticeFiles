# with variables

n = 10
pwr = 2

def badsquare_v():
    r = n ** pwr
    return r

print(badsquare_v()) #runs function/prints returned result (y) using vars


#---------------------------------------------------#
# with arguments in place of global variables (**preferred method**)

def badsquare_a(num, pwr):
    x = num ** pwr
    return x

result = badsquare_a(4, 2)  # represents called function with arguments
print(result)  #prints variable value