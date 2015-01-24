from watson import WatsonRelationshipExtractionService, WatsonUserModelingService
import tweepy
from flask import Flask, request, jsonify
import os

app = Flask(__name__, static_url_path="")
auth = tweepy.OAuthHandler("xx", "xx")
auth.set_access_token("xx-xx",
                      "xx")

api = tweepy.API(auth)





userModeling = WatsonUserModelingService(url="xx", user="xx", password="xx")
relationshipExtration= WatsonRelationshipExtractionService(user="xx" ,password="xx")


@app.route('/')
def hello():
    return 'Hello from IOContext api!'


@app.route('/api/v1/timeline')
def timeline():
    public_tweets = api.home_timeline()
    return jsonify({'tweets': [tweet.text for tweet in public_tweets]})


@app.route('/api/v1/portrait/<screen_name>')
def getPortrait(screen_name):
    #tweets = api.user_timeline(id=screen_name,  )
    tweets = tweepy.Cursor(api.user_timeline, id=screen_name).items(200)
    text = ""
    for tweet in tweets:
        text += tweet.text + "\n " + "\n"
    portrait = userModeling.requestPortrait(text)
    return jsonify({'portrait': portrait})

@app.route('/api/v1/interests/<screen_name>')
def getRelationship(screen_name):
    #tweets = api.user_timeline(id=screen_name,  )
    tweets = tweepy.Cursor(api.user_timeline, id=screen_name).items(20)
    text = ""
    for tweet in tweets:
        text += tweet.text + "\n " + "\n"
    relationship = relationshipExtration.extractRelationship(text)
    return jsonify({'relationship': relationship})


@app.route('/api/v1/getPeople')
def searchUser():
    users = api.search_users(request.args['name'])
    return jsonify({'users': [
        {'name': user.name,
         'description': user.description,
         'profile_background_image_url': user.profile_background_image_url,
         'screen_name': "@"+user.screen_name
        } for user in users
    ]})


PORT = int(os.getenv('VCAP_APP_PORT', 8000))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(PORT), debug=True)

