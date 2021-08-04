total_marks = 600
acheived_marks = 544
average = (acheived_marks/total_marks) * 100

if 90 <  average <= 100:
    print('A1')
elif 80 <= average <= 90:
    print('A2')
elif 70 <= average <= 80:
    print('B1')
elif 60 <= average <= 70:
    print('B2')
elif 50 <= average <= 60:
    print('C1')
elif 40 <= average <= 50:
    print('C2')
elif 32 <= average <= 40:
    print('D')
elif 20 <= average <= 32:
    print('E1')
elif 0 <= average <= 20:
    print('E2')
else:
    print('average should in range of 0-100')