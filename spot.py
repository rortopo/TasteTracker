import os

from flask import Flask, jsonify, request, session, redirect, url_for, render_template

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
import hugg

hugbot = hugg.hugCommands("rorycavanmc@gmail.com", "wnVmBwCsUuThM2")




app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

client_id = '0d17cf42d40a48bea802aef127087548'
client_secret = '7afa8777c069421492d72d1d57de49a1'
redirect_uri = 'http://localhost:8080/callback'
scope = 'playlist-read-private user-library-read user-top-read'

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret= client_secret,
                        redirect_uri=redirect_uri,
                        scope=scope,
                        cache_handler=cache_handler,
                        show_dialog=True)
sp = Spotify(auth_manager=sp_oauth)


@app.route('/')
def home():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('poop'))


@app.route('/homefr')
def homefr():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    ape = "hellodidididid"
    #return "welcome to my page <a href='/get_songs'>get top_songs</a>"
    return redirect(url_for('get_songs'))




@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('homefr'))


@app.route('/get_playlists')
def get_playlists():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)

    playlists = sp.current_user_playlists()
    playlists_info = [(pl['name'], pl['external_urls']['spotify'])
                      for pl in playlists['items']]
    playlists_html = '<br>'.join([f'{name}:{url}' for name, url in playlists_info])
    return jsonify(playlists_html)


def get_songs1(songs: str):
    biasPrompt = "Pretend that you are a pretentious record store owner. You only like music that says something profound about the person who listens to it. The more obscure the artist, the better. This means that you prefer songs with fewer listens. You will be given a list of 50 songs, and deduce how much you like the collection as a whole, giving it a score of 0-10. 10 is a high score, meaning you liked it, while 0 means you did not. Be SUPER PRETENTIOUS. Give an integer as the first word of the answer. If you do not give an integer first, the machine will break."
   
    rating  = hugbot.pretentious_score(biasPrompt, songs)

    

    

    return rating



def get_preten(songs: str) -> str:
    biasPrompt = "Pretend that you are a pretentious record store owner. You only like music that says something profound about the person who listens to it. The more obscure the artist, the better. This means that you prefer songs with fewer listens. You will be given a list of 50 songs, and deduce how much you like the collection as a whole, giving it a score of 0-10. 10 is a high score, meaning you liked it, while 0 means you did not. Be SUPER PRETENTIOUS. Give an integer as the first word of the answer seperated by a space. If you do not give an integer first, the machine will break."

    rating = hugbot.pretentious_score(biasPrompt, songs)

    return rating

def get_radio(songs: str) -> str:
    biasPrompt = "Pretend that you are a young college radio station employee. You love to hear new music all the time, appreciating variation across genres. If someone has genre stagnation, or not many, you dislike that. If someone listens to many different genres, you appreciate that. You will be given a list of 50 songs, and deduce how much you like the collection as a whole, giving it a score of 0-10. 10 is a high score, meaning you liked it, while 0 means you did not. Give an integer as the first word of the answer seperated by a space, explaining why afterwards"

    rating = hugbot.pretentious_score(biasPrompt, songs)

    return rating
    

def get_ringo(songs: str) -> str:
    biasPrompt = "Pretend you are Ringo Starr, the drummer for the Beatles. You love to have a good time. You will be given a list of 50 songs, and deduce how much you like the collection as a whole, giving it a score of 0-10. 10 is a high score, meaning you liked it, while 0 means you did not. Give an integer seperated by a space as the first word of the answer. If you do not give an integer first, the machine will break."

    rating = hugbot.pretentious_score(biasPrompt, songs)

    return rating

def get_batman(songs:str) -> str:
    biasPrompt = "Pretend you are Batman. You are dark brooding and mysterious in your conversation and interests. In music, you prefer heavier chords, and slow tempo. You will be given a list of 50 songs, and deduce how much you like the collection as a whole, giving it a score of 0-10. 10 is a high score, meaning you liked it, while 0 means you did not. Give an integer seperated by a space as the first word of the answer. If you do not give an integer first, the machine will break. Also do NOT list every song, a few will suffice."

    rating = hugbot.pretentious_score(biasPrompt, songs)

    return rating




    



@app.route('/get_songs')
def get_songs():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    songs = sp.current_user_top_tracks(limit=50)
    song_info = [(pl['name'], pl['artists'][0]['name'])
                for pl in songs['items']]
    songs_html = '<br>'.join([f'{name}:{artist}' for name, artist in song_info]) + "\n"
    ape = "LAKSHDLhfwHGA;EKLRHG;EUKRGHAEHIRUGHNEA;IUGHNE;IUSAGHN;IUESARBG;DEBGV;UNSGV;ESNGV;AESNGV;ANGV;IA"
    preten=get_preten(songs_html)
    radio = get_radio(songs_html)
    ringo = get_ringo(songs_html)
    batman = get_batman(songs_html)
    preten_num = preten.split('\n')[0]
    radio_num = radio.split('\n')[0]
    ringo_num = ringo.split('\n')[0]
    batman_num = batman.split('\n')[0]


    total_score = (int(preten_num) + int(radio_num)+int(ringo_num) + int(batman_num)) / 4
    
    return render_template('home.html', preten=preten, radio = radio, ringo = ringo, batman = batman, preten_num=preten_num, radio_num = radio_num, ringo_num = ringo_num, batman_num = batman_num, total_score = total_score )
    

    return songs_html  + '<br />' + get_songs1(songs_html)
                 
                 

    



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    
    
#class spotifyConnect():