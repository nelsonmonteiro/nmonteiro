import re

input_dict = {
    1: "f2 + f5",
    2: "5 - f4",
    3: "f1 * f2",
    4: "x",
    5: "90 + 1"
}

pattern = re.compile("f\d+")


def get_merged_formula(input_dict, formula_id):
    func = input_dict[formula_id]
    functions = re.findall("f\d+", func)

    for f in functions:
        print func, input_dict[int(f[1:])], functions
        func.replace(f, get_merged_formula(input_dict, int(f[1:])))


print get_merged_formula(input_dict, 1)



