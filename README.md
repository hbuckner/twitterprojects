# twitterprojects
Messing around with Twitter API. 

Methods and examples of use:

# getlist(searchterm)
Description: searches term then adds users to list
input: String
@returns: List of ids

Example:  getlist("pinapple pizza")

# followbot(List)
Description: takes in list of user IDs and follows that list
input:list

Example: followbot(["johndoe","mr_geektastic","Emperorzoan"])

# checkifFriend(List,user_id)
Description:Checks to see if user is freinds with x if not unfollows user.
input:list, user_id
returns: username and time the user was unfollowed in a list

Example checkifFriend(["johndoe","mr_geektastic","Emperorzoan"],1234567")

# makeEven(UserID)
Description: gets all users user is following and checks to see if friends and if not, unfollows them
input: UserID of user whos following list you are checking

Example: makeEven("123456789")
