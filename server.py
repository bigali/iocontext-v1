from watson import WatsonRelationshipExtractionService, WatsonUserModelingService
import tweepy
from flask import Flask, request, jsonify
import os

app = Flask(__name__, static_url_path="")
auth = tweepy.OAuthHandler("VGbGua2zcrvAt8q7rFzYcF7Pp", "LC7DxOcHjzaoHH61MjlWwJvkERWhvnNIHKIasvvvDq9i3J8fGf")
auth.set_access_token("273164662-rcIu2uf0crCAolbKpGJETrU9iMc5XhDHjEo2Oupq",
                      "QxjyYfMQlK83GqwxVZmD4AZFIjtVNTbALFmrGLFdfjfjo")

api = tweepy.API(auth)





userModeling = WatsonUserModelingService(url="https://gateway.watsonplatform.net/systemu/service/",user="072abbf5-28cd-48e8-920a-cd147fb83578", password="CQjtluCopyFo")
relationshipExtration= WatsonRelationshipExtractionService(user= "d9d905bb-70f9-42a0-9200-2db9e5c6af69",password= "btOvBRXxU2A6")


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

