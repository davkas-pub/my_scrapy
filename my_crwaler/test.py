# import re
# string = 'S04E06'
#
# eposode_list = re.search(r"S(\d+)E(\d+)", string).group(2)
#
# print(eposode_list)


id = [5,4,3,2,1]

print(id[1:-1])

id = 5
select_str = ".seasonitem h3[id='{0}']".format(id)

print(select_str)
