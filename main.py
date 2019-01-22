#Defining the variables
Artist = "Sinach"
Song_Title = "I know who I am"
Album_tile = "I am Blessed"
Genre = "Gospel"
Duration_in_minutes = 1.52
Year_Released = 2000

def get_artist():
    return Artist

def get_song_title():
    return Song_Title

def get_song_duration():
    return Duration_in_minutes

def is_latest_release():
    if Year_Released < 2018:
        return False
    else:
        return True

    
#outputing the values of the variables
print(Artist)
print(Song_Title)
print(Album_tile)
print(Genre)
print(Duration_in_minutes)
print(Year_Released)

#separating line
print("==================")

#using the get_song_title function
print("My favorite song is",get_song_title())

#using the get_artist fucntion
print("It was sang by",get_artist())

#using the is_latest_release function
print("Latest Release?",is_latest_release())



