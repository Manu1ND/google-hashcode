import solver


def process(filename):
    input = open("input/"+filename + ".in", "r")
    result = solver.solver(filename, input)
    input.close()
    output = open("output/"+filename + ".out", "w")
    output.writelines(result)
    output.close()


filenames = ["a_example", "b_little_bit_of_everything",
             "c_many_ingredients", "d_many_pizzas", "e_many_teams"]
for filename in filenames:
    process(filename)
