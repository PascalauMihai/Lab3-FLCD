from HashTable import HashTable


def isSymbol(givenCharacter):
    if givenCharacter in "[]{}()!=-+*/\\;:'\",<.>&|%":
        return True
    return False


class Scanner:
    def __init__(self, givenProgramFileName, givenTokensFileName):
        self.__programFileName = givenProgramFileName
        self.__tokensFileName = givenTokensFileName
        self.__tokensList = {}
        self.readAndCreateTokensList()
        self.__PIF = []
        self.__symbolTable = HashTable(100)
        print(self.__tokensList)

    def readAndCreateTokensList(self):
        with open(self.__tokensFileName, 'r') as filePath:
            next(filePath)
            next(filePath)
            currentLine = filePath.readline()
            while currentLine:
                name, code = currentLine.split(" -> ")
                if code[-1] == '\n':
                    code = code[:-1]
                if name == "Space":
                    self.__tokensList[' '] = -1
                elif name == "identifier":
                    self.__tokensList[name] = 0
                elif name == "constant":
                    self.__tokensList[name] = "constant"
                else:
                    self.__tokensList[name] = -1

                currentLine = filePath.readline()

    def scanProgram(self):
        with open(self.__programFileName, 'r') as filePath:
            currentLine = filePath.readline()
            index = 0
            while currentLine:
                print(currentLine)
                currentElement = ""
                if currentLine[index].isalpha():
                    while currentLine[index] != '\n' and currentLine[index].isalpha():
                        currentElement += currentLine[index]
                        index += 1
                    if currentElement in self.__tokensList:
                        self.__PIF.append([currentElement, self.__tokensList[currentElement]])
                    else:
                        while currentLine[index] != '\n' and currentLine[index].isdigit():
                            currentElement += currentLine[index]
                            index += 1
                elif currentLine[index].isdigit():
                    while currentLine[index] != '\n' and currentLine[index].isdigit():
                        currentElement += currentLine[index]
                        index += 1
                elif isSymbol(currentLine[index]):
                    while currentLine[index] != '\n' and isSymbol(currentLine[index]):
                        currentElement += currentLine[index]
                        index += 1
                else:
                    # throw exception - unknown symbol
                    pass
                print(currentElement)
                print(self.__PIF)
                print(currentLine[index])
                if(currentLine[index] == '\n'):
                    return

def run():
    scanner = Scanner("program.txt", "token.in")
    scanner.scanProgram()


run()
