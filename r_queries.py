from requests import Response, get

class R_Queries():
    def __init__(self, link: str):
        self.link = link
        
    # limit is 25 by default up to 100
    def get_after(self, meme_name: str, limit=25) -> Response:
        return get(self.link + "/new.json?after=" + meme_name + "&?" + str(limit))
    
    def get_before(self, meme_name: str, limit=25) -> Response:
        return get(self.link + "/new.json?before=" + meme_name + "&?" + str(limit))
    
    def get_new(self, limit=25) -> Response:
        return get(self.link + "/new.json?limit=" + str(limit))
    
    def get_hot(self, limit=25) -> Response:
        return get(self.link + "/hot.json?limit=" + str(limit))
    
    def get_random(self) -> Response:
        return get(self.link + "/random.json")