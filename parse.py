class Star:
    def __init__(self, mass, lum):
        self.mass = mass
        self.lum = lum

class Planet:
    def __init__(self,mass):
        self.mass = mass

objs_star = list()
objs_planet = list()

def parse_run(file_name):
    if parser(file_name) is False:
        print("Failed to Load System File")
        return False
    return True

def parser(file_name):
    file = open(file_name)
    if file.closed:
        return False
    list = file.readlines()[1:]
    list1 = [elem.strip().split() for elem in list]

    for i in range(0,len(list1)):
        if list1[i][0] == "STAR":
            parse_star(list1[i])
        elif list1[i][0] == "PLANET":
            parse_planet(list1[i])

def parse_star(list):
    objs_star.append(Star(list[1],list[2]))

def parse_planet(list):
    objs_planet.append(Planet(list[1]))