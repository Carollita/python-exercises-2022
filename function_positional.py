# Only Positional

def add_anime(name, year, episodes, /, source, studio, ranked):
    print(name, year, episodes, source, studio, ranked)

add_anime('Death Parade', 2015, 12, source='Original', studio='Madhouse', ranked=377) # valid

# add_anime(name='Death Parade', year=2015, episodes=12, source='original', studio='Madhouse', ranked=377) invalid

# Keyword only

def add_anime(*, name, year, episodes, source, studio, ranked):
    print(name, year, episodes, source, studio, ranked)

add_anime(name='Zankyou no terror', year=2014, episodes=11, source='Original', studio='MAPPA', ranked=456)

# Keyword and positional only

def add_anime(name, year, episodes, /, *, source, studio, ranked):
    print(name, year, episodes, source, studio, ranked)

add_anime('Monster', 2004, 74, source='Manga', studio='Madhouse', ranked=25)