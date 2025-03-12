#Store the walk time in a variable called a.
a=15
#Store the bus time in a variable called b.
b=75
#Store the total length of time for this commute in a third variable called c.
c=a+b
#store the drive time in a variable called d.
d=90
#store the walk time in a variable called e.
e=5
#store the total length of time in a variable called f.
f=d+e
#compare c and f.
c>f
False
#f is bigger. so driving takes more time.
4.2
#create variable X and X should be True.
X=True
#create variable Y and Y should be False.
Y=False
#create a new variable called W which encodes the Boolean variable ‘both X and Y’. 
W = X and Y
#create the truth table of W.
print(W)
X=not X
W = X and Y
print(W)
Y=not Y
W = X and Y
print(W)
X=not X
W=X and Y
print(W)