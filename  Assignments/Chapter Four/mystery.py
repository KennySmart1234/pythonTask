
#[1, 2, 3, 4, 5] when it loop through all the value it will return 55 as the final output


def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y   
