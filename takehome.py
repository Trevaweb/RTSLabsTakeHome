class RTSTakeHome:

    def aboveBelow(self, intList, comparison):
        aboveBelowDict = {"above" : 0, "below" : 0}

        for num in intList:
            if num > comparison:
                aboveBelowDict["above"] += 1
            #num could equal comparison so also check to make sure it is below comparison
            #instead of using an else here
            elif num < comparison:
                aboveBelowDict["below"] += 1

        return aboveBelowDict

if __name__ == '__main__':
    x = RTSTakeHome()
    x.aboveBelow([1, 6, 2, 1, 10], 6)


