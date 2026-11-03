alp = [1,2,3,4]
r=[x*x for x in alp]
print(r)
alpha = [1,2,3,4,5,6,7,8,9,10]
even=[x for x in alpha if x%2==0]
print(even)
zlpha = [1,2,3,4,5,6,7,8,9,10]
div3=[x for x in zlpha if x%3==0]
print(div3)

print([x*x for x in range(1,21)])
print([x for x in range(1,25) if x%3==0])
list1=[3,6,9,12,15,18,21,24]
print([x for x in list1 if x%2==0])
list2 =["apple", "banana", "kiwi"]
print([f.upper() for f in list2])
list3 =["Ali", "Sara", "Ahsan", "Bilal"]
result =[name for name in list3 if name.startswith("A")]
print(result)
txt = "this is a book"
result = [word[0] for word in txt.split()]
print(result)
print([x for x in range(1,101) if x%3 and x%5 ==0 ])
list4= [0, 20, 30, 40]
print([x for x in list4 if 	(x * 9/5) + 32 == 0 ])
list4 = [0, 20, 30, 40]
result = [x for x in list4 if (x * 9/5) + 32 == 0]
print(result)
celsius = [0, 20, 30, 40]

fahrenheit = [round((c * 9/5) + 32, 1) for c in celsius]

print(fahrenheit)


fahrenheit = [ round((f * 9/5) + 32, 1) for f in range(1,101) ]
celsius = [c for c in range(1,101)]
combined= [(c,f) for c,f in zip(celsius,fahrenheit) ]
print(combined)


list5= [-5, 3, -1, 10, -20, 8]
r = [x for x in list5 if x >= 0 ]
print(r)



list6= [1,2,3,4]
ans = {x:x**2 for x in list6}
print(ans)