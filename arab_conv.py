def conv(num2, output):

    arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    i = 0
    print("Here")
    if num2 > 0:
        print("Here in if")
        for x in range(num2 // arab[i]):
            print("in for")
            print(x)
            y = mag(x)
            output = output + rom[i]
            num2 = num2 - (y*arab[i])
            print(output)
            if num2 == 0:
                print(output)
            i = i + 1
    #return output


num = input('Enter a number between 0 and 9999: ')
num2 = int(num)

output = ''

conv(num2, output)

