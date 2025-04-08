import os 

def main():
    i =4
    path = "D:/D drive Data/assignment04-rizwana/assignment01/online-projects/6-Bulk-file-rename/test/"
    if not os.path.exists(path):
        print(f"Error: The directory '{path}' does not exist.")
        return
    for filename in os.listdir(path):
        my_dest = "image" + str(i) + ".jpg"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == "__main__":
    main()