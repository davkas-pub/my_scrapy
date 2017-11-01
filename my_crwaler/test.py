import re
string = 'S04E06'

eposode_list = re.search(r"S(\d+)E(\d+)", string).group(2)

print(eposode_list)

