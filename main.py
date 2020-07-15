try:
    from pytube import YouTube
    from pytube import Playlist
except :
    print('Required modules not found ')

def yt_single(u):
    
    yt = YouTube(u)

    r = 1
  
    for i in yt.streams.filter(file_extension='mp4'):
        l = str(i).split()
        if ('res' in l[3] and not('"None"' in l[3])) :
            print('\t'+str(l[3]) + '-' + str(r))
        r+=1

    opt = int(input('\n *Select the resolution by entering the number adjacent to it:'))
    path = input('\n Enter the foldr path for downloading:')
    s = (yt.streams.filter(file_extension='mp4'))[opt - 1]
    print('\n\t'+str(s) + ' is downloading')

    s.download(path)
    print('\n -------Downloaded--------')

def yt_multi():
    pass


if __name__ == "__main__":

    print('--------------------Py Youtube Downloader _ By InbaKrish..-------------------------')
    ty = int(input('\n 1. Youtube single video \n 2.Youtube playlist \n\t\tEnter your option:'))
    
    if ty == 1:
        
        ur = input('\n *Enter Video URL and it enter:')
        yt_single(ur)
    

    
