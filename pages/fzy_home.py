'''我的主业'''
import streamlit as st
from PIL import Image
page =st.sidebar.radio(
    '我的主页',
    [
        '我的兴趣推荐内容',
        '我的图像处理工具',
        '我的智慧词典',
        '我的留言区',
        '亚文化圈子介绍与推荐',
    ]
)
def page1():
    '''我的兴趣推荐'''
    st.subheader('我的动漫推荐')
    tab1,tab2 = st.tabs(['天气之子','少女与战车'])
    with tab1:
        st.write('《天气之子》是由新海诚执导、Comix Wave Films负责制作的原创动画电影，同时也是继你的名字后第二次和RADWIMPS合作制作的作品。具体内容不在此累述，新海诚的动漫电影看就对了！')
        st.image('新海诚_天气の子.png')
        st.write('处了这个，新海诚的其他电影，例如《秒速5厘米》和《你的名字》也非常值得我们看')
        a,b = st.columns([1,1])
        with a:
            st.image('秒速5厘米.png')
        with b:
            st.image('君の名は.png')
    with tab2:
        st.write('''《少女与战车》拥有过硬的战车真实细节和不错的战斗画面，画风和剧情也相对轻松而不同于多数战争番的压迫，
                 重编的各国音乐也不错，推荐看看，目前有OVA12集和剧场以及最终章4集(目前速度大概是一年半才一更)''')
        a,b = st.columns([1,1])
        with a:
            st.image('少战_1.png')
        with b:
            st.image('少战_2.png')
    st.write('------------------------------')
    st.subheader('我的游戏推荐')
    tab1,tab2= st.tabs(['Terraria简介','一些梗'])
    with tab1:
        st.write('''Terraria是一款老游戏了，可以说是2D沙盒游戏里的巅峰，他的开发者工作室氛围和网络活动 也非常活跃和不一样，和其他大部分工作室比更有一种都是家人的感觉
                 。同时Re-Logic的成员人数也较少，但他们一人能做出这么好的作品也是十分惊人的，具体了解Terraria的一些历史及Redigit(游戏策划与Re-Logic创立者)的故事可以去自行寻找，不在此累述
                 ，游戏里的一些名梗(meme[模因])也是很有趣的，放在Tap2了''')    
        st.image("Terraria.png")
        st.write('作为一款在Minecraft之后的2D沙盒游戏，有些人可能就会把它当做2D版的Minecraft，但是事实上这种观点是错误的，两个游戏之内容间可以说是天差地别')
        video_file = open('Terraria建筑.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.write('我希望这段TR的建筑视频可以改变大家对于TR笼统的认知，视频来自B站up @外星小林 。同样我也再推荐一个TR的建筑大佬 @Orange缺,他在TR里还原了紫禁城和清明上河图等等')
    with tab2:
        st.image("迪士尼初版米老鼠.jpg")
        st.write('在过去的版本中Redigit一直想在游戏中添加米老鼠宠物来致敬或恶搞，但迫于西半球最强法务部的威没能实现，在这张meme图中可以看出他们早有预谋在新的版本加入黑白米老鼠了(笑')
        st.image("监狱强于一切.jpg")
        st.write('游戏中NPC入住的最低条件被玩家们研究透后便开始制作这样的监狱，并用经常用于建筑大佬的评论区低下并配上“this is the best!”来开玩笑或调侃')
        st.image("最后一次更新.jpg")
        st.write('''“看来我们已经到达了旅途的终点了，这将是我们最后一次更新”这是TR最经典的名梗之一，因为历史原因Red一度不想继续更新Tr而是另做打算
                 ，但由于cenx(Red的妻子)和玩家们的一度催促和坚持，Red还是在继续更新游戏，但是Red仍在每次更新时加上这一句，于是这也成为了一个梗，国内常说是“旅途的[中]点”因为旅途从未结束，
                 但由于优质的mod和tmod启动器的存在，这次1.4.5更新也许真的是旅途的终点了''')
    st.write('------------------------------')
    st.subheader('我的音乐推荐')
    go = st.selectbox('仍在持续更新......', ['RE Aoharu', '团结人民之歌'])
    if go == 'RE Aoharu':
        st.image("BA.png")
        st.write('Tip:这几首歌原声音量可能较大，建议提前调小系统音量')
        with open('RE Aoharu.wav','rb') as f:
             mymp3 = f.read()
        st.audio(mymp3,format = "audio/wav",start_time = 0)
        st.write('‘RE Aoharu’是游戏“Blue Archive”的原声带及主题旋律之一，拥有多个变种的音乐，如Aoharu和ARONA，这段旋律仅仅用几个简单的音符就构建了“开阔性”，可以很好用于开头想想未来或放在结尾来回放过去，同时他的电子音色较为清新可以很好的对标游戏的主题')
    elif go == '团结人民之歌':
        tab1,tab2= st.tabs(['团结人民之歌','团结人民之歌(小提琴版'])
        with tab1:
            st.image("智利_圣地亚哥.png")
            st.write('Tip:听tab2的小提琴独奏能更好地分辨旋律')
            with open('团结人民之歌[纪念阿连德逝世50周年].wav','rb') as f:
                 mymp3 = f.read()
            st.audio(mymp3,format = "audio/wav",start_time = 0)
            st.write('这是一首50~60年前来自智利的歌，后被用来纪念萨尔瓦多·吉列尔莫·阿连德·戈森斯总统，整体旋律昂扬向上，又十分贴合因此被用于此，要想要更具体的了解阿连德可以去看电影《圣地亚哥在下雨》或者查看网络上的百科与网友介绍')
        with tab2:
            st.image("阿连德.png")
            with open('团结人民之歌.wav','rb') as f:
                 mymp3 = f.read()
            st.audio(mymp3,format = "audio/wav",start_time = 0)
            st.write('作为一首红歌，合唱才能完全体现出其中的震撼和感染力，因此其并太不适合与独奏，但是独奏能帮助我们更好地了解和掌握旋律')
    st.write('------------------------------ ')
    st.write('''我喜欢的想推荐的歌(以及乐队)还有很多，但是由于时间和篇幅问题只有这些，不定期增加中.......
            先提前推荐些我喜欢的乐队：MIli，AJR[仅仅是还在活跃的已解散的不在此累述]当然，很多独立的音乐人、Vtube的和游戏OST也很棒''')    
    st.write('------------------------------')
    st.subheader('我的书籍推荐')
    st.write('暂未制作完成，敬请期待')
    st.write('------------------------------')
    
def page2():
    '''我的图像处理工具'''
    st.write(":sunglasses:图像处理小程序:sunglasses:")
    uploader_file = st.file_uploader("上传图片",type=["png",'jpeg','jpg'])
    if uploader_file:
        file_name = uploader_file.name
        file_type = uploader_file.type
        file_size = uploader_file.size
        img = Image.open(uploader_file)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,2,0,1))
            
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
    
