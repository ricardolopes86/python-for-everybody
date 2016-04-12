largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        inp = float(num)
    except:
        print "Invalid input"
        continue
        
    if largest is None:
        largest = num
    if smallest is None:
        smallest = num    
    if largest < num:
        largest = num
    if smallest > num:
        smallest = num

print "Maximum is ", largest
print "Minimum is ", smallest
From marquard@uct.ac.za