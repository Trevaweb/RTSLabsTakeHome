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

    def stringRotation(self, ogString, rotation):
        #build a string with the end rotation amount prepended to the begining of the original string minus the end rotation amount
        newString = ogString[-rotation:] + ogString[:-rotation]
        return newString

if __name__ == '__main__':
    x = RTSTakeHome()
    x.aboveBelow([1, 6, 2, 1, 10], 6)
    x.stringRotation("test this string", 5)
