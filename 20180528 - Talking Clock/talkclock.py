"""
Description
No more hiding from your alarm clock! You've decided you want your computer 
to keep you updated on the time so you're never late again. 
A talking clock takes a 24-hour time and translates it into words.
Input Description
An hour (0-23) followed by a colon followed by the minute (0-59).
Output Description
The time in words, using 12-hour format followed by am or pm. 
"""

hour = {
    '00' : "Twelve",
    '01' : "One",
    '02' : "Two",
    '03' : "Three",
    '04' : "Four",
    '05' : "Five",
    '06' : "Six",
    '07' : "Seven",
    '08' : "Eight",
    '09' : "Nine",
    '10' : "Ten",
    '11' : "Eleven",
    '12' : "Twelve",
    '13' : "One",
    '14' : "Two",
    '15' : "Three",
    '16' : "Four",
    '17' : "Five",
    '18' : "Six",
    '19' : "Seven",
    '20' : "Eight",
    '21' : "Nine",
    '22' : "Ten",
    '23' : "Eleven",
    '24' : "Twelve",
}

MinF = {
    '0' : "Oh",
    '1' : "",
    '2' : "Twenty",
    '3' : "Thirty",
    '4' : "Fourty",
    '5' : "Fifty",
    '6' : "Sixty",
    '7' : "Seventy",
    '8' : "Eighty",
    '9' : "Ninety",
    
}

MinS = {
    '0' : "",
    '1' : "One",
    '2' : "Two",
    '3' : "Three",
    '4' : "Four",
    '5' : "Five",
    '6' : "Six",
    '7' : "Seven",
    '8' : "Eight",
    '9' : "Nine",
    '10' : "Ten",
    '11' : "Eleven",
    '12' : "Twelve",
    '13' : "Thirteen",
    '14' : "Fourteen",
    '15' : "Fifteen",
    '16' : "Sixteen",
    '17' : "Seventeen",
    '18' : "Eighteen",
    '19' : "Nineteen",
    
}

time_in = input("Input time: ")
inhour  = time_in.split(':')[0]
in_mtens = time_in.split(':')[1][0]
in_mones = time_in.split(':')[1][1]

sentence = "It's " + hour[inhour]

if (in_mtens == "0") & (in_mones == "0") :
    None #do nothing
elif in_mtens != "1":
    sentence += (" " + MinF[in_mtens])
    sentence += (" " + MinS[in_mones])
else:
    sentence += (" " + MinS["1" + in_mones])

meridian = "AM"
if int(inhour) > 11:
    meridian = " PM"

sentence += (meridian)


print(sentence)

"""
Sample Input data

00:00
01:30
12:05
14:01
20:29
21:00

Output:
It's Twelve  AM
It's One Thirty AM
It's Twelve Oh Five PM
It's Two Oh One PM
It's Eight Twenty Nine PM
It's Nine PM
"""

"""
#Smarter way:

import sys
from num2words import num2words

def clock_To_String(time):
        split_time = time.split(":",2)
    end = "am"
    if int(split_time[0]) >= 12:
        end = "pm"
        split_time[0] = str(int(split_time[0]) - 12)
    if int(split_time[0]) == 0:
        split_time[0] = "12"
    print ("it's %s%s%s%s" % 
    (num2words(int(split_time[0])) + " ",
    "" if int(split_time[1]) >= 10 or int(split_time[1]) == 0 else "oh ",
    "" if int(split_time[1]) == 0 else num2words(int(split_time[1])) + " "
    ,end))  
clock_To_String(sys.argv[1])
"""