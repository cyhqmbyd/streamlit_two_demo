'''我的主页'''
import streamlit as st
from PIL import Image
import time
page = st.sidebar.radio(
    '我的主页',
    [
        '我的兴趣推荐内容',
        '我的图像处理工具',
        '我的智慧词典',
        '我的留言区',
    ]
)
def page1():
    '''我的兴趣推荐'''
    st.write('我的电影推荐')
    c1,c2,c3 = st.columns(3)
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    with c1:
        st.image('q.jpg')
        st.write('绿皮书是一部深入人心的电影，通过托尼和谢利的旅程，展现了人性的复杂与美好。')
    with c2:
        st.image('w.jpg')
        st.write('肖申克的救赎是一部经典的人性之作，安迪的坚韧与智慧，改变了肖申克的命运，触动了无数观众的心灵。')
    with c3:
        st.image('e.jpg')
        st.write('楚门的世界揭示了现代社会对隐私和真实的扭曲，金凯瑞的出色表演令人震撼，引人深思。')
    st.write('我的游戏推荐')
    st.image('r.jpg')
    st.write('《绝地求生》(PUBG)是一款充满策略和竞技性的多人在线射击游戏。在游戏中，玩家需要在不断缩小的地图上与敌人展开激烈战斗，最后存活下来。')
    st.link_button('pubg官网', 'http://www.pubgmobile.com/en-US/')
    st.write('我的书籍推荐')
    st.image('t.jpg')
    st.write('《钢铁是怎样炼成的》是一部激励人心的自传体小说，通过保尔·柯察金的成长经历，展现了坚韧不拔、勇往直前的精神力量。')
    st.write('我的习题集推荐')
    c6,c7 = st.columns(2)
    with c6:
        st.image('y.jpg')
        st.write('万维中考模拟题是针对中考的全面、系统性的模拟试题，具有很高的参考价值。题目设计合理，难度适中，符合中考的命题规律。对于即将参加中考的学生来说，是一份非常宝贵的复习资料。')
    with c7:
        st.image('u.jpg')
        st.write('一本图书，初中英语版是一本适合初中生学习的英语教材，它注重学生的听、说、读、写全面发展。教材内容生动有趣，练习丰富多样，能够帮助学生在轻松愉快的氛围中提高英语水平。')
    

    # st.image('bcm_天象奇景.jpg')
    # with open('bcm_歌曲.mp3','rb') as f:
    #     myMp3 = f.read()
    # st.audio(myMp3, format = 'audio/mp3', start_time = 10)
    
def page2():
    #布局练习
    col1,col2 = st.columns([1,1])
    with col1:
        st.image('6.png')
        col3,col4 = st.columns([1,1])
        with col3:
            st.image('1.png')
        with col4:
            st.image('2.png')
    with col2:
        st.image('5.png')
    
    '''我的图像处理工具'''
    st.write(":sunglasses:图像处理小程序:sunglasses:")
    uploader_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
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
            st.image(img_change(img,1,0,2))
        with tab4:
            st.image(img_change(img,2,1,0))

def img_change(img,rc,rg,rb):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取所有的像素值，RGB=(245,27,104)--->RGB=(104,27,245)
            r = img_array[x,y][rc]
            g = img_array[x,y][rg]
            b = img_array[x,y][rb]
            img_array[x,y] = (r,g,b)
    return img

def page3():
    '''我的智慧词典'''
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
        
    #获取每行数据的序号、单词和解释
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')

    #将列表里面的数据导入字典中，{单词:[序号，n解释]}
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]

    #从本地文本中读取单词查询次数
    with open("check_out_times.txt") as f:
        times_list = f.read().split('\n')
        
    #将列表数据转为二维列表，获取到编号和查询次数
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')

    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    
    #创建输入框
    word = st.text_input('请输入要查询的单词！')
    #显示结果{"book":[1,"书本"]}
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.write("查询次数",times_dict[n])
        if word == 'coke':
            st.write('喜欢吗老弟')
        st.code(
            '''
            #恭喜你触发一个彩蛋，这是一行python代码程序
            print("Hello World")
            '''
        )
    with open('check_out_times.txt','w',encoding='utf-8')as f:
        message = ''
        for k,v in times_dict.items():
            message += str(k) + "#" + str(v) + '\n'
        message = message[:-1]
        f.write(message)

def page4():
    '''我的留言区'''
    st.write('我的留言区')
    #内容读取，并整理成列表
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split('#')

    #将数据展示到留言板上
    for i in message_list:
        if i[1] == '阿短':
            with st.chat_message('☕'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('💯'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是......',['阿短','编程猫'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
        
    
if page == '我的兴趣推荐内容':
    page1()
elif page == '我的图像处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()