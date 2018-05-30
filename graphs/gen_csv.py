import os

data_file  = "datafast.txt"
clean_file = "cycles.txt"

os.system("grep -v Cross {} >{}".format(data_file, clean_file))

with open(clean_file, "r") as file:
    for line in file:
        cycles, time, offers, contracts, escrows = line.split(" | ")

        cycles    = cycles.replace("Cycle: ", "")
        offers    = offers.replace(" open offers", "")
        contracts = contracts.replace(" contracts", "")
        escrows   = escrows.replace(" escrows", "")

        print("{},{},{},{}".format(cycles, offers, contracts, escrows), end="")

