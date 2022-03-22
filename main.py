colorCode = input().split()

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white']

tolerences = {"brown": "1%", "red":"2%", "orange":"3%", "yellow":"4%", "green":"0.5%", "blue":"0.25%", "violet":"0.1%", "grey":"0.05%", "gold":"5%"}

if len(colorCode) == 3:
    resValue = int(str(colors.index(colorCode[0])) + str(colors.index(colorCode[1]))) * (10 ** colors.index(colorCode[2]))
    print("Value = ", resValue)

if len(colorCode) == 4:
    resValue = int(str(colors.index(colorCode[0])) + str(colors.index(colorCode[1]))) * (10 ** colors.index(colorCode[2]))
    print("Value = ", resValue)
    print("Tolerence = ", tolerences[colorCode[-1]])
    

