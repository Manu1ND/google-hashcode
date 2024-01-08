import solver


def process(filename):
    input = open("input/" + filename + ".txt", "r")
    result = solver.solver(input)
    input.close()
    output = open("output/"+filename + ".txt", "w")
    output.writelines(result)
    output.close()
    print("{} done".format(filename))


filenames = ["a_example", "b_lovely_landscapes",
             "c_memorable_moments", "d_pet_pictures", "e_shiny_selfies"]

for filename in filenames:
    process(filename)
