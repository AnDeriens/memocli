
# 発言者
print('発言者を選んでください')

people = ['aさん', 'bさん']
for i in range(len(people)):
    print(str(i + 1) + '.', people[i])

selected_person_num = int(input())
selected_person = people[selected_person_num - 1]

print('選ばれたのは', selected_person)

# 発言内容
print('発言内容を教えてください')

content = input()

# 保存
file_path = 'storage.csv'
with open(file_path, mode = 'a') as f:
    f.write(','.join([selected_person, content]))
    f.write("\n")

print('保存しました')
