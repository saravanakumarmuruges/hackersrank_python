if __name__ == '__main__':
    s = input()
    
    if any(a.isalnum() for a in s):
        print(True)
    else:
        print(False)

    if any(a.isalpha() for a in s):
        print(True)
    else:
        print(False)

    if any(a.isdigit() for a in s):
        print(True)
    else:
        print(False)
    
    if any(a.lower() for a in s):
        print(True)
    else:
        print(False)
    if any(a.upper() for a in s):
        print(True)
    else:
        print(False)