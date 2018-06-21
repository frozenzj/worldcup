#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=3057&teamId=27585&type=home
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=3057&teamId=31664&type=home		欧洲杯资格赛
#https://data.huanhuba.com/leagueData/getTeamTreeList?seasonId=3057			teamtree
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=12654&teamId=31664&type=home		国际友谊赛
nora_h='http://liansai.166cai.cn/league/176/5776/teams'  #北美nora  35
soua_h='http://liansai.166cai.cn/league/126/6223/teams'  #南美soua  10
ocea_h='http://liansai.166cai.cn/league/265/6159/teams'  #大洋ocea  11
asia_h='http://liansai.166cai.cn/league/141/5749/teams'  #亚洲asia  45
eurp_h='http://liansai.166cai.cn/league/175/6256/teams'  #欧洲eurp  54
afri_h='http://liansai.166cai.cn/league/157/6222/teams'  #非洲afri  53
import re
from bs4 import BeautifulSoup as Bs
import requests

nora=requests.get('http://liansai.166cai.cn/league/176/5776/teams')
Tnora=Bs(nora.content,'lxml')
Tnora_pre=[]
k=Tnora.find_all('a')[-71::2]
for i in range(len(Tnora.find_all('a')[-71::2])):
    Tnora_pre.append(i)
str_test=re.match(r"(<a href=\"http://liansai.166cai.cn/team/)([0-9]{0,5})(\" target=\"_blank\">)([\u4e00-\u9fa5]*)(.*)",str(k[1]))
str_test.group(2,4)
nora_s=[]
rule=r"(<a href=\"http://liansai.166cai.cn/team/)([0-9]{0,5})(\" target=\"_blank\">)([\u4e00-\u9fa5]*)(.*)"
i=0
for i in range(1,len(k)):
    str_test=re.match(rule,str(k[i]))
    nora_s.append(str_test.group(2,4))
nora_s[6]
nora_d=dict(nora_s)

soua_get=requests.get(soua_h)
soua_soup=Bs(soua_get.content,'lxml')
soua_soup_pre=[]
soua_soup_l=soua_soup.find_all('a')
soua_soup_l[-21::2]
