def read_a_file(filename):
    with open(file_name, "r") as file:
        print(file.readlines()[2])




if __name__ == "__main__":
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"

    read_a_file(file_name)