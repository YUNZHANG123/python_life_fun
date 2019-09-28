# Question: get all the information of each friend 
# The information contains the friend's nickname, remarkname, and other aspects
# Purpose: practise the Python IO
# Sophia  20190914
import itchat

def save_to_txt():
    friends = parse_data(get_data())
    for item in friends:
        with open('friends_data.txt', mode='a', encoding='utf-8') as f: #4th step: create a file
            f.write('%s,%s,%d,%s,%s,%s,%d,%d\n' % (
                item['NickName'], item['RemarkName'], item['Sex'], item['Province'], item['City'], item['Signature'],
                item['StarFriend'], item['ContactFlag'])) #5th step: put information in the file


def get_data():
    itchat.auto_login() #1st step: login in WeChat
    friends = itchat.get_friends(update=True) #2nd step: get friends' info
    return friends

 
def parse_data(data):
    friends = []
    for item in data[1:]: 
        friend = {
            'NickName': item['NickName'],  
            'RemarkName': item['RemarkName'], 
            'Sex': item['Sex'], 
            'Province': item['Province'], 
            'City': item['City'],  
            'Signature': item['Signature'].replace('\n', ' ').replace(',', ' '), 
            'StarFriend': item['StarFriend'], 
            'ContactFlag': item['ContactFlag'] 
        }
        print(friend) #3rd step: put the info into a dictionary
        friends.append(friend)
    return friends

if __name__ == '__main__':
    save_to_txt() 