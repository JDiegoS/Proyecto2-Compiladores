class Quadruple():
    def __init__(self):
        self.temp = 0
        self.loop = 0
        self.quadTable = []

    def newTemp(self):
        self.temp += 1

    def newLoop(self):
        self.loop += 1

    def generateQuadruple(self, op, arg1, arg2, result):
        self.quadTable.append({'op': op, 'arg1': arg1, 'arg2': arg2, 'result': result})