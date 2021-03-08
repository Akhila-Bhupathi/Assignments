import re
def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(credit_card_number):
    
    cc_num=str(credit_card_number)
    cc_num = cc_num[::-1]
    
    cc_num = [int(x) for x in cc_num]
    
    doubled_second_digit_list = list()
    
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    sum_of_digits = sum(doubled_second_digit_list)
    
    return sum_of_digits % 10 == 0

def check_card_type(credit_card_number):
    
    card_num=str(credit_card_number)
    visa = bool(re.match("4[0-9]{12}(?:[0-9]{3})", card_num))
    mastercard = bool(re.match("5[1-5][0-9]{14}", card_num))
    discover = bool(re.match("6(?:011|5[0-9]{2})[0-9]{12}", card_num))
    american_express = bool(re.match("3[47][0-9]{13}", card_num))

    if(visa):
        return "visa"
    elif(mastercard):
        return "mastercard"
    elif(discover):
        return "discover"
    elif(american_express):
        return "american_express"
    
    
    
