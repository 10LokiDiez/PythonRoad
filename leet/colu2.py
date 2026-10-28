out = []
m =11
n=3

for i in range(m):
    stri = ""
    if i == 0:
        stri = "." * n
    else:
        stri = ("#" * (n-1)) + "."
    out.append(stri)
    
print(out)