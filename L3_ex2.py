import os


def ex2():

    # Ask the user
    print("Choose a number: ")
    total_files = input()
    files = []

    # Create loop variable
    n_total_files = int(total_files)

    # get the name
    print("Insert the name of the files:")
    for k in range(n_total_files):

        print("Name of the file " + str(k+1) + ":")

        name_file = input()

        files.append(name_file)

    # Store
    for k in range(n_total_files):
        name = "ffmpeg -i {} ".format(files[k])

    # Add name
    name = str(name + ".mp4")
    os.system(name)


if __name__ == "__main__":

    ex2()
