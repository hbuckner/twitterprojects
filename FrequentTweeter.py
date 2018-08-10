#get how often a user uses a word

import pandas
import twitter


def wordFinder(string, word):

    if word in string:
        return 1
    else:
         return 0
def tweetJudgement(username,word,cutoffNumber):
    api = twitter.Api(consumer_key="pCYVRXIzdFYlFZPtFc06kDDaX",
                      consumer_secret="ohsw6Dg6VJzylI1HJiUv6MZgJXpCdaPnWVS7yF57cQ8dUM6Qc7",
                      access_token_key="173834439-Hwj5oyhrrWr5zcHwo5JfMuuQdV1Df0bbZHK661cr",
                      access_token_secret="bDmaVqSjYbQHPCLk92hqqzH5ZlF3dyoRbbPy2iVGNHx8n"
                      )
    results = api.GetUserTimeline(screen_name=username, count=100)
    #print(api.VerifyCredentials())
    tweets =[i.AsDict() for i in results]
    file = open("tweets.txt", "w+", encoding='utf-8')
    number=0
    for i in tweets:
        line = i['id'], i['text']
        file.write(str(line)+"\n")
        number = number + wordFinder(str(line),"the")
        print(number)
    if number >= cutoffNumber:
        print(True)
        return True
    else:
        print(False)
        return False
tweetJudgement("mr_geektastic", "word",390)
#print([s.text for s in statuses])
