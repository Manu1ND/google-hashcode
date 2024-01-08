import solver


def process(filename):
    input = open("input/" + filename + ".txt", "r")
    result = solver.solver(input)
    input.close()
    output = open("output/"+filename + ".txt", "w")
    output.writelines(result)
    output.close()
    print("{} done".format(filename))


filenames = ["a_example", "b_read_on", "c_incunabula",
             "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]

for filename in filenames:
    process(filename)
