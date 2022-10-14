from constraint import *


def must_be(marija, petar):
    if marija == 1 or petar == 1:
        return True
    else:
        return False


def marija_termin(marija, termin):
    if marija == 1 and termin in [14, 15, 18]:
        return True
    elif marija == 0 and termin not in [14, 15, 18]:
        return True
    else:
        return False


def petar_termin(petar, termin):
    if petar == 1 and termin in [12, 13, 16, 17, 18, 19]:
        return True
    elif petar == 0 and termin not in [12, 13, 16, 17, 18, 19]:
        return True
    else:
        return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [13, 14, 16, 19])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # MARIJA = [14, 15, 18]
    # SIMONA = [13, 14, 16, 19]
    # PETAR = [12, 13, 16, 17, 18, 19]
    # [12, 13, 14, 15, 16, 17, 18, 19, 20]
    problem.addConstraint(must_be, ("Marija_prisustvo", "Petar_prisustvo"))
    problem.addConstraint(marija_termin, ("Marija_prisustvo", "vreme_sostanok"))
    problem.addConstraint(petar_termin, ("Petar_prisustvo", "vreme_sostanok"))

    # ----------------------------------------------------

    # [print(solution) for solution in problem.getSolutions()]

    # ZA PRAVILNO PRINTANJE, da ne bide izmeshano
    for solution in problem.getSolutions():
        print(f"{{'Simona_prisustvo': {solution['Simona_prisustvo']}, 'Marija_prisustvo': {solution['Marija_prisustvo']}, 'Petar_prisustvo': {solution['Petar_prisustvo']}, 'vreme_sostanok': {solution['vreme_sostanok']}}}")
