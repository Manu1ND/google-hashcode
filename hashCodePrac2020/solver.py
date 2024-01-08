class Pizza:
    def __init__(self, pizzaType, nOfIngredients, ingredients):
        self.pizzaType = pizzaType
        self.nOfIngredients = nOfIngredients
        self.ingredients = ingredients


def solver(filename, input): # not be changed
    pizzas = []
    pizzaType = 0
    delToTwoTeam = 0
    delToThreeTeam = 0
    delToFourTeam = 0

    nOfPizzas, nOfTwoTeam, nOfThreeTeam, nOfFourTeam = map(
        int, input.readline().split())

    while line := input.readline().split():
        nOfIngredients = line[0]
        ingredients = line[1:]
        pizzas.append(Pizza(pizzaType, nOfIngredients, ingredients))
        pizzaType += 1

    # pizza allocation
    # for team of four
    if nOfPizzas > 0:
        delToFourTeam = nOfPizzas//4
        if nOfFourTeam < delToFourTeam:
            delToFourTeam = nOfFourTeam
        nOfPizzas = nOfPizzas - (delToFourTeam * 4)

        # 1 pizza left with atleast 1 team of two and three
        if (nOfPizzas == 1) and (nOfTwoTeam > 0) and (nOfThreeTeam > 0):
            delToFourTeam -= 1
            delToTwoTeam = delToThreeTeam = 1
            nOfPizzas = 0

        # 2 pizzas left
        if nOfPizzas == 2:
            if nOfTwoTeam > 0:  # minimum 1 team
                delToTwoTeam += 1
            elif nOfThreeTeam > 1:  # minimum 2 teams
                delToFourTeam -= 1
                delToThreeTeam += 2
            nOfPizzas = 0

    # for team of three
    if nOfPizzas > 0:
        delToThreeTeam = nOfPizzas//3
        if nOfThreeTeam < delToThreeTeam:
            delToThreeTeam = nOfThreeTeam
        nOfPizzas = nOfPizzas - (delToThreeTeam * 3)

        # 1 pizza left with atleast 2 teams of two
        if (nOfPizzas == 1) and (nOfTwoTeam > 1):
            delToThreeTeam -= 1
            delToTwoTeam += 2
            nOfPizzas = 0

    # for team of two
    if nOfPizzas > 0:
        delToTwoTeam += nOfPizzas//2
        if nOfTwoTeam < delToTwoTeam:
            delToTwoTeam = nOfTwoTeam

    totalPizzasDelivered = delToTwoTeam + delToThreeTeam + delToFourTeam

    # sort pizzas
    pizzas.sort(key=lambda x: x.nOfIngredients, reverse=True)  # Highest First

    result = []
    result.append(str(totalPizzasDelivered) + "\n")

    for i in range(delToFourTeam):
        result.append(str("4 {} {} {} {}".format(
            pizzas[0].pizzaType, pizzas[1].pizzaType, pizzas[2].pizzaType, pizzas[3].pizzaType)) + "\n")
        pizzas = pizzas[4:]

    for i in range(delToThreeTeam):
        result.append(str("3 {} {} {}".format(
            pizzas[0].pizzaType, pizzas[1].pizzaType, pizzas[2].pizzaType)) + "\n")
        pizzas = pizzas[3:]

    for i in range(delToTwoTeam):
        result.append(str("2 {} {}".format(
            pizzas[0].pizzaType, pizzas[1].pizzaType)) + "\n")
        pizzas = pizzas[2:]

    return result # not be changed
