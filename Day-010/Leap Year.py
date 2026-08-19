def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.

    if year % 4 != 0:
        return f"{year} is not a leap year."
    else:
        if year % 100 != 0:
            return f"{year} is a leap year!"
        else:
            if year % 400 != 0:
                return f"{year} is not a leap year."
            else:
                return f"{year} is a leap year!"


years = is_leap_year(int(input("Enter a year: ")))
print(years)