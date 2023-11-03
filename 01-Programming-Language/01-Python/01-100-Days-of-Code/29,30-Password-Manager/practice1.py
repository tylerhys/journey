try:
    file = open("afile.txt")
    dicts = {"key":1}
    print(dicts["das"])
except FileNotFoundError:
    print("file missing")
except KeyError as error_message:
    print(error_message)
else:
    content = file.read()
finally:
    print("Will print no matter what")
    raise TypeError("This is a fake error")
