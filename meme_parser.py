class MemeParser():
    def __new__(self, sr_children):
        return self.get_memes(self, sr_children)
        
    def get_memes(self, sr_children) -> list:
        memes = list()
        for child in sr_children:
            if "data" in child and "post_hint" in child["data"] and child["data"]["post_hint"] == "image":
                memes.append(child["data"]["url"])
        return memes