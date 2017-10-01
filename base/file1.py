try:
    fh = open("t1.txt", "a")
    fh.write("\nabc")
except Exception:
    print("exception")
finally:
    fh.close()
