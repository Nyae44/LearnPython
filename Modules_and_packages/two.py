import one

print("TOP LEVEL IN two.py")

one.func()

if __name__ == "__main__":
    print("TWO.PY IS BEING RUN DIRECTLY")
else:
    print("Two.py has been imported")