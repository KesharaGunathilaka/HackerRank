def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True

    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    # Write your logic here

    return leap


year = 2000  # int(input())
print(is_leap(year))
