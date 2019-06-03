import re
from validate_email import validate_email
import phonenumbers
#install phonenumbers
#install validate_email
def validPhoneNumber(str): 
    #replace (,  ), +1, -, #all behine
    str_replaced = (str.replace('(','', -1)
                        .replace(')','', -1).replace('#','', -1)
                        .replace('+1','', -1).replace('-','', -1))

    Pattern = re.compile("[^a-zA-Z]\d{9}$") 
    return Pattern.match(str_replaced)

def main():

    print(validPhoneNumber("4692681252"))
    print(validPhoneNumber("+14692681252"))
    print(validPhoneNumber("4692681+252"))
    print(validPhoneNumber("469-2681252"))
    print(validPhoneNumber("4692^681252"))
    print(validPhoneNumber("4692681252#12")) 
    print(validate_email('123@7-11.com'))
    print(phonenumbers.parse("4692681252", "US"))
    print(phonenumbers.parse("+14692681252", "US"))
    print(phonenumbers.parse("14692681252", "US"))
    print(phonenumbers.parse("(469)2681252", "US"))
    print(phonenumbers.parse("469-268-1252", "US"))
    print(phonenumbers.parse("4692681+252", "US"))
    print(phonenumbers.parse("4692^681252", "US"))
    print(phonenumbers.parse("4692681252#12", "US"))
    
if __name__ == "__main__":
    main()