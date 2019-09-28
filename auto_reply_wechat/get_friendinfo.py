import itchat



@itchat.msg_register(itchat.content.TEXT)

def print_content(msg):
    
    return (msg['Text'])
itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)
print(friends[0:2])
itchat.run()