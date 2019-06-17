import os

#    Simple utility to create a series of folders in a given directory labelled 2007 - 2019.

path = "C:\\" #input("Enter primary directory name: ")

for i in range(7, 20):   #  Change range and strings to modify for own dates.

    if i < 10:
        folder = "200"+str(i)
    else:
        folder = "20"+str(i)


    try:
        os.mkdir(folder)
        print("Created {}".format(folder))

    except:
        pass
