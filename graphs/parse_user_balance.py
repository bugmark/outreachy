import math
import numpy

balance_csv = "balances.csv"

daily_balance_csv = "parse_balance_log.csv"
# daily_earning_csv = "user_earning.csv"
# daily_freq_csv    = "user_freq.csv"

# (user, day) -> (balance, earningg, freq)
user_day = {}

users = []
days  = []

with open(balance_csv, "r") as file:
    file.readline()

    for line in file:
        _, _, _, day, email, _, bal, earn, freq = line.strip("\n").split(",")

        if email not in users:
            users.append(email)

        if day not in days:
            days.append(day)

        user_day[(email, day)] = (bal, earn, freq)


for user in users:
    for day in days:
        try:
            assert((user, day) in user_day.keys())
        except:
            print("Data is not complete")

            exit(1)

with open(daily_balance_csv, "w") as balance:

    header = "user\\day,{}".format(",".join(days))

    print(header, file=balance)
    # print(header, file=earning)
    # print(header, file=freq)

    for user_id, user in enumerate(users):
        print("user{} : {}".format(user_id, user))

        for file in [balance]:
            print("user{}".format(user_id), end="", file=file)

        for day in days:
            bal, earn, f = user_day[(user, day)]
            x=[float(i) for i in bal.split(' ')]
            #print(x)
            y=[numpy.log(j) for j in x]

            y=[u.tolist() for u in y]
            #print(type(y[0]))
            print(",{}".format(y[0]), end="", file=balance)
            #print(",{}".format(earn), end="", file=earning)
            #print(",{}".format(f), end="", file=freq)

        for file in [balance]:
            print("", file=file)
