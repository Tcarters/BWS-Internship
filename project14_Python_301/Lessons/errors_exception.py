
try:
    total = 1 / 0
    # this will not execute

    print ( " Trying 1 / 0 ")
except Exception:
    print ( "Execption was caught ")
    total = 0


print ( total )

print ( int (input ("What is a number ? ")))