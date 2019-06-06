class CalUtils:
    def __init__(self):
        self.names = []
        self.heights = []
        self.TotalStudentHeight = 0
        self.TotalStudentCount = 0

    def inclusive(self):
        with open('listOfStudentHeight.txt', "r") as d:
            for line in d:
                d = line.split("\t")
                name = d[0]
                height = d[1]
                self.names.append(str(name))
                self.heights.append(float(height))

    def calAvgHeight(self):
            self.TotalStudentCount = (len(self.names))
            self.TotalStudentHeight = (sum(self.heights))
            average = sum(self.heights)/len(self.names)
            print(f"Student average height is {round(average,2)}m(rounded off to 2 decimal place) for {self.TotalStudentCount} students.")

h = CalUtils()

ExtraInfo = input("Do you have extra info of new students to add? (YES/NO): ").upper()

if ExtraInfo == "NO":
    h.inclusive()
    h.calAvgHeight()

elif ExtraInfo == "YES":
    updated_name = str(input("Enter New Name: "))
    while True:
        try:
            updated_height=float(input("Enter New Height: "))
            break
        except:
            print("Enter Numbers only")

    with open('listOfStudentHeight.txt', "a") as d:
        d.write(f"\n{str(updated_name).upper()}\t{float(updated_height)}")
    h.inclusive()
    h.calAvgHeight()

else:
    print("Please enter only either Yes or No. ")