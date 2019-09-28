# Question: get the profile pictures of all friends in WeChat
# Purpose: practise the Python IO
# Sophia  20190914
if __name__ == '__main__':
    itchat.auto_login(hotReload=True) #1st step: auto_login
    friends = itchat.get_friends(update=True)

    for i, val in enumerate(friends ):
        with open(str(i) +".png", "wb") as f:
            img = itchat.get_head_img(val["UserName"])                    
            f.write(img) #2nd step: get pictures