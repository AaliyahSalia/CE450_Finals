def deep_rvrs(tup):
    if len(tup) == 0:
        return tup
    elif isinstance(tup[0], tuple):
        return deep_rvrs(tup[1:]) + (deep_rvrs(tup[0]),)
    else:
        return deep_rvrs(tup[1:]) + (tup[0],)

a = (11, 12, 13, 14) 
print(deep_rvrs (a))
tpl = (11, (12, (13,113), 14), 15)
print(deep_rvrs (tpl))
# Output
