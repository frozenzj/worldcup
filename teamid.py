import re
from bs4 import BeautifulSoup as Bs
import requests
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=3057&teamId=27585&type=home
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=3057&teamId=31664&type=home		欧洲杯资格赛
#https://data.huanhuba.com/leagueData/getTeamTreeList?seasonId=3057			teamtree
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=12654&teamId=31664&type=home		国际友谊赛
tn32=[('俄罗斯','沙特阿拉伯','埃及','乌拉圭'),('葡萄牙','西班牙','摩洛哥','伊朗'),('法国','澳大利亚','秘鲁','丹麦'),('阿根廷','冰岛','克罗地亚','尼日利亚'),('巴西','瑞士','哥斯达黎加','塞尔维亚'),('德国','墨西哥','瑞典','韩国'),('比利时','巴拿马','突尼斯','英格兰'),('日本','波兰','哥伦比亚','塞内加尔')]
def invert_dict(d):
    return dict(zip(d.values(),d.keys()))
def teamid(area=0):
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
def allteamid(mode=1):
    at=[]
    i=0
    for i in range(6):
        at=at+teamid(i)
    tidall=dict(at)
    tnall=invert_dict(tidall)
    if mode==1:
        return tidall
    if mode==2:
        return tnall
