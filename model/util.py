import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    id=''
    while number_of_small_letters or number_of_capital_letters or number_of_digits or number_of_special_chars:
        number=random.randint(1,4)
        if number== 1 and number_of_small_letters== 0:
            continue
        elif number== 1:
            id+=chr(random.randint(97,122))
            number_of_small_letters -=1
        if number == 2 and number_of_capital_letters ==0:
            continue
        elif number==2:
            id+=chr(random.randint(65,90))
            number_of_capital_letters -=1
        if number == 3 and number_of_digits ==0:
            continue
        elif number==3:    
            id+=str(random.randint(0,9))
            number_of_digits -=1
        if number==4 and number_of_special_chars ==0:
            continue
        elif number==4:
            id += allowed_special_chars[random.randint(0,3)]
            number_of_special_chars -=1
    return id
        



