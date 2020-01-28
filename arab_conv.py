def conv(num):

    arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    j = 0
    output = ''
    
    if num > 4999 or num <= 0:
        print('Number is not valid')
    elif  5000 > num > 0:
        while num < arab[i]:
            i = i + 1
        while (num // arab[i]) > 0:
            num2 = num // arab[i]
            while (num - arab[i]) >= 0 and j < num2:
                output = output + rom[i]
                j = j + 1
            j = 0
            num = num - (num2*arab[i])
            if num == 0:
                return output
                break
            i = i + 1
            while num < arab[i]:
                i = i + 1








        
        




