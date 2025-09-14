def words_to_numbers(s):
    ones={
        "zero": 0, "One": 1, "Two":2,"Three":3,"four":4,"five":5,"Six":6,"seven":7,"eight":8,"nine":9
    }
    teens={"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
    tens={"twenty":20, "thirty":30 , "fourty":40 , "fifty":50 ,"sixty":60, "seventeen":70, "eighty":80, "ninety":90}
    multipliers={"hundred":100, "thusand":1000}

    words= s.lower().split()
    num, current=0,0
    for w in words:
        if w in ones:
            current+=ones[w]
        elif w in teens:
            current+=teens[w]
        elif w in tens:
            current+=tens[w]
        elif w=="hundred":
            current*=100
        elif w=="thousands":
            num+=current*1000
            current=0
    return num+current

def number_to_words(n):
    ones=["zero","one", "two","three","fou","five","six","seven","eight","nine"]
    teens=["ten","eleven","twelve","thirteen","fourteen","fifteen", "sixteen","seventeen","eighteen","nineteen"]
    tens=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]

    if n<10:
        return ones[n]
    elif n<20:
        return teens[n-10]
    elif n<100:
        return tens[n//10]+("" if n%10==0 else " " +ones[n%10])
    elif n<1000:
        return ones[n//100]+" hundred"+("" if n%100==0 else " " +number_to_words(n%100))
    elif n<10000:
        return ones[n//1000] +" thusand" + ("" if n%1000==0 else " "+ number_to_words(n%1000))
    
user_input= input("Enter a number or words between 1 to 10000:")

if user_input.isdigit():
    num= int(user_input)
    print('In words:', number_to_words(num))
else: 
    num= words_to_numbers(user_input)
    print("In numbers:", num)


        
