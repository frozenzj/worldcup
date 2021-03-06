import re
from bs4 import BeautifulSoup as Bs
import requests
from itertools import chain
import pandas as pd
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=3057&teamId=27585&type=home
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=3057&teamId=31664&type=home		欧洲杯资格赛
#https://data.huanhuba.com/leagueData/getTeamTreeList?seasonId=3057			teamtree
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=12654&teamId=31664&type=home		国际友谊赛
#tbody[0-2#全、主、客#]('tr')[0-99#场次#]('td')[0-9#比赛类型、日期、主、比（全，上半场）、客、赛果、盘口、盘路、大小、分析#]

def invert_dict(d):#字典键-值翻转
    return dict(zip(d.values(),d.keys()))
def teamid(area=0):#获取各地区队名及相应网页编号
    if area==0:
        htmla='http://liansai.166cai.cn/league/176/5776/teams'  #北美nora  35
        teamnum=35
    elif area==1:
        htmla='http://liansai.166cai.cn/league/126/6223/teams'  #南美soua  10
        teamnum=10
    elif area==2:
        htmla='http://liansai.166cai.cn/league/265/6159/teams'  #大洋ocea  11
        teamnum=11
    elif area==3:
        htmla='http://liansai.166cai.cn/league/141/5749/teams'  #亚洲asia  45
        teamnum=45
    elif area==4:
        htmla='http://liansai.166cai.cn/league/175/6256/teams'  #欧洲eurp  54
        teamnum=54
    elif area==5:
        htmla='http://liansai.166cai.cn/league/157/6222/teams'  #非洲afri  53
        teamnum=53
    #http://liansai.166cai.cn/team/912/panlumatchs?nums=100
    rule=r"(<a href=\"http://liansai.166cai.cn/team/)([0-9]{0,5})(\" target=\"_blank\">)([\u4e00-\u9fa5]*)(.*)"
    h_get=requests.get(htmla)
    h_soup=Bs(h_get.content,'lxml')
    h_soup_l=h_soup.find_all('a')[-teamnum*2-1::2]
    #for i in range(len(Tnora.find_all('a')[-71::2])):
    #    Tnora_pre.append(i)
    #str_test=re.match(r"(<a href=\"http://liansai.166cai.cn/team/)([0-9]{0,5})(\" target=\"_blank\">)([\u4e00-\u9fa5]*)(.*)",str(k[1]))
    #str_test.group(2,4)
    h_s=[]
    i=0
    for i in range(1,len(h_soup_l)):
        str_test=re.match(rule,str(h_soup_l[i]))
        h_s.append(str_test.group(2,4))
    if area==4:
        h_s.append(('414','俄罗斯'))
#    h_d=dict(h_s)
#    h_d_v=invert_dict(h_d)
    return h_s
def allteamid(mode=1):#获取所有队伍名称及id，返回列表
    at,at1=[],[]
    tn32=[('俄罗斯','沙特阿拉伯','埃及','乌拉圭'),('葡萄牙','西班牙','摩洛哥','伊朗'),('法国','澳大利亚','秘鲁','丹麦'),('阿根廷','冰岛','克罗地亚','尼日利亚'),('巴西','瑞士','哥斯达黎加','塞尔维亚'),('德国','墨西哥','瑞典','韩国'),('比利时','巴拿马','突尼斯','英格兰'),('日本','波兰','哥伦比亚','塞内加尔')]
    i=0
    for i in range(6):
        at=at+teamid(i)
    tidall=dict(at)
    tnall=invert_dict(tidall)
    if mode==0:
        for i in range(len(at)):
            at1.append(at[i][0])
        return at1
    if mode==1:
        return tidall
    if mode==2:
        return tnall
    if mode==32:
        tid=[]
        i=0
        j=0
        for i in range(len(tn32)):
            tid.append([])
            for j in range(len(tn32[i])):
                tid[i].append(tnall[tn32[i][j]])
        return tid
def teamh(ids):#根据队伍id返回BS内容
    r=requests.get('http://liansai.166cai.cn/team/%s/panlumatchs?nums=100'%(ids))
    rs=Bs(r.content,'lxml')
    return rs
def rtest(r_s,mode,zkc=1,lw=0,n=0):#根据BS内容，返回各栏位内容
#    r=requests.get('http://liansai.166cai.cn/team/912/panlumatchs?nums=100')
#    r_s=Bs(r.content,'lxml')
    if mode==1:
        k=str(r_s('tbody')[zkc]('tr')[lw]('td')[n])
        return k
    else:
        j=len(r_s('tbody')[0]('tr'))
        return j
