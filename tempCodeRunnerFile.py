import re

def validPhoneNumber(str): 
    #replace (,  ), +1, -, #all behine
    #
    Pattern = re.compile("^[0-9]") 
    return Pattern.match(str) 

def main():

    print(validPhoneNumber("469268125A2"))

if __name__ == "__main__":
    main()