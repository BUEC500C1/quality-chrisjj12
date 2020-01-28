def conv(num2, output):

    arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    j = 0
    if num2 > 0:
        while num2 < arab[i]:
            i = i + 1
        while (num2 // arab[i]) > 0:
            num3 = num2 // arab[i]
            while (num2 - arab[i]) >= 0 and j < num3:
                output = output + rom[i]
                j = j + 1
            j = 0
            num2 = num2 - (num3*arab[i])
            if num2 == 0:
                print(output)
                break
            i = i + 1
            while num2 < arab[i]:
                i = i + 1


output = ''




        
        




