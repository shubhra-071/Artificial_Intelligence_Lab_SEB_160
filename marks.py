Maths=int(input("Enter the marks of Maths:"))
Physics=int(input("Enter the marks of Physics:"))
Chemistry=int(input("Enter the marks of Chemistry:"))
Biology=int(input("Enter the marks of Biology:"))
English=int(input("Enter the marks of English:"))
avg=(Maths+Physics+Chemistry+Biology+English)/5
print(avg)
if avg>=90 and avg<100:
 print("first class\n")
elif avg>=70:
 print("second class\n")
elif avg>=50:
 print(" distinction\n")
elif avg>=35:
 print("pass\n")
else:
 print("fail\n")
