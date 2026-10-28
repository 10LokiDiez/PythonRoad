out = []
m =11
n=3
if m != 1 or n != 1:
    for i in range(m):
        stri = ""
        for j in range (n):
            if i == j or i+1 ==j:
                stri += "."
            else:
                stri += "#"
        out.append(stri)
elif m == 1 :
    for i in range(n):
        out.append(".")
elif n == 1:
    stri = "." * m
    out.append(stri)
        

for line in out:
    print(line)