
low = "(IX|(IV|V?I{0,3}))?"
medium = "(XC|(XL|L?X{0,3}))?"
high = "(CM|(CD|D?C{0,3}))?"

regex_pattern = r"^M{0,3}%s%s%s$"%(high,medium,low)	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))