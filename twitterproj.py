import twitter
import time
from req import *

api = twitter.Api(consumer_key=a,consumer_secret=b,access_token_key=c,access_token_secret=d,sleep_on_rate_limit=True)
api.VerifyCredentials()
'''
Description: searches term then follows users
input: String
@returns: List of ids
'''
def getlist(searchterm):
    results = api.GetSearch(
    term=searchterm,count=100)
    idlist=[]
    idlist=[u.user for u in results]
    newlist=[u.screen_name.encode("utf-8") for u in idlist]
    return(newlist)

'''
Description: takes in list of user IDs and follows that list
input:list
'''
def followthot(List):
    for x in List:
        try:
            api.CreateFriendship(user_id=x)
        except:
            print("trying again")
'''
Description:Checks to see if user is freinds with x if not unfollows user.
input:list, user_id
'''
def checkifFriend(List,user_id):
    for x in List:
        #   print(api.ShowFriendship(source_user_id=173834439,target_screen_name=x)['relationship']['target']['following'])
        if api.ShowFriendship(user_id,target_screen_name=x)['relationship']['target']['following'] == False:
            try:
                api.DestroyFriendship(screen_name=x)
                print("friendship with "+x+" is being destroyed")
            except:
                print("there was an issue with ")

'''
Description: gets friends of user checks to see if friends if not, unfollows them
'''
def makeEven():
    try:
        users=api.GetFriends()
        friendids=[u.screen_name for u in users]
        checkifFriend(friendids,"173834439")
    except:
        print("there is issue in makeEven")


def main():
    #search name
    while(True):
        searching=getlist("Developer")
    #follow who tweets about search term
        followthot(searching)
        print("following")
        print(searching)
    #wait 1 hour
        #time.sleep(600)
        checkifFriend(searching)
    #check to see if they followed back if not unfoll)ow

makeEven()
#main()