#group mode
#detail_r0=r"((\D+\d+)+\D{2})(?P<n>[\u4e00-\u9fa5]{1,})(\D+)"
##k=re.match(detail_r1,str(r_soup('tbody')[1]('tr')[0]('td')[0]('a')))
#detail_r1=r"(\D*)(?P<n>\d+-\d+-\d+)(.*)"
##k2=re.match(r2,str(r_soup('tbody')[1]('tr')[0]('td')[1]))
#detail_r2=r"((\D+\d+)+)([^\u4e00-\u9fa5]+)(?P<n>[\u4e00-\u9fa5]+)(\D+)"
#detail_r3=r"(\D+)(\d+)(\D+)(\d+)(\D+)(\d+-\d+)(\D+)"
#detail_r4=r"([^\u4e00-\u9fa5]+)(?P<n>[\u4e00-\u9fa5]+)(.*)"
#detail_r5=r"([^\u4e00-\u9fa5]+)(?P<n>[\u4e00-\u9fa5]+)(.*)"
#detail_r6=r"([^\*]+)(\*?)([^\u4e00-\u9fa5]+)([\u4e00-\u9fa5]+/?[\u4e00-\u9fa5]*)(.*)"
#detail_r7=r"(\D+)((\d*.?\d*)?)(\D+)([\u4e00-\u9fa5]+)(\D+)"
#detail_r8=r"(\D{4})(?P<n>[\u4e00-\u9fa5]+)(\D+)"
#findall mode
def rop():#各栏位正则表达
    r0=r"[\u4e00-\u9fa5]{1,}"
    #k=re.match(detail_r1,str(r_soup('tbody')[1]('tr')[0]('td')[0]('a')))
    r1=r"\d+-\d+-\d+"
    #k2=re.match(r2,str(r_soup('tbody')[1]('tr')[0]('td')[1]))
    r2=r"[\u4e00-\u9fa5]+"
    r3=r"(\d+):?\D+:?\D*:?(\d+)\D+(\d+-\d+)"
    r4=r"[\u4e00-\u9fa5]+"
    r5=r"[\u4e00-\u9fa5]+"
    r6=r"[^\*]+(\*?)[^\u4e00-\u9fa5]+([\u4e00-\u9fa5]+/?[\u4e00-\u9fa5]+)"
    r7=r"\D+(\d*.?\d*)\D+([\u4e00-\u9fa5]+)\D+"
    r8=r"[\u4e00-\u9fa5]+"
    rules=[]
    for i in range(9):
        rules.append(eval("r"+str(i)))
    return rules
def teamdict():#根据栏位内容返回列表
    i,j,k=0,0,0
    tl={}
    rules=rop()
    tid=allteamid(32)
    ids=list(chain(*tid))
    for i in range(len(ids)):
        tl[i]={}
        rs=''
        rs=teamh(ids[i])
        for j in range(rtest(rs,0)):
            tl[i][j]={}
            for k in range(9):
                tl[i][j][k]=re.findall(rules[k],rtest(rs,1,0,j,k))
    return tl
def teamlist(idmode=32):
    i,j=0,0
    tl=[]
#    rules=rop()
    if idmode==32:
        tid=allteamid(idmode)
        ids=list(chain(*tid))
    else:
        ids=allteamid(idmode)
    for i in range(len(ids)):
        rs=''
        rs=teamh(ids[i])
        for j in range(1,rtest(rs,0)):
#            for k in range(9):
            templ=[]
            tempx=[]
#                tl.append(re.findall(rules[k],rtest(rs,1,0,j,k))[0])
#            for k in rs('tr')[j].stripped_strings:
#                templ.append(k)
            templ=list(rs('tr')[j].stripped_strings)
            if len(templ)==11:
                tempx=''.join((templ[3],templ[4])).split()
                templ[3]=tempx[0]
                templ[4]=tempx[1]
            elif len(templ)==12:
                if templ[7]=='*':
                    tempx=''.join((templ[3],templ[4])).split()
                    templ[3]=tempx[0]
                    templ[4]=tempx[1]
                    templ[8]=''.join(templ[7:9])
                    templ.pop(7)
                else:
                    templ[3]=''.join(templ[3:5])
                    templ.pop(4)
            elif len(templ)==13:
                if templ[8]=='*':
                    templ[3]=''.join(templ[3:5])
                    templ.pop(4)
                    templ[8]=''.join(templ[7:9])
                    templ.pop(7)
                else:
                    templ[3]=''.join(templ[3:6])
                    templ.pop(4)
                    templ.pop(4)
            else:
                templ[3]=''.join(templ[3:6])
                templ.pop(4)
                templ.pop(4)
                templ[8]=''.join(templ[7:9])
                templ.pop(7)
#            templ[3]=''.join((templ[3],templ[4]))
#            tempx=templ[3].split()
#            templ[3]=tempx[0]
#            templ[4]=tempx[1]
            tl.append(templ[0:-1])
    k=list(rs('tr')[0].stripped_strings)
    k.insert(4,'上半场比分')
    k1=k[0:-1]
#    tl.insert(0,k[0:-1])
#    np.resize(tl,(-1,9))
    return k1,tl
#=======================================#

def rankbsc():
    rank_h=r'https://www.km28.com/data/fifarank.html'
    r=requests.get(rank_h)
    rs=Bs(r.content,'lxml')
    return rs
#def rankrules():
#    ruletitle=r'[^\u4e00-\u9fa5]*([\u4e00-\u9fa5]*).*'
def rankdict():
    rankbs=rankbsc()
    titlel=[]
    contentnum=len(rankbs('tr'))
    i=0
    for i in rankbs('tr')[0].stripped_strings:
        titlel.append(i)
    titlel[1]='区域'
    titlel=titlel[0:-1]
    contentl=[]
    i=0
    j=0
    for i in range(1,contentnum):
        contentl.append([])
        for j in rankbs('tr')[i].stripped_strings:
            contentl[i-1].append(j)
        contentl[i-1].insert(1,rankbs('tr')[i].attrs['data-type'])
    #contentl.insert(0,titlel)
    return titlel,contentl
#output original matchdf,rankdf
def testopdf():
    matcht,matchc=teamlist()
    rankt,rankc=rankdict()
    matchdf=pd.DataFrame(matchc,columns=matcht)
    rankdf=pd.DataFrame(rankc,columns=rankt)
    return matchdf,rankdf
def merge_mnr(m,r):
    r2c=r.loc[:,['球队','排名']]#提取两列数据
    r2c=r2c.rename(columns={'球队':'主队'})#改列标题
    #建立vlookup字典
    test1={}
    for i in range(len(r2c)):
        test1[r2c.iloc[i]['主队']]=r2c.iloc[i]['排名']
    m['Hrank']=m.主队.map(test1)
    m['Crank']=m.客队.map(test1)
    if any(m['Hrank'].isna()):
        m['Hrank']=m['Hrank'].fillna(0)
        m['Hrank']=m['Hrank'].astype('int')
    if any(m['Crank'].isna()):
        m['Crank']=m['Crank'].fillna(0)
        m['Crank']=m['Crank'].astype('int')
    match=m
    return match
def dfscore(mdf):
    dfsplit=pd.DataFrame((x.split(':') for x in mdf.比分),index=mdf.index,columns=['Hs','Cs'])
    mdf=pd.merge(mdf,dfsplit,right_index=True,left_index=True)
    for i in range(len(mdf)):
        if mdf.iloc[i]['Hs']>mdf.iloc[i]['Cs']:
            mdf.loc[i,'赛果']='win'
        elif mdf.iloc[i]['Hs']==mdf.iloc[i]['Cs']:
            mdf.loc[i,'赛果']='draw'
        else:
            mdf.loc[i,'赛果']='lose'
    matchdf=mdf
    return matchdf
def shortm(match,rank):
    m_df=merge_mnr(match,rank)
    m_df=dfscore(m_df)
    m_df['dist']=m_df['Hrank']-m_df['Crank']
    dfm=m_df.loc[:,['主队','Hs','客队','Cs','赛果','dist']]
    return dfm
def anaylsis(df,distance=49):
    dff=df[df['dist'].abs()>=distance]
    dict1={'w':0,'d':0,'l':0}
    for i in range(len(dff)):
        disct=dff.iloc[i]['dist']
        wtl=dff.iloc[i]['赛果']
        if disct<0:
            if wtl=='win':
                dict1['w']+=1
            elif wtl=='draw':
                dict1['d']+=1
            else:
                dict1['l']+=1
        else:
            if wtl=='win':
                dict1['l']+=1
            elif wtl=='draw':
                dict1['d']+=1
            else:
                dict1['w']+=1
    w=dict1['w']
    d=dict1['d']
    l=dict1['l']
    tot=w+d+l
#    print('total:'+str(tot)+'\n'+'winpercentage:'+str(l/tot))
    list1=[distance,tot,round(w/tot,5)]
    return list1
