import numpy as np
import scipy as sp
import parse

parse.parse_run("config_files/sys.conf")

for i in range(0,len(parse.objs_star)):
    print(parse.objs_star[i].mass)
    print(parse.objs_star[i].lum)

for i in range(0,len(parse.objs_planet)):
    print(parse.objs_planet[i].mass)
