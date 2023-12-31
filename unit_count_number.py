# I
while True:
    num_to_ctr = input("Enter a number to count its units: ").strip()
    num_to_ctr = num_to_ctr[::-1]
# 123579 --> 975321
    if num_to_ctr.isnumeric():
        counts = {}
        for ix, unit in enumerate(num_to_ctr):
            dict_key = "1" + ("0" * ix)
            counts[dict_key] = int(unit)
#        print("\n\t", counts)
        for key, value in counts.items():
            print(f"\t^{key:{len(num_to_ctr)}} u*->: {value}")
        print("")
    else:
        print("\n\tEnter a number!\n")
# II
while True:
    num_to_ctr = input("Enter a number to count its units: ").strip()
# 123579
    if num_to_ctr.isnumeric():
        num_len = len(num_to_ctr)
        num_to_ctr = int(num_to_ctr)
        counts = {}
        for step in range(num_len):
            unit = num_to_ctr % 10
            dict_key = "1" + ("0" * step)
            counts[dict_key] = unit
            next_step = num_to_ctr // 10
            num_to_ctr = next_step
#        print("\n\t", counts)
        for key, value in counts.items():
            print(f"\t^{key:{len(num_to_ctr)}} u*->: {value}")
        print("")
    else:
        print("\n\tEnter a number!\n")
# INPUT
#       Enter a number to count its units: 123579
# OUTPUT
#       {'1': 9, '10': 7, '100': 5, '1000': 3, '10000': 2, '100000': 1}
# or
#       ^1      u*->: 9
#       ^10     u*->: 7
#       ^100    u*->: 5
#       ^1000   u*->: 3
#       ^10000  u*->: 2
#       ^100000 u*->: 1
