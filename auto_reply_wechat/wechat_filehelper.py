import itchat

@itchat.msg_register(itchat.content.TEXT)

def print_content(msg):
    
    print(msg['Text'])

# This is code that enables the user to auto_login without scaning the code
itchat.auto_login(hotReload=True)


itchat.send(u'Text', 'filehelper')
itchat.run()
