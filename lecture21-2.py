blank_numbers = [4, 3, 2, 1, 0]
star_numbers = [1, 3, 5, 7, 9]

for blank in blank_numbers:
    for star in star_numbers:
        print("{}{}".format(" " * blank, "*" * star))