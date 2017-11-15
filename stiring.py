s="I love to write python"
split_s=s.split()
print split_s
for x in split_s:
    y=x.find("i")
    if y>-1:
        print "I found 'i' in: '{0}'".format(y)
    
