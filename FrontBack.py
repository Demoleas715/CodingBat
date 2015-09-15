"""Front Back"""
"""var = input("What's your word?")
midVar = var[1:len(var)-1]
print(var[len(var)-1] + midVar + var[0])"""

def front_back(var):
	if len(var) <=1:
		return var

	midVar = var[1:len(var)-1]
	return var[1:len(var)-1] + midVar +var[0]