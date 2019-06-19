import os



path = os.getcwd() #input("Enter primary directory name: ")

for i in range(7, 20):

    if i < 10:
        folder = "200"+str(i)
    else:
        folder = "20"+str(i)


    try:
        os.mkdir(folder)
        print("Created {}".format(folder))

    except:
        pass
