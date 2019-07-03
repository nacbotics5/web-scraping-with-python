#-*-coding:utf8;-*-
import re
from random import choice


class sub(object):
    """ a simple text to number evaluating class """
    def text_to_number(self,text):
        '''convert a number written as text to its real number equivalence'''
        text = text.lower()
    
        text = re.sub(r"ten", "10", text)
        text = re.sub(r"eleven", "11", text)
        text = re.sub(r"twelve", "12", text)
        text = re.sub(r"thirteen", "13", text)
        text = re.sub(r"fourteen", "14", text)
        text = re.sub(r"fifteen", "15", text)
        text = re.sub(r"sixteen", "16", text)
        text = re.sub(r"seventeen", "17", text)
        text = re.sub(r"eighteen", "18", text)
        text = re.sub(r"nineteen", "19", text)
        text = re.sub(r"twenty one", "21", text)
        text = re.sub(r"twenty two", "22", text)
        text = re.sub(r"twenty three", "23", text)
        text = re.sub(r"twenty four", "24", text)
        text = re.sub(r"twenty five", "25", text)
        text = re.sub(r"twenty six", "26", text)
        text = re.sub(r"twenty seven", "27", text)
        text = re.sub(r"twenty eight", "28", text)
        text = re.sub(r"twenty nine", "29", text)
        text = re.sub(r"twenty", "20", text)
        text = re.sub(r"thirty one", "31", text)
        text = re.sub(r"thirty two", "32", text)
        text = re.sub(r"thirty three", "33", text)
        text = re.sub(r"thirty four", "34", text)
        text = re.sub(r"thirty five", "35", text)
        text = re.sub(r"thirty six", "36", text)
        text = re.sub(r"thirty seven", "37", text)
        text = re.sub(r"thirty eight", "38", text)
        text = re.sub(r"thirty nine", "39", text)
        text = re.sub(r"thirty", "30", text)
        text = re.sub(r"forty one", "41", text)
        text = re.sub(r"forty two", "42", text)
        text = re.sub(r"forty three", "43", text)
        text = re.sub(r"forty four", "44", text)
        text = re.sub(r"forty five", "45", text)
        text = re.sub(r"forty six", "46", text)
        text = re.sub(r"forty seven", "47", text)
        text = re.sub(r"forty eight", "48", text)
        text = re.sub(r"forty nine", "49", text)
        text = re.sub(r"forty", "40", text)
        text = re.sub(r"fifty one", "51", text)
        text = re.sub(r"fifty two", "52", text)
        text = re.sub(r"fifty three", "53", text)
        text = re.sub(r"fifty four", "54", text)
        text = re.sub(r"fifty five", "55", text)
        text = re.sub(r"fifty six", "56", text)
        text = re.sub(r"fifty seven", "57", text)
        text = re.sub(r"fifty eight", "58", text)
        text = re.sub(r"fifty nine", "59", text)
        text = re.sub(r"fifty", "50", text)
        text = re.sub(r"sixty one", "61", text)
        text = re.sub(r"sixty two", "62", text)
        text = re.sub(r"sixty three", "63", text)
        text = re.sub(r"sixty four", "64", text)
        text = re.sub(r"sixty five", "65", text)
        text = re.sub(r"sixty six", "66", text)
        text = re.sub(r"sixty seven", "67", text)
        text = re.sub(r"sixty eight", "68", text)
        text = re.sub(r"sixty nine", "69", text)
        text = re.sub(r"sixty", "60", text)
        text = re.sub(r"seventy one", "71", text)
        text = re.sub(r"seventy two", "72", text)
        text = re.sub(r"seventy three", "73", text)
        text = re.sub(r"seventy four", "74", text)
        text = re.sub(r"seventy five", "75", text)
        text = re.sub(r"seventy six", "76", text)
        text = re.sub(r"seventy seven", "77", text)
        text = re.sub(r"seventy eight", "78", text)
        text = re.sub(r"seventy nine", "79", text)
        text = re.sub(r"seventy", "70", text)
        text = re.sub(r"eighty one", "81", text)
        text = re.sub(r"eighty two", "82", text)
        text = re.sub(r"eighty three", "83", text)
        text = re.sub(r"eighty four", "84", text)
        text = re.sub(r"eighty five", "85", text)
        text = re.sub(r"eighty six", "86", text)
        text = re.sub(r"eighty seven", "87", text)
        text = re.sub(r"eighty eight", "88", text)
        text = re.sub(r"eighty nine", "89", text)
        text = re.sub(r"eighty", "80", text)
        text = re.sub(r"ninety one", "91", text)
        text = re.sub(r"ninety two", "92", text)
        text = re.sub(r"ninety three", "93", text)
        text = re.sub(r"ninety four", "94", text)
        text = re.sub(r"ninety five", "95", text)
        text = re.sub(r"ninety six", "96", text)
        text = re.sub(r"ninety seven", "97", text)
        text = re.sub(r"ninety eight", "98", text)
        text = re.sub(r"ninety nine", "99", text)
        text = re.sub(r"ninety", "90", text)    
        text = re.sub(r"one", "01", text)
        text = re.sub(r"two", "02", text)
        text = re.sub(r"three", "03", text)
        text = re.sub(r"four", "04", text)
        text = re.sub(r"five", "05", text)
        text = re.sub(r"six", "06", text)
        text = re.sub(r"seven", "07", text)
        text = re.sub(r"eight", "08", text)
        text = re.sub(r"nine", "09", text)       
        text = re.sub(r"hundred", "00", text)
        text = re.sub(r"thousand", "000", text)
        text = re.sub(r"million", "000000", text)
        text = re.sub(r"billion", "000000000", text)    
        return text
    


