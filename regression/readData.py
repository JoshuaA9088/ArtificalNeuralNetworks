
def getData(filename):
    """
    Read X Y data into list
    """
    data = []
    f = open(filename)
    for line in f:
        line = line.split()
        for i in range(len(line)):
            line[i] = float(line[i])
        data.append(line)
    return data
