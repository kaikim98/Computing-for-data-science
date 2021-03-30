"""
**Instruction**
<Social security number>
Korean social security number is composed in this way
First 6 digits indicate the birth year/month/day. When birth day is 1994/05/30 -> First 6 digits are 940530
7th digit indicate the sex of the person. Male gets 1 or 3 and female gets 2 or 4.
If the preson is born before year 2000, he or she receives 1 or 2, respectively
If the person is born after yera 2000(inclusive), he or she receives 3 or 4 respectively.

Complete P3 function for which input is the person's info and returns the first 7 digits of Korean social security number as string
- Input is a list of form [str sex, int birth_year, int birth_month, int birth_day]
- sex is either 'MALE' or 'FEMALE'
- Input does not include invalid dates(e.g. don't worry about 2021-02-29, 1998-04-31, 2007-13-01 etc)

>>> P3(['MALE', 1996, 10, 30])
'9610301'

>>> P3(['FEMALE', 2000, 1, 2])
'0001024'

>>> P3(['FEMALE', 2021, 3, 28])
'2103284'


"""

def P3(info:list) -> str:        
    if info[1] % 100 < 10:
        a = '0' + str(info[1] % 100)
    else:
        a = str(info[1] % 100)
    if info[2] < 10:
        b = '0' + str(info[2])
    else:
        b = str(info[2])
    if info[3] < 10:
        c = '0' + str(info[3])
    else:
        c = str(info[3])
    if info[1] < 2000:
        if info[0] == 'MALE':
            d = str(1)
        elif info[0] == 'FEMALE':
            d = str(2)
    elif info[1] >= 2000:
        if info[0] == 'MALE':
            d = str(3)
        elif info[0] == 'FEMALE':
            d = str(4)
    x = print(a+b+c+d)
    return x