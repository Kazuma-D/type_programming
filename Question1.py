for num in range(1, 101):
    string = ''
    
    # ここから記述
    
    if num % 15 == 0:         #15の倍数のもの
        string = "FizzBuzz"

    elif num % 3 == 0:        #3の倍数かつ15の倍数でないもの
        string = "Fizz"

    elif num % 5 == 0:        #5の倍数かつ15の倍数でないもの
        string = "Buzz"

    else:                     #それら以外
        string = num
        
    # ここまで記述

    print(string)
