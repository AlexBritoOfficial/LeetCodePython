def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    record = []
    for element in operations:

        match element:
            case "+":
                record.append(record[-1]+record[-2])
            case "D":
                record.append(record[-1] * 2)
            case "C":
                record.pop()
            case _:
                record.append(int(element))
    return sum(record)

if __name__ == "__main__":
    ## ops = ["5", "2", "C", "D", "+"]
    ops = ["61","-50","65","+","D","-99","-58","88","19","-11"]
    print(calPoints(ops))