def page3():
    '''我的智慧词典'''
    st.write('智慧词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        # 输出查询的单词内容
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.text('单词被查询次数为：' + str(times_dict[n]))
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)

def page4():
    '''我的留言区'''    
    with open('leave_messages.txt',encoding='utf-8')as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split('#')

    for i in message_list:
        if i[1] == "阿短":
            with st.chat_message('A'):
                st.write(i[1],':',i[2])
        elif i[1] == "编程猫":
            with st.chat_message('M'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是......',['阿短','编程猫'])
    new_message = st.text_input("想要说的话......")
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]    
            f.write(message)
def page5():
    '''亚文化圈子介绍与推荐'''
    st.write('时间问题暂未完成，敬请期待,目前只只做了部分链接')
    st.link_button('東方project','https://thwiki.cc/%E9%A6%96%E9%A1%B5')
            
if page == "我的兴趣推荐内容":
    page1()
elif page == "我的图像处理工具":
    page2()
elif page == "我的智慧词典":
    page3()
elif page == "我的留言区":
    page4()
elif page == '亚文化圈子介绍与推荐':
    page5()

#模版
#    st.write('我的兴趣推荐')
#    st.image('天象奇景.jpg')
#    with open('歌曲.mp3','rb') as f:
#        mymp3 = f.read()
#    st.audio(mymp3,format = "audio/mp3",start_time = 0)