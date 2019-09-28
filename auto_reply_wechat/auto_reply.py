import itchat



@itchat.msg_register(itchat.content.TEXT)

def print_content(msg):
    
    return (msg['Text'])


# This function is the API to login 
# "hotReload=True" means we can login next with cache
itchat.auto_login(hotReload=True)

itchat.run()