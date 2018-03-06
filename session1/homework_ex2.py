# Create a new Python file with the following statements in it, then run it.
# Were the things that were printed what you expected to see?

a = 1
a = a + 1
print a # Expect 2
b = "hello"
print b # Expect hello
c = b.title()
print b # Expect hello
print c # Expect Hello
d = "hello"
e = d.title()
print d # Expect hello
print e # Expect Hello
name = "Dave"
f = "Hello {0}! ".format(name)
print f # Expect Hello Dave
name = "Sarah"
print f # Expect Hello Dave
print f * 5 # Expect Hello Dave!Hello Dave!Hello Dave!Hello Dave!Hello Dave!
