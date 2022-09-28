#fist box
a = 3 # 3red balls
b = 2 # 2white balls
#second box
c = 4 # 4red balls
d = 5 # 5white balls
#third box
e = 2 # 2red balls
f = 4 # 4white balls
b1 = 1/3
b2 = 1/3
b3 = 1/3
# red/total
x_b1 = a/(a+b) 
x_b2 = c/(c+d)
x_b3 = e/(e+f)
s = b2*x_b2
ss = (b1*(x_b1))+(b2*(x_b2))+(b3*(x_b3))
pa2_x = s/ss
print(pa2_x)