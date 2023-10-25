if __name__ == '__main__':
    n = int(input())
    out = ""
    if n<=150:
        for i in range(1,n+1):
            out = out+ str(i)
        print(out)
    else:
        print("Number is greated than 150")