class Tape:

    def __init__(self, file, mode):
        self.file = open(file, mode)
        self.path = file
        self.mode = mode

    def reopen(self, mode):
        if mode:
            self.mode = mode
        self.file.close()
        self.file = open(self.path, self.mode)

    def read(self):
        nums = ""
        digit = self.file.read(1)
        if digit == "" or digit == "\n":
            self.current = digit
            return digit
        while digit != " " and digit != "\n":
            nums += digit
            digit = self.file.read(1)
        self.current = nums
        return nums

    def write(self, num_2):
        self.file.write(num_2)
        self.current = num_2

def reopen(tapes, mode):
    for i in range(mode * 2, mode * 2 + 2):
        tapes[i].reopen('r')
    for i in range(((mode + 1) % 2) * 2, ((mode + 1) % 2) * 2 + 2):
        tapes[i].reopen('w')

def bubble(list_2):
    for i in range(len(list_2) - 1):
        for j in range(len(list_2) - i - 1):
            if list_2[j] > list_2[j + 1]:
                cushion = list_2[j]
                list_2[j] = list_2[j+1]
                list_2[j+1] = cushion
    return list_2