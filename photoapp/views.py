from django.shortcuts import render
from twitter import *
from tkinter import *

def MainHomePage(request):
    homepage = Homepage.objects.get(pk=1)
    context = {'homepage': homepage, 'tweets': getTweets()}
    return render_to_response('index.html', context, context_instance=RequestContext(request))
def getTweets():
    tweets = []
    try:
            import twitter
            api = twitter.Api()
            latest = api.GetUserTimeline('HackedExistence')
            for tweet in latest:
                status = tweet.text
                tweet_date = tweet.relative_created_at
                tweet.append({'status':status, 'date': tweet_date})
    except:
            tweets.append({'status': ' Follow us @RobertWilliamsJr', 'date': 'about 10 minutes ago'})
    return{'tweets': tweets}        
        
         
         

def index(request):
    return render(request, 'photoapp/home.html')


def tweet(request):
    return render(request, 'photoapp/home.html')
