class Song:
    all=[]

    def __init__(self,name):
        self.name=name
        Song.all.append(self)
    
    @classmethod
    def add_song_to_all(cls,song):
        cls.all.append(song)

    @classmethod
    def show_song_names(cls):
        print([song.name for song in cls.all])   

kovu=Song('kovu')
tamaa=Song('tamaa')

Song.show_song_names()