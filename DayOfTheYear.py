def dayOfYear(date):
    """
    :type date: str
    :rtype: int
    """

    daysPerMonth = [0,
                    31,
                    28,
                    31,
                    30,
                    31,
                    30,
                    31,
                    31,
                    30,
                    31,
                    30,
                    31]

    year = int(date[0] + date[1] + date[2] + date[3])
    month = int(date[5] + date[6])
    day = int(date[8] + date[9])

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            daysPerMonth[2] = 29
            return (sum(daysPerMonth[:month]) + day)

    else:
        return sum(daysPerMonth[:month]) + day


if __name__ == "__main__":
    date = "1900-05-02"


    print(dayOfYear(date))


