import solver


def process(filename):
    input = open("input/" + filename + ".in.txt", "r")
    result = solver.solver(input)
    input.close()
    output = open("output/" + filename + ".txt", "w")
    output.writelines(result)
    output.close()
    print("{} done".format(filename))


filenames = ["a_an_example", "b_better_start_small", "c_collaboration", "d_dense_schedule", "e_exceptional_skills", "f_find_great_mentors"]

for filename in filenames:
    process(filename)
