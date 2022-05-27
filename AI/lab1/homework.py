'''
a = [1,2,3,'hello','world'] #creat a list
b = [x for x in range(100) if x %9 == 0]
print(b)
'''
def Factors(number):
    result = []
    for i in range(1, number+1):
        if (number % i) == 0:
            result.append(i)
    return result

def Common_Factors(n1, n2):
    result = []
    for element in n1:
        if element in n2:
            result.append(element)
    return result

def greatest_common_factor(common_factors):
    count = 0
    length = len(common_factors)
    current_largest = common_factors[count]
    for i in common_factors:
        count += 1
    if count <= length -1:
        if current_largest < common_factors[count]:
            current_largest = common_factors[count]
    return current_largest

def main():
    n1 = 8
    n2 = 16
    result1 = Factors(n1)
    result2 = Factors(n2)
    CF = Common_Factors(result1, result2)
    GCF = greatest_common_factor(CF)
    dict = {}
    dict.setdefault([n1, n2], []).append(CF)
    print (dict)

if __name__ == '__main__':

    main()