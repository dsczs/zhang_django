try:
    fh = open("t1.txt", "w")
    fh.write("abc")
except Exception:
    print("exception")
