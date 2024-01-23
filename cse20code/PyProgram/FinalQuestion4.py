#FinalQuestion4 

filename = input("please enter a file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())

