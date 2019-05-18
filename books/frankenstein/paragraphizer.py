import os
import glob
import re

working_dir = os.getcwd()
# print(working_dir)
p_graphs = []


for filenumber, filename in enumerate(sorted(glob.glob(os.path.join("./", "*.txt")))):
    with open(filename, 'r',) as f:
        data = f.read()
        split = data.split("\n\n")
        for number, paragraph in enumerate(split, 1):
            p_graphs += [paragraph]
            with open("Chap_{}_par_{}".format(filenumber + 1, number) + ".txt","w") as x:
                if paragraph is not '':
                    x.write(paragraph)
                    x.close()



for p in p_graphs:
    print(p)
    print


# for x in p_graphs:
#     print(x)
#     print()
#
