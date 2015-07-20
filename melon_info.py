"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melon_name, melon_seedless, melon_price, melon_flesh_color, melon_rind_color, melon_avg_weight


def print_melon(name, seedless, price, flesh_color, rind_color, weight):
	hashasnot = 'have'
	if seedless:
		hashasnot = 'do not have'
	
	print "%ss %s seeds and are $%0.2f. Their flesh color is %s, their rind color is %s, and their average weight is %0.2f units." % ( name, hashasnot, price, flesh_color, rind_color, weight)


for i in melon_name.keys():
    print_melon(melon_name[i], melon_seedless[i], melon_price[i], melon_flesh_color[i], melon_rind_color[i], melon_avg_weight[i])
