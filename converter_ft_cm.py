from re import findall
while True:
    ft = input("Enter ft: ").strip()
    if findall('[^0-9.]', ft) or ft == '0' or ft == '.' or ft in '':
        print("Enter a correct number!")
    else:
        print(ft, "ft is", round(float(ft) * 30.48, 2), "cm" "\n")
        while True:
            another_choise = input("Another value to measure? 'y' for 'Yes', any other key for 'No'\n").lower().strip()
            if another_choise == "y":
                break
            else:
                print("\nSee ya again!")
                exit()
