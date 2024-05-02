#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_elments(elments):
        return (elments if elments != search else replace)
    return list(map(s_r_elments, my_list))
