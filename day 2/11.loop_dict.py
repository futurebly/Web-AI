# members = [
#     ['egoing', 'Seoul', 'Web'],
#     ['leezhe', 'Jeju', 'Design']
# ]

# print(members[0][1])
# for member in members:
#     print(member[0], member[1], member[2])

# member = {'name':'egoing', 'city':'seoul', 'job':'web'}
# print(member['name'])
# print(member['city'])

members = [
    {'name':'egoing', 'city':'seoul', 'job':'web'},
    {'name':'leezche', 'city':'jeju', 'job':'design'}
]
# print(members[0]['city'])
for member in members:
    print(member['name'], member['city'], member['job'])