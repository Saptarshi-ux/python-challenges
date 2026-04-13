def snail(snail_map):
    return list(snail_map[0]) + \
           snail(list(zip(*snail_map[1:]))[::-1]) if snail_map else []
