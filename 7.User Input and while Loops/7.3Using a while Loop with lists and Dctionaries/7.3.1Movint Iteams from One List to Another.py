#confirmed_users.py
#首先，创建一个待验证的用户列表
#和一个用于储存已验证用户的空列表
unconfirmed_users = ['user1','user2','user3']
confirmed_users = []
#验证每个用户，知道没有未验证用户为止
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
#显示所有已验证的用户
print("\nThe following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())