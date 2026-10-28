s = "abcd"
k = 2
sinv= s[k-1::-1]
snor= s [k:]
s = sinv + snor
print(s)