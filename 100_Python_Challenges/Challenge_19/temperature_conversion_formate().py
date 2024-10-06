def to_celsius(temp):
    # C = (f-32)*5/9
    return (temp-32)*5/9
    #C = (f-32)*5/9
for temp in range(2,100,10):
    print("C={:.2f} | F={:.2f}".format(temp,to_celsius(temp)))