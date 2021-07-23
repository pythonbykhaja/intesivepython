f_no = 1
s_no = 2
print(f_no)
print(s_no)
result = 2
while True:
    t_no = f_no + s_no
    if t_no >= 4000000:
        break
    if t_no % 2 == 0:
        result += t_no # result = result + t_no
    print(t_no)
    f_no = s_no
    s_no = t_no
print()
print("Sum of even numbers till 4000000 is ", result)