f = open("test.txt")
content = f.readlines()
f.close()
print "".join(content)

print("\n")
g = open("test2.txt", "w")
g.write("".join(content))
g.write("\nsomething new")
g.close()

f = open("test2.txt")
content = f.readlines()
f.close()
print "".join(content)
