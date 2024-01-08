class Project:
    def __init__(self, name, days, score, bestBefore, noRoles) -> None:
        self.name = name #string
        self.days = days #int
        self.score = score #int
        self.bestbefore = bestBefore #int
        self.roles = {} #dictionary of required roles
        n = noRoles