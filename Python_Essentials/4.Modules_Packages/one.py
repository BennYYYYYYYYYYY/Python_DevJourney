print("We are running codes in one.py now.")

def get_name():
    print(__name__)


if __name__ == "__main__":
    print("We are running codes in directly.")
else:
    print("one.py is imported")
    get_name()

    


