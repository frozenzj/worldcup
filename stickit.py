#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=3057&teamId=27585&type=home
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=3057&teamId=31664&type=home		欧洲杯资格赛
#https://data.huanhuba.com/leagueData/getTeamTreeList?seasonId=3057			teamtree
#https://data.huanhuba.com/leagueData/getSingleMatch?seasonId=12654&teamId=31664&type=home		国际友谊赛
#http://liansai.166cai.cn/league/176/5776/teams	北美nora
#http://liansai.166cai.cn/league/126/6223/teams	南美soua
#http://liansai.166cai.cn/league/265/6159/teams	大洋ocea
#http://liansai.166cai.cn/league/141/5749/teams	亚洲asia
#http://liansai.166cai.cn/league/175/6256/teams	欧洲eurp
#http://liansai.166cai.cn/league/157/6222/teams	非洲afri
import re
from bs import BeautifulSoup as Bs
import requests
nora=requests.get('http://liansai.166cai.cn/league/176/5776/teams')
Tnora=Bs(nora.content,'lxml')
Tnora_pre=[]
k=Tnora.find_all('a')[-71::2]
for i in range(len(Tnora.find_all('a')[-71::2])):
    Tnora_pre.append(i)
strs=re.match(r"(<a href=\"http://liansai.166cai.cn/team/)([0-9]{0,5})(\" target=\"_blank\">)([\u4e00-\u9fa5]*)(.*)",str(k[1]))
strs.group(2,4)
