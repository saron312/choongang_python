olympic =[[1,'미국',46,37,38,121],
          [2,'영국',27,23,17,67],
          [3,'중국',26,18,26,70],
          [4,'러시아',19,18,19,55],
          [5,'독일',17,10,15,42],
          [6,'일본',12,8,21,41],
          [7,'프랑스',10,18,14,42],
          [8,'대한민국',9,3,9,21]]
#print(olympic[0][1],'금은동 메달 개수:',olympic[0][2:5])
#print(olympic[:4])
for row in olympic:
    print(row[:2])
    
print('금메다라보다 동메달이 더 많은 나라')
for row in olympic:
    if row[2] < row[4]:
        print('=>'+row[1])
        
print('1위부터 8위까지 모든 국가가 획득한 금메달 개수의 합')
total_gold = 0
for row1 in olympic:
    total_gold += row1[2]
print(total_gold)

for row2 in olympic:
    gold = row2[2]/row2[-1]*100
    if gold>40:
        print(row2[1],gold,'%')