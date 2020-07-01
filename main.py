import json,docx,numpy
from statistics import mode,_counts
doc=docx.Document()
nof=int(input('Enter the number of your json files: '))
if nof==1:
    with open('StreamingHistory0.json') as a: datas=json.load(a)
elif nof==2:
    with open('StreamingHistory0.json') as a: fir=json.load(a)
    with open('StreamingHistory1.json') as b: sec=json.load(b)
    datas=fir+sec
elif nof==3:
    with open('StreamingHistory0.json') as a: fir=json.load(a)
    with open('StreamingHistory1.json') as b: sec=json.load(b)
    with open('StreamingHistory2.json') as c: thir=json.load(c)
    datas=fir+sec+thir
elif nof==4:
    with open('StreamingHistory0.json') as a: fir=json.load(a)
    with open('StreamingHistory1.json') as b: sec=json.load(b)
    with open('StreamingHistory2.json') as c: thir=json.load(c)
    with open('StreamingHistory3.json') as d: four=json.load(d)
    datas=fir+sec+thir+four
elif nof==5:
    with open('StreamingHistory0.json') as a: fir=json.load(a)
    with open('StreamingHistory1.json') as b: sec=json.load(b)
    with open('StreamingHistory2.json') as c: thir=json.load(c)
    with open('StreamingHistory3.json') as d: four=json.load(d)
    with open('StreamingHistory4.json') as e: five=json.load(e)
    datas=fir+sec+thir+four+five
elif nof==6:
    with open('StreamingHistory0.json') as a: fir=json.load(a)
    with open('StreamingHistory1.json') as b: sec=json.load(b)
    with open('StreamingHistory2.json') as c: thir=json.load(c)
    with open('StreamingHistory3.json') as d: four=json.load(d)
    with open('StreamingHistory4.json') as e: five=json.load(e)
    with open('StreamingHistory5.json') as f: six=json.load(f)
    datas=fir+sec+thir+four+five+six
save=input("Do you want to save your results in word file? yes or no: ")
if save in ['yes','Yes']: name=input("Enter the file name you want to save as: ")
top=int(input('Enter the number of songs you want on your top chart: '))
order=int(input('Enter the way you want to sort out your chart\n(1 for total streaming time of the song\n2 for number of times of streaming the song): '))

unsortedsongs,artists,sortedsongs,info,songs,singer,seppos,msplayed,sortsingersongs,sortedsongdict,songdict=[],[],[],[],[],[],[],[],[],[],{}
def returnmonth(a):
    monthdict={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    for i in monthdict.keys():
        if a==i: return monthdict.get(i)
def zipdict(list1,list2): return dict(list(zip(list1,list2)))
def returnlist(list,appenlist,attri):
    for item in list:
        if item[attri] not in appenlist: appenlist.append(item[attri])
returnlist(datas,unsortedsongs,'trackName')
returnlist(datas,artists,'artistName')

class SpotifyDataProcessing:
    def gettotalmineachsongs(self,unsortlist,data,mtdict):
        self.unsortlist,self.data,self.mtdict=unsortlist,data,mtdict
        for song in self.unsortlist:
            for data in self.data:
                if data['trackName']==song:
                    if song not in self.mtdict.keys(): self.mtdict.update({song:[data['msPlayed'],data['artistName']]})
                    elif song in self.mtdict.keys(): self.mtdict.update({song:[self.mtdict[song][0]+data['msPlayed'],data['artistName']]})
    def sortsongs(self,artist,dict,sortlist,list1,list2):
        self.artist,self.dict,self.sortlist,self.list1,self.list2=artist,dict,sortlist,list1,list2
        for artist in self.artist:
            for song in self.dict:
                if self.dict[song][1]==artist:
                    self.sortlist.append(song)
                    self.list1.append(self.dict[song])
        for i in range(len(self.list1)): self.list2.append(self.list1[i][0])
    def getpos(self,artist,list1,list2):
        self.artist,self.list1,self.list2=artist,list1,list2
        for artist in self.artist:
            for pos,val in enumerate(self.list1):
                if pos!=len(self.list1)-1:
                    if val[1]==artist and self.list1[pos+1][1]!=artist: self.list2.append(pos)
    def getsinger(self,list1,list2,list3):
        self.list1,self.list2,self.list3=list1,list2,list3
        for val in self.list2: self.list3.append(self.list1[val][1])
        self.list3.append(self.list1[-1][1])
    def dictify(self):
        global complete
        for ind,val in enumerate(seppos):
            if ind>0:
                songs.append(zipdict(sortedsongs[seppos[ind-1]+1:val+1],msplayed[seppos[ind-1]+1:val+1]))
                if ind==len(seppos)-1: songs.append(zipdict(sortedsongs[val+1:],msplayed[val+1:]))
            elif ind==0: songs.append(zipdict(sortedsongs[:val+1],msplayed[:val+1]))
        complete=zipdict(singer,songs)
    def sortcomplete(self):
        global complete,sortcom
        for singer in complete:
            sortedvals=sorted(complete[singer].values(),reverse=True)
            for val in sortedvals:
                for i in range(len(complete[singer])):
                    dictvalues=list(complete[singer].items())[i][1]
                    if val==dictvalues:
                        keys=list(complete[singer].items())[i][0]
                        sortsingersongs.append(keys)
            sortedsongdict.append(zipdict(sortsingersongs,sortedvals))
            sortsingersongs.clear()
        sortcom=zipdict(list(complete.keys()),sortedsongdict)
global complete,sortcom
sdp=SpotifyDataProcessing()
sdp.gettotalmineachsongs(unsortedsongs,datas,songdict)
sdp.sortsongs(artists,songdict,sortedsongs,info,msplayed)
sdp.getpos(artists,info,seppos)
sdp.getsinger(info,seppos,singer)
sdp.dictify()
sdp.sortcomplete()


values,valuespos,toppos,topval,topsong,topartist,sd,songduration,nooftimes,nopos=[],[],[],[],[],[],[],[],[],[]
class TopChart:
    def getvalandsval(self):
        global sortedvalues
        for artist in complete:
            for song in complete[artist]:
                val=complete[artist][song]
                values.append(val)
        sortedvalues=values.copy()
        sortedvalues.sort(reverse=True)
    def posofvalfromsval(self):
        global sortedvalues
        for i in range(top):
            for pos,val in enumerate(values):
                if sortedvalues[i]==val:
                    toppos.append(pos)
                    topval.append(val)
    def getinfo(self):
        for i in range(top):
            n=0
            for artist in complete:
                for song in complete[artist]:
                    n+=1
                    if n==toppos[i]+1:
                        topsong.append(song)
                        topartist.append(artist)
    def maxmode(self,list):
        self.list=list
        if _counts(list)==1: return mode(list)
        else:
            newlist=[]
            for i in range(len(_counts(list))): newlist.append(_counts(list)[i][0])
            return max(newlist)
    def getduration(self,song,data,ssd,songdur,topp):
        self.song,self.data,self.ssd,self.songdur,self.topp=song,data,ssd,songdur,topp
        for song in self.song:
            for data in self.data:
                if data['trackName']==song: self.ssd.append(data['msPlayed'])
            self.songdur.append(self.maxmode(self.ssd))
            del self.ssd[:]
        return self.songdur[:self.topp]
    def presentation(self,hours):
        self.hours=hours
        if not self.hours:
            if save in ['yes','Yes']:
                doc.add_paragraph("Your top "+str(top)+" most-streamed songs are:")
                for i in range(len(topsong)): nooftimes.append(topval[i]/self.getduration(topsong,datas,sd,songduration,top)[i])
                sortedtimes=nooftimes[:]
                sortedtimes.sort(reverse=True)
                for j in range(len(sortedtimes)):
                    for pos,val in enumerate(nooftimes):
                        if sortedtimes[j]==val:
                            nopos.append(pos)
                            break
                for i in range(len(sortedtimes)): doc.add_paragraph(str(i+1)+". "+topsong[nopos[i]]+" by "+topartist[nopos[i]]+" with "+str(int(sortedtimes[i]))+" times, or "+str(int(topval[nopos[i]]/(1000*60*60)))+" hours")
            else:
                print("Your top "+str(top)+" most-streamed songs are:")
                for i in range(len(topsong)): nooftimes.append(topval[i]/self.getduration(topsong,datas,sd,songduration,top)[i])
                sortedtimes=nooftimes[:]
                sortedtimes.sort(reverse=True)
                for j in range(len(sortedtimes)):
                    for pos,val in enumerate(nooftimes):
                        if sortedtimes[j]==val:
                            nopos.append(pos)
                            break
                for i in range(len(sortedtimes)): print(str(i+1)+". "+topsong[nopos[i]]+" by "+topartist[nopos[i]]+" with "+str(int(sortedtimes[i]))+" times, or "+str(round(topval[nopos[i]]/(1000*60*60),1))+" hours")
        if self.hours:
            if save in ['yes','Yes']:
                doc.add_paragraph("Your top "+str(top)+" most-streamed songs are:")
                for j in range(len(topsong)): doc.add_paragraph(str(j+1)+". "+topsong[j]+" by "+topartist[j]+" with "+str(int(topval[j]/self.getduration(topsong,datas,sd,songduration,top)[j]))+" times, or "+str(int(topval[j]/(1000*60*60)))+" hours")
            else:
                print("Your top "+str(top)+" most-streamed songs are:")
                for j in range(len(topsong)): print(str(j+1)+". "+topsong[j]+" by "+topartist[j]+" with "+str(int(topval[j]/self.getduration(topsong,datas,sd,songduration,top)[j]))+" times, or "+str(round(topval[j]/(1000*60*60),1))+" hours")
tc=TopChart()
tc.getvalandsval()
tc.posofvalfromsval()
tc.getinfo()
if order==1: tc.presentation(True)
elif order==2: tc.presentation(False)


artno=int(input('Enter the number of artists you want on your top artists: '))
topartval,artpos,topartists=[],[],[]
class TopArtist:
    def totaltime(self):
        global comartist,sorttopart
        for songdiction in songs: topartval.append(numpy.sum(list(songdiction.values())))
        comartist=zipdict(singer,topartval)
        sorttopart=topartval[:]
        sorttopart.sort(reverse=True)
        for i in range(len(sorttopart)):
            for pos, val in enumerate(topartval):
                if sorttopart[i]==val:
                    artpos.append(pos)
                    break
    def presentation(self):
        global sorttopart
        if save in ['yes','Yes']:
            doc.add_paragraph("Your top "+str(artno)+" artists are:")
            for i in range(len(sorttopart[:artno])):
                doc.add_paragraph(str(i+1)+". "+singer[artpos[i]]+" with "+str(int(sorttopart[i]/(1000*60*60)))+" hours")
                topartists.append(singer[artpos[i]])
        else:
            print("Your top "+str(artno)+" artists are:")
            for i in range(len(sorttopart[:artno])):
                print(str(i+1)+". "+singer[artpos[i]]+" with "+str(round(sorttopart[i]/(1000*60*60),1))+" hours")
                topartists.append(singer[artpos[i]])
ta=TopArtist()
ta.totaltime()
ta.presentation()


tsforeachta,asd,tsd,toptensong,toptensongval,sorttt,toptenpertime,sortttpt,noposttpt,realnoposttpt=[],[],[],[],[],[],[],[],[],[]
class TopSongFromTopArtist:
    def gettopsonglist(self):
        global sortcom
        for artist in topartists:
            for singer in sortcom:
                if artist==singer: tsforeachta.append(sortcom[singer])
    def getduration(self,song):
        self.song=song
        for data in datas:
            if data['trackName']==self.song: asd.append(data['msPlayed'])
        tsd.append(tc.maxmode(asd))
        del asd[:]
        return tsd[-1]
    def cleantopten(self):
        global rscom
        for i in range(len(topartists)):
            toptensong.append(list(tsforeachta[i].keys())[:10])
            toptensongval.append(list(tsforeachta[i].values())[:10])
        for i in range(len(toptensong)): sorttt.append(zipdict(toptensong[i],toptensongval[i]))
        rscom=zipdict(topartists,sorttt)
    def presentation(self):
        global rscom
        if order==2:
            if save in ['yes','Yes']:
                doc.add_paragraph("Your top 10 (at most) songs from your top "+str(artno)+" artists are: ")
                for i in range(len(toptensongval)): toptenpertime.append([toptensongval[i][j]/self.getduration(toptensong[i][j]) for j in range(len(toptensongval[i])) if self.getduration(toptensong[i][j])!=0])
                for i in range(len(toptenpertime)): sortttpt.append(sorted(toptenpertime[i],reverse=True))
                for i in range(len(sortttpt)):
                    for j,sval in enumerate(sortttpt[i]):
                        for pos,val in enumerate(toptenpertime[i]):
                            if sval==val:
                                noposttpt.append(pos)
                                break
                    kk=noposttpt[:]
                    realnoposttpt.append(kk)
                    del noposttpt[:]
                for i in range(len(sortttpt)):
                    doc.add_paragraph(str(i+1)+". "+topartists[i]+":")
                    for j in range(len(sortttpt[i])):
                        times=int(sortttpt[i][j])
                        if times>1: doc.add_paragraph(str(j+1)+". "+toptensong[i][realnoposttpt[i][j]]+" with "+str(times)+" times, or "+str(round(toptensongval[i][realnoposttpt[i][j]]/(1000*60*60),1))+" hours")
            else:
                print("Your top 10 (at most) songs from your top "+str(artno)+" artists are: ")
                for i in range(len(toptensongval)): toptenpertime.append([toptensongval[i][j]/self.getduration(toptensong[i][j]) for j in range(len(toptensongval[i])) if self.getduration(toptensong[i][j])!=0])
                for i in range(len(toptenpertime)): sortttpt.append(sorted(toptenpertime[i],reverse=True))
                for i in range(len(sortttpt)):
                    for j,sval in enumerate(sortttpt[i]):
                        for pos,val in enumerate(toptenpertime[i]):
                            if sval==val:
                                noposttpt.append(pos)
                                break
                    kk=noposttpt[:]
                    realnoposttpt.append(kk)
                    del noposttpt[:]
                for i in range(len(sortttpt)):
                    print(str(i+1)+". "+topartists[i]+":")
                    for j in range(len(sortttpt[i])):
                        times=int(sortttpt[i][j])
                        if times>1: print(str(j+1)+". "+toptensong[i][realnoposttpt[i][j]]+" with "+str(times)+" times, or "+str(round(toptensongval[i][realnoposttpt[i][j]]/(1000*60*60),1))+" hours")
        elif order==1:
            if save in ['yes','Yes']:
                doc.add_paragraph("Your top 10 (at most) songs from your top "+str(artno)+" artists are: ")
                for i,artist in enumerate(topartists):
                    doc.add_paragraph(str(i+1)+". "+topartists[i]+":")
                    for j in range(len(rscom[artist])):
                        songname,songvalue=list(rscom[artist].keys()),list(rscom[artist].values())
                        if self.getduration(songname[j])!=0:
                            times=int(list(rscom[artist].values())[j]/self.getduration(songname[j]))
                            if songvalue[j]!=0 and times>1: doc.add_paragraph(str(j+1)+". "+songname[j]+" with "+str(int(songvalue[j]/self.getduration(songname[j])))+" times, or "+str(round(songvalue[j]/(1000*60*60),1))+" hours")
            else:
                print("Your top 10 (at most) songs from your top "+str(artno)+" artists are: ")
                for i,artist in enumerate(topartists):
                    print(str(i+1)+". "+artist+":")
                    for j in range(len(rscom[artist])):
                        songname,songvalue=list(rscom[artist].keys()),list(rscom[artist].values())
                        if self.getduration(songname[j])!=0:
                            times=int(list(rscom[artist].values())[j]/self.getduration(songname[j]))
                            if songvalue[j]!=0 and times>1: print(str(j+1)+". "+songname[j]+" with "+str(times)+" times, or "+str(round(songvalue[j]/(1000*60*60),1))+" hours")

        # elif order==1:
        #     #doc.add_paragraph("Your top 10 (at most) songs from your top "+str(artno)+" artists are: ")
        #     print("Your top 10 (at most) songs from your top "+str(artno)+" artists are: ")
        #     for i in range(len(topartists)):
        #         #doc.add_paragraph(str(i+1)+". "+topartists[i]+":")
        #         print(str(i+1)+". "+topartists[i]+":")
        #         for ind,song in enumerate(tsforeachta[i]):
        #             if ind>=10: break
        #             else:
        #                 #doc.add_paragraph(str(ind+1)+". "+song+" with "+str(int(list(tsforeachta[i].values())[ind]/self.getduration(song)))+" times, or "+str(round(list(tsforeachta[i].values())[ind]/(1000*60*60),1))+" hours")
        #                 print(str(ind+1)+". "+song+" with "+str(int(list(tsforeachta[i].values())[ind]/self.getduration(song)))+" times, or "+str(round(list(tsforeachta[i].values())[ind]/(1000*60*60),1))+" hours")
tsfta=TopSongFromTopArtist()
tsfta.gettopsonglist()
tsfta.cleantopten()
tsfta.presentation()


wantmonth=str(input('Do you want to have a monthly chart? yes or no: '))
if wantmonth in ['yes','Yes']:
    month=input('Enter the specific month (1-12): ')
    year=input('Enter the year: ')
    mtop=int(input('Enter the number of songs shown on your monthly top chart: '))
    morder=int(input('Enter the way you want to sort out your chart\n(1 for total streaming time of the song\n2 for number of times of streaming the song): '))
    mdatas,unsortmsong,martists,sortmsong,minfo,mmsplayed,mseppos,msinger,msongs,mvalues,mvaluespos,mtoppos,mtopval,mtopsong,mtopartist,msd,msongduration,mnooftimes,mnopos,msongdict=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],{}
    class MonthlyChart:
        def __init__(self,month,yr):
            self.month,self.yr=month,yr
        def getmonthdata(self):
            for data in datas:
                if data['endTime'][:4]==self.yr:
                    if int(self.month)<10:
                        if data['endTime'][6]==self.month: mdatas.append(data)
                    elif int(self.month)>=10:
                        if data['endTime'][5:7]==self.month: mdatas.append(data)
        def sortdata(self):
            global mcomplete
            returnlist(mdatas,unsortmsong,'trackName')
            returnlist(mdatas,martists,'artistName')
            sdp.gettotalmineachsongs(unsortmsong,mdatas,msongdict)
            sdp.sortsongs(martists,msongdict,sortmsong,minfo,mmsplayed)
            sdp.getpos(martists,minfo,mseppos)
            sdp.getsinger(minfo,mseppos,msinger)
            for ind,val in enumerate(mseppos):
                if ind>0:
                    msongs.append(zipdict(sortmsong[mseppos[ind-1]+1:val+1],mmsplayed[mseppos[ind-1]+1:val+1]))
                    if ind==len(mseppos)-1: msongs.append(zipdict(sortmsong[val+1:],mmsplayed[val+1:]))
                elif ind==0: msongs.append(zipdict(sortmsong[:val+1],mmsplayed[:val+1]))
            mcomplete=zipdict(msinger,msongs)
        def getchart(self,hours):
            self.hours=hours
            #tc.getvalandsval()
            global msortedvalues
            for artist in mcomplete:
                for song in mcomplete[artist]:
                    val=mcomplete[artist][song]
                    mvalues.append(val)
            msortedvalues=mvalues.copy()
            msortedvalues.sort(reverse=True)
            #tc.posofvalfromsval()
            for i in range(mtop):
                for pos,val in enumerate(mvalues):
                    if msortedvalues[i]==val:
                        mtoppos.append(pos)
                        mtopval.append(val)
            #tc.getinfo()
            for i in range(mtop):
                n=0
                for artist in mcomplete:
                    for song in mcomplete[artist]:
                        n+=1
                        if n==mtoppos[i]+1:
                            mtopsong.append(song)
                            mtopartist.append(artist)
            #tc.presentation()
            if not self.hours:
                if save in ['yes','Yes']:
                    doc.add_paragraph("Your top "+str(mtop)+" most-streamed songs in "+returnmonth(int(month))+" "+self.yr+" are:")
                    for i in range(len(mtopsong)): mnooftimes.append(mtopval[i]/tc.getduration(mtopsong,mdatas,msd,msongduration,mtop)[i])
                    msortedtimes=mnooftimes[:]
                    msortedtimes.sort(reverse=True)
                    for j in range(len(msortedtimes)):
                        for pos,val in enumerate(mnooftimes):
                            if msortedtimes[j]==val:
                                mnopos.append(pos)
                                break
                    for i in range(len(msortedtimes)):
                        times=int(msortedtimes[i])
                        if times>1: doc.add_paragraph(str(i+1)+". "+mtopsong[mnopos[i]]+" by "+mtopartist[mnopos[i]]+" with "+str(times)+" times, or "+str(round(mtopval[mnopos[i]]/(1000*60*60),1))+" hours")
                else:
                    print("Your top "+str(mtop)+" most-streamed songs in "+returnmonth(int(month))+" "+self.yr+" are:")
                    for i in range(len(mtopsong)): mnooftimes.append(mtopval[i]/tc.getduration(mtopsong,mdatas,msd,msongduration,mtop)[i])
                    msortedtimes=mnooftimes[:]
                    msortedtimes.sort(reverse=True)
                    for j in range(len(msortedtimes)):
                        for pos,val in enumerate(mnooftimes):
                            if msortedtimes[j]==val:
                                mnopos.append(pos)
                                break
                    for i in range(len(msortedtimes)):
                        times=int(msortedtimes[i])
                        if times>1: print(str(i+1)+". "+mtopsong[mnopos[i]]+" by "+mtopartist[mnopos[i]]+" with "+str(times)+" times, or "+str(round(mtopval[mnopos[i]]/(1000*60*60),1))+" hours")
            if self.hours:
                if save in ['yes','Yes']:
                    doc.add_paragraph("Your top "+str(mtop)+" most-streamed songs in "+returnmonth(int(month))+" "+self.yr+" are:")
                    for j in range(len(mtopsong)):
                        if tc.getduration(mtopsong,mdatas,msd,msongduration,mtop)[j]!=0:
                            times=int(mtopval[j]/tc.getduration(mtopsong,mdatas,msd,msongduration,mtop)[j])
                            if times>1: doc.add_paragraph(str(j+1)+". "+mtopsong[j]+" by "+mtopartist[j]+" with "+str(times)+" times, or "+str(round(mtopval[j]/(1000*60*60),1))+" hours")
                else:
                    print("Your top "+str(mtop)+" most-streamed songs in "+returnmonth(int(month))+" "+self.yr+" are:")
                    for j in range(len(mtopsong)):
                        if tc.getduration(mtopsong,mdatas,msd,msongduration,mtop)[j]!=0:
                            times=int(mtopval[j]/tc.getduration(mtopsong,mdatas,msd,msongduration,mtop)[j])
                            if times>1: print(str(j+1)+". "+mtopsong[j]+" by "+mtopartist[j]+" with "+str(times)+" times, or "+str(round(mtopval[j]/(1000*60*60),1))+" hours")
    mc=MonthlyChart(month,year)
    mc.getmonthdata()
    mc.sortdata()
    if morder==1: mc.getchart(True)
    elif morder==2: mc.getchart(False)
if wantmonth not in ['yes','Yes']: print('Hope you enjoy!')
if save in ['yes','Yes']: doc.save(name+'.docx')
