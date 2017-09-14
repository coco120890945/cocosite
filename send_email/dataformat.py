import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pyh import *

month_userinfo_list=[[3L, 3L, 0L, 34L]]
new_userinfo_list=[[3001L, '13063797253', '', 13063797253L, '', 0, '2017-05-13 09:12:14'], [3002L, '18120045381', '', 18120045381L, '', 0, '2017-05-13 09:37:58'], [3003L, '13316826508', '', 13316826508L, '', 1, '2017-05-16 03:19:37'], [3007L, '17703858838', '', 17703858838L, '', 1, '2017-05-19 15:01:40'], [3008L, '13673669350', '', 13673669350L, '', 0, '2017-05-22 15:19:19'], [3009L, '13450236559', '', 13450236559L, '', 0, '2017-05-25 11:24:12'], [3010L, '18121373391', '\xe5\xa7\x9a\xe6\xb5\xb7\xe6\x9d\x83', 18121373391L, '18121373391', 1, '2017-05-31 11:26:37'], [3011L, '17319741507', '', 17319741507L, '', 1, '2017-06-01 20:39:29'], [3012L, '17319744507', 'google', 17319744507L, '', 1, '2017-06-01 21:08:02'], [3013L, '17703858938', '', 17703858938L, '', 0, '2017-06-02 10:55:06'], [3014L, '18670092225', '', 18670092225L, '', 1, '2017-06-06 10:11:13'], [3015L, '15897872044', '', 15897872044L, '', 0, '2017-07-05 17:21:48'], [3016L, '18301325781', '', 18301325781L, '', 0, '2017-07-09 10:14:19'], [3017L, '13833385699', '', 13833385699L, '', 1, '2017-07-18 15:19:10'], [3018L, '18859206763', '', 18859206763L, '', 0, '2017-07-27 08:46:07'], [3019L, '17328314497', '', 17328314497L, '', 0, '2017-07-27 12:00:20'], [3020L, '18680580314', '', 18680580314L, '', 1, '2017-07-27 14:23:47'], [3021L, '17328314475', '', 17328314475L, '', 0, '2017-07-27 14:49:05'], [3022L, '13435373613', '', 13435373613L, '', 0, '2017-07-27 15:26:48'], [3023L, '17328314238', '', 17328314238L, '', 0, '2017-07-27 15:54:20'], [3024L, '15617706735', '', 15617706735L, 'hhzzmk', 1, '2017-07-29 16:47:05'], [3025L, '18071711755', '\xe5\xae\x8b\xe5\xb0\x8f\xe6\x9e\x97', 18071711755L, '18071711755', 1, '2017-08-06 16:36:17'], [3026L, '13850363093', '', 13850363093L, '', 0, '2017-08-07 18:50:45'], [3027L, '18220121307', '', 18220121307L, '553382113', 1, '2017-08-13 21:54:27'], [3028L, '17612116268', '', 17612116268L, '', 0, '2017-08-15 17:15:25'], [3029L, '13890341951', '\xe5\x90\xb4\xe6\x98\x8e\xe6\x9e\x9d', 13890341951L, '13890341951', 1, '2017-08-15 23:04:36'], [3030L, '13336988963', '\xe5\x8f\xb6\xe5\x90\x9b\xe5\xb8\x85', 13336988963L, '68742114', 1, '2017-08-28 16:12:28'], [3031L, '18530085066', '\xe5\xa4\xa7\xe8\x8e\x90\xe8\x8e\x90', 18530085066L, '18530085166', 0, '2017-08-29 14:56:57'], [3032L, '18530089066', '', 18530089066L, '', 1, '2017-08-29 15:01:10'], [3033L, '18328079451', '', 18328079451L, '', 1, '2017-08-29 20:03:16'], [3034L, '18530085166', '', 18530085166L, '', 0, '2017-08-30 11:38:38'], [3035L, '18682027206', '', 18682027206L, '18682027206', 1, '2017-09-03 08:06:36'], [3036L, '18711087353', '', 18711087353L, '', 1, '2017-09-13 15:29:38'], [3037L, '18711087354', '', 18711087354L, '', 1, '2017-09-13 15:30:06']]










def to_html(month_userinfo_list,new_userinfo_list):
    page = PyH('new mail')
    page<<'<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
    page<<'<font  >&nbsp;&nbsp;&nbsp;&nbsp;HI:all</font>'
    page<<div(style="text-align:left")<<h4('&nbsp;&nbsp;&nbsp;&nbsp; congratulation   !!!! ')
    page<<div(style="text-align:left")<<h4('&nbsp;&nbsp;&nbsp;&nbsp; you have a new user sign in.')
    page<<'<font color="#a52a2a"  >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; is_proxy is flag :1 dailiren  0 toubaoren.</font>'
    page<<div(style="text-align:center")<<h4('The total information')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr3 = mytab << tr(bgcolor="lightgrey")
    tr3 << th('month_count') +th('dailiren_month_count')+th('toubaoren_month_count')+ th('total_count')
    for i in range(len(month_userinfo_list)):
        tr4 = mytab << tr()
        for j in range(4):
            tr4 << td(month_userinfo_list[i][j])

    page<<div(style="text-align:center")<<h4('new user info')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr1 = mytab << tr(bgcolor="lightgrey")
    tr1 << th('uid') + th('username')+th('real_name') +th('phone') + th('wechat') +th('is_proxy')+th('addtime')
    for i in range(len(new_userinfo_list)):
        tr2 = mytab << tr()
        for j in range(7):
            tr2 << td(new_userinfo_list[i][j])
            if new_userinfo_list[i][j]==' ':
                tr2.attributes['bgcolor']='yellow'
            if new_userinfo_list[i][j]=='':
                tr2[1].attributes['style']='color:red'
    return page.printOut('test.html')

a = to_html(month_userinfo_list,new_userinfo_list)

