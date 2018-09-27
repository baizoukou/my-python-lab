## creat fct

def raise_to_power(base_num, pow_num): ## fct take 2 input num
    result = 1 ## def var call result is going to store result
    for index in range(pow_num): ## specify for loop that loop through range of num
        result = result * base_num ## math is going to be store in result
    return  result
print(raise_to_power(2,3))
