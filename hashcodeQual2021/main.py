import solver


def process(filename):
    input = open("input/" + filename + ".txt", "r")
    result = solver.solver(input)
    input.close()
    output = open("output/" + filename + ".txt", "w")
    output.writelines(result)
    output.close()
    print("{} done".format(filename))


filenames = ["a", "b", "c", "d", "e", "f"]

for filename in filenames:
    process(filename)
