class Averages:
    def __init__(self, inputdata):
        self.numberlist = inputdata.copy()

    def mean(self):
        return sum(self.numberlist)/len(self.numberlist)

    def median(self):
        list_length = len(self.numberlist)
        sorted_numbers = sorted(self.numberlist)
        if list_length % 2 == 0:
            firstnumber = sorted_numbers[list_length // 2]
            secondnumber = sorted_numbers[list_length // 2 - 1]
            return (firstnumber + secondnumber) / 2
        else:
            return sorted_numbers[list_length // 2]


avgs = Averages([5, 10, 15, 1000, 1])
print(avgs.mean())
print(avgs.median())
