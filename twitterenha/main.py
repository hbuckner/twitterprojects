from twitterproj import *
from textblob import TextBlob

''' get tweets of the days in which the user was unfollowed '''
def main():
    Flist = makeEven("173834439")
    tweet=[]
    listoftweets=[]
    my_time = datetime.datetime.strptime('01/01/70', '%m/%d/%y')
    for x in Flist:
        date = x[1]
        time=x[2]
        #print(date)
        results =api.GetSearch(term="mr_geektastic",since = date,result_type="recent")
        #print(results.ID)
        #print(tweetTimeStamp)
        for u in results:
            timeinseconds=u.created_at_in_seconds
            tweetTimeStamp = my_time+datetime.timedelta(seconds=int(timeinseconds)-18000)
            print(str(u.text))
            if tweetTimeStamp > time-datetime.timedelta(hours=24):
                blob=TextBlob(str(u.text))
                tweet=[blob.sentiment[0],blob.sentiment[1],"tweet: "+str(u.text)]
                listoftweets.append(tweet)
    listoftweets.sort(key=lambda listoftweets: listoftweets[0])
    print(listoftweets)
    return listoftweets

main()
#results =api.GetSearch(term="mr_geektastic",since = "2019-01-14",result_type="recent")

#timeinseconds=[u.created_at_in_seconds for u in results]
#my_time = datetime.datetime.strptime('01/01/70', '%m/%d/%y')
#new_datetime = my_time+datetime.timedelta(seconds=int(timeinseconds[0])-18000)
#print(new_datetime)
#print([u.created_at_in_seconds for u in results])
