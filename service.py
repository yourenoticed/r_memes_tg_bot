from meme_parser import MemeParser
from r_queries import R_Queries
from json import loads
from time import sleep

class Service():
    def __init__(self, sr: str):
        self.query = R_Queries("http://www.reddit.com/r/" + sr)
        
    def get_hot_memes(self, limit=25):
        response = self.query.get_hot(limit)
        memes = loads(response.text)
        children = memes["data"]["children"]
        return MemeParser(children)
    
    def get_new_memes(self, limit=25):
        response = self.query.get_new(limit)
        memes = loads(response.text)
        children = memes["data"]["children"]
        return MemeParser(children)
    
    def get_random_meme(self):
        response = self.query.get_random()
        memes = loads(response.text)
        while len(memes) <= 0:
            response = self.query.get_random()
            sleep(1)
            memes = loads(response.text)
        children = memes[0]["data"]["children"]
        meme_data = MemeParser(children)[0]
        return meme_data