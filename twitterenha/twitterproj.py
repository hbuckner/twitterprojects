import twitter
import time
from req import *
import datetime

api = twitter.Api(consumer_key=a,consumer_secret=b,access_token_key=c,access_token_secret=d,sleep_on_rate_limit=True)
api.VerifyCredentials()
'''
Description: searches term then adds users to list
input: String
@returns: List of ids
'''
def getlist(searchterm):
    results = api.GetSearch(
    term=searchterm,count=100,result_type="recent")
    idlist=[]
    idlist=[u.user for u in results]
    newlist=[u.screen_name.encode("utf-8") for u in idlist]
    return(newlist)

'''
Description: takes in list of user IDs and follows that list
input:list
'''
def followbot(List):
    for x in List:
        try:
            api.CreateFriendship(user_id=x)
        except:
            print("trying again")
'''
Description:Checks to see if user is freinds with x if not unfollows user.
input:list, user_id
returns: username and time the user was unfollowed in a list
'''
def checkifFriend(List,user_id):
    returnlist=[]
    userdelete=[]
    for x in List:
        #   print(api.ShowFriendship(source_user_id=173834439,target_screen_name=x)['relationship']['target']['following'])
        if api.ShowFriendship(user_id,target_screen_name=x)['relationship']['target']['following'] == False:
            try:
                api.DestroyFriendship(screen_name=x)
                userdelete=[x,str(datetime.datetime.now().date()),datetime.datetime.now()]
                returnlist.append(userdelete)
                #print(userdelete)
                print("friendship with "+x+" is being destroyed")
            except:
                raise
                break
    return(returnlist)
    #print(returnlist)
'''
Description: gets friends of user checks to see if friends if not, returns list of people who unfollowed and at what date
'''
def makeEven(UserID):
    try:
        users=api.GetFriends()
        friendids=[u.screen_name for u in users]
        Friend = checkifFriend(friendids,UserID)
        #print(Friend)
        return(Friend)
    except:
        raise
