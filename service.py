from meme_parser import MemeParser
from r_queries import R_Queries
from json import loads


class Service():
    def __init__(self, sr=""):
        self.query = R_Queries("http://www.reddit.com/r/" + sr)

    def get_best_memes(self, limit=25):
        response = self.query.get_best(limit)
        try:
            memes = loads(response.content)
            children = memes["data"]["children"]
            return MemeParser(children)
        except:
            return None

    def get_hot_memes(self, limit=25):
        response = self.query.get_hot(limit)
        try:
            memes = loads(response.content)
            children = memes["data"]["children"]
            return MemeParser(children)
        except:
            return None

    def get_new_memes(self, limit=25):
        response = self.query.get_new(limit)
        try:
            memes = loads(response.content)
            children = memes["data"]["children"]
            return MemeParser(children)
        except:
            return None

    def get_random_meme(self):
        response = self.query.get_random()
        try:
            memes = loads(response.content)
            children = memes[0]["data"]["children"]
            meme_data = MemeParser(children)[0]
            return meme_data
        except:
            return None

    def get_search(self, prompt: str):
        try:
            search_result = loads(self.query.get_search(prompt).text)
            results = search_result["names"]
            return results
        except:
            return None
