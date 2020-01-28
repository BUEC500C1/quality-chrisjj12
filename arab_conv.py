def conv(num): #function

    arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] #array of distinct numbers according to roman
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] #all the roman numerals
    i = 0 #initializing a counter
    j = 0 # initializing a counter
    output = '' # initializing the string
    
    if not isinstance(num, int) or num > 4999 or num <= 0: #error checking
        return('Number is not valid')
    elif  5000 > num > 0: #valid input number range
        while num < arab[i]: #if an input number is smaller than a number in the array, it will go onto the next
            i = i + 1 #this allows for the loop go to the next spot in the array
        while (num // arab[i]) > 0: #the floor operator is used to get the placement whether it is thousands, hundreds, tens, ones
            num2 = num // arab[i] #the floor function is use for later on for num = num - (num2*arab[i])
            while (num - arab[i]) >= 0 and j < num2: #this loops the roman numeral until it gets the correct amount
                output = output + rom[i] #this adds the roman numeral to the output
                j = j + 1 #this allows for the loop go to the next spot in the array
            j = 0 #reinitializes the counter
            num = num - (num2*arab[i]) #this has it so that the thousands then hundreds then tens then ones gets eliminated through each loop
            if num == 0: #this if statement returns the output
                return output
                break #ends the program onces the output is returned
            i = i + 1 #this allows for the loop go to the next spot in the array
            while num < arab[i]: #if an input number is smaller than a number in the array, it will go onto the next
                i = i + 1 #this allows for the loop go to the next spot in the array








        
        




