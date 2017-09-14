import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyh import *

list1=[[1,'Lucy']]
list=[[3036L, '18711087353', '', 18711087353L, '', '2017-09-13 15:29:38'], [3037L, '18711087354', '', 18711087354L, '', '2017-09-13 15:30:06']]
def to_html(list,list1):
    page = PyH('new mail')
    page<<div(style="text-align:left")<<h4('HI:all \n congratulation   !!!! \n you have a new user sign in.')
    page<<div(style="text-align:center")<<h4('The total information')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr3 = mytab << tr(bgcolor="lightgrey")
    tr3 << th('month_count') + th('total_count')
    for i in range(len(list1)):
        tr4 = mytab << tr()
        for j in range(2):
            tr4 << td(list1[i][j])

    page<<div(style="text-align:center")<<h4('new user info')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr1 = mytab << tr(bgcolor="lightgrey")
    tr1 << th('uid') + th('username')+th('real_name') +th('phone') + th('wechat') +th('addtime')
    for i in range(len(list)):
        tr2 = mytab << tr()
        for j in range(6):
            tr2 << td(list[i][j])
            if list[i][j]==' ':
                tr2.attributes['bgcolor']='yellow'
            if list[i][j]=='':
                tr2[1].attributes['style']='color:red'
    return page.printOut()

a = to_html(list,list1)
print a
print type(a)