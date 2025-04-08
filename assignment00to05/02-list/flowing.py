def add_copies(list, data):
    for i in range(5):
        list.append(data)

def my_message():
    messag = input("Write your message:")
    list = []
    print(list, "before")
    add_copies(list, messag)
    print(list, "after")

if __name__ == "__main__":
    my_message() 
