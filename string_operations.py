
a = "hello, My name is samuel"
b = "Soloman Is My Brother"
c = "12, im from space Sharon"
d = " this sentence starts with space"

# print(a.capitalize())
# print(b.capitalize())
# print(c.capitalize())
# print(d.capitalize())

# print(a.title())
# print(b.title())
# print(c.title())
# print(d.title())

# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

e = "a& b& c& d& e&"
print(e)

print(e.split("&"))

print(e.split("&", 2))

print(e.split("&", 4))

f = "S, A, M, U, E, L"

print(f.split(",", 3))

g = "this is a sentence"
# print(g.rindex("v"))
# print(g.index("v"))

print(g.find("e", 12, 18))
print(g.rfind("e"))

print(g.center(30, "$"))

print(g[::-1])

print(g.index(0))