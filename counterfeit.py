
#AVG190500T

# Hello World program in Python
#1: reqirement first 3 eng_chars, upper and distinct
#2: reqirement year 1900~2019
#3: reqirement index faceamount before last letter
#4: reqirement after faceamount must be a len=1 eng_char

serialNumber = ["AVG190420T", "RTF20001000Z","QWER201850G","AAA2019100B","QWER201850GH"]

###### From Here OK
_3_chars_valid = True
year_valid = True
facemount_valid = True
last_char_valid = True

valid_amount_set = ["10","20", "50", "100", "200","500", "1000"]
#1 check cahr
#2 check year
#3 check faceamount

def get_index_of_digit(string):
  index = 0
  for c in string:
    if c.isdigit():
      break;
    index +=1
  return index

def is_distinct(string):
  char_map = [False] * 128
  for i in string:
    ascii_val = ord(i)
    if char_map[ascii_val]:
      return False
    char_map[ascii_val] = True
  return True

def get_year(s_num, first_index_of_digits):
  index_of_year = first_index_of_digits+4
  if index_of_year > len(s_num):
    return 0
    
  year_string = s_num[first_index_of_digits:first_index_of_digits+4]
  year_val  = int(year_string) if year_string.isdigit() else 0
  
  return year_val


def get_amt_string(s_num, index_of_amt_start):
  index_of_amt_end = len(s_num)-1
  if index_of_amt_end <= index_of_amt_start:
    facemount_valid=False
    return "0"
  return s_num[index_of_amt_start:index_of_amt_end]
 
  
def get_faceamount(s_num):
  serialnum_len = len(s_num)
  first_index_of_digits = get_index_of_digit(s_num)

  if serialnum_len <= 9 or serialnum_len > 12:
    return 0
  
  if first_index_of_digits != 3:
    #the first indext of digit must be 3
    _3_chars_valid = False
    return 0

  if s_num[0:3].isupper()==False:
    #First 3 chars must be upper letter
    _3_chars_valid = False
    return 0

  if is_distinct(s_num[0:3])==False:
    #First 3 chars must be distinct letter
    _3_chars_valid = False
    return 0

  if s_num[-2].isalpha() or (not (s_num[-1].isalpha())):
    #only last digits can be alpha
    last_char_valid = False
    return 0
  year_val = get_year(s_num, first_index_of_digits)
  if not (year_val >= 1900 and  year_val <=2019):
    year_valid = False
    return 0
  #finally get faceamount , end of year index till s_num -1
  index_of_amt_start = first_index_of_digits+4
  amt_string = get_amt_string(s_num, index_of_amt_start)
  
  if not amt_string in valid_amount_set:
    facemount_valid=False
    return 0
  
  
  amt_val =  int(amt_string) if amt_string.isdigit() else 0

  return amt_val
  
def countCounterfeit(serialNumber):
    sum = 0
    for i in serialNumber:
        sum += get_faceamount(i)
    return sum
  
###### To a: 
serialNumber = ["AVG190420T", "RTF20001000Z","QWER201850G","AAA2019100B","QWER201850GH"]

# print("ans", get_faceamount("RFV201111T"))
print("ans", get_faceamount())
# print("ans", get_faceamount(serialNumber[2]))
# print("ans", get_faceamount(serialNumber[3]))
# print("ans", get_faceamount(serialNumber[4]))


serialNumber2 = ["QDB2012R20B", "RED190250E","RFV201111T","TYU20121000E","AAA198710B", "Abc200010E"]
sum = 0
# for i in serialNumber2:
#     print("ans", get_faceamount(i))
#     sum += get_faceamount(i)
# print(sum)