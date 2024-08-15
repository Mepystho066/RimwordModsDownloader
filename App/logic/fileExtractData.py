
def ReadFile(inputFile):
    File =open(f"{inputFile}", "r")
    dataFile = File.read()
    dataFile = dataFile.split("\n")
    return dataFile