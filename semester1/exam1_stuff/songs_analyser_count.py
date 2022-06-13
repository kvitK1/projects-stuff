def read_file(path: str) -> list:
    """
    Reads csv file and returns data as list of tuples
    >>> read_file("songs.csv")[:3]
    [('http://www.billboard.com/charts/hot-100/1958-08-02', '8/2/1958', \
    '1', 'Poor Little Fool', 'Ricky Nelson', 'Poor Little FoolRicky Nelson', '1', '', '1', '1'), \
    ('http://www.billboard.com/charts/hot-100/1995-12-02', '12/2/1995', \
    '1', 'One Sweet Day', 'Mariah Carey & Boyz II Men', \
    'One Sweet DayMariah Carey & Boyz II Men', '1', '', '1', '1'), \
    ('http://www.billboard.com/charts/hot-100/1997-10-11', '10/11/1997', \
    '1', 'Candle In The Wind 1997/Something About The Way You Look Tonight', \
    'Elton John', 'Candle In The Wind 1997/Something About The Way You Look TonightElton John', \
    '1', '', '1', '1')]
    """
    with open(path, 'r', errors='ignore') as file:
        data = [(line[:-1].split(',')) for line in file if not (line.startswith('url') or len(line) == 0)]
        return data


def count_songs(song_list: list) -> dict:
    """
    Counts number of times each song appeared in charts
    Stores data in dict where key is a tuple of (song name, artist name)
    and key os number of occurances
    >>> list(count_songs(read_file("songs.csv")).items())[:3]
    [(('Poor Little Fool', 'Ricky Nelson'), 4), \
    (('One Sweet Day', 'Mariah Carey & Boyz II Men'), 17), \
    (('Candle In The Wind 1997/Something About The Way You Look Tonight', 'Elton John'), 32)]
    """
    songs = []
    for song in song_list:
        songs.append((song[3], song[4]))
    song_set = set(songs)
    dictionary = {}
    for song in song_set:
        times = songs.count(song)
        dictionary[song] = times
    return dictionary


def count_bigger_than_60(song_dict: dict) -> list:
    """
    Takes input from count_songs and selects only that songs which
    were seen in charts more than 60 times
    Returns list of tuples: (song name, artist name, number of occurrences)
    >>> count_bigger_than_60(count_songs(read_file("songs.csv")))[:3]
    [('Party Rock Anthem', 'LMFAO Featuring Lauren Bennett & GoonRock', 68), \
    ('Rolling In The Deep', 'Adele', 65), ('Sail', 'AWOLNATION', 70)]
    """
    data = []
    song_dict = count_songs(read_file('/Users/kvitoslava/vscode_intro/my_stuff/iiispyyt/songs.csv'))
    for song in song_dict.keys():
        if song_dict[song] > 60:
            data.append((song[0], song[1], song_dict[song]))
    return data

# count_bigger_than_60(read_file('/Users/kvitoslava/vscode_intro/my_stuff/iiispyyt/songs.csv'))

def write_file(song_list: list, file_name: str) -> None:
    """
    Writes data to file, nte nate of file is given as second argument
    Takes input from filtering function and writes data as follows (next lines must be in the file):
    Counting Stars,OneRepublic,68
    Party Rock Anthem,LMFAO Featuring Lauren Bennett & GoonRock,68
    Rolling In The Deep,Adele,65
    .....
    """
    # song_list = count_bigger_than_60(read_file('/Users/kvitoslava/vscode_intro/my_stuff/iiispyyt/songs.csv'))
    new_list = []
    for element in song_list:
        el = ",".join([str(i) for i in element])
        new_list.append(el)
    with open(file_name, "w") as file:
        for line in new_list:
            file.write(line+'\n')

def main():
    """
    Main function
    """
    pass
    print(read_file('/Users/kvitoslava/vscode_intro/my_stuff/iiispyyt/songs.csv'))
    count_songs(read_file('/Users/kvitoslava/vscode_intro/my_stuff/iiispyyt/songs.csv'))
    print(count_bigger_than_60(read_file('/Users/kvitoslava/vscode_intro/my_stuff/iiispyyt/songs.csv')))
    write_file(count_bigger_than_60(read_file('/Users/kvitoslava/vscode_intro/my_stuff/iiispyyt/songs.csv')), "song.txt")
