class Needle:
    myList=["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

    # def __init__(self):
    #     self.myList

    def findNeedle(self):
        for i in range(len(self.myList)):
            if self.myList[i]=='needle':
                return(f"found the needle at position{[i]} ")

needleOne=Needle()
print(needleOne.findNeedle())


