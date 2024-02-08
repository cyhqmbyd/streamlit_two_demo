'''我的主页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio(
    '我的主页',
    [
        '我的兴趣推荐',
        '我的图像处理工具',
        '我的智慧词典',
        '我的留言区',
        '习题'
    ]
)
def page1():
    '''我的兴趣推荐'''
    st.title('我的兴趣推荐')
    st.header('我的爱好')
    st.subheader('打篮球和玩魔方')
    
    st.header('我最喜欢的科目')
    st.subheader('数学和体育')
    
    st.header('我推荐的电影')
    st.subheader('《哪吒之魔童降世》')
    st.image("《哪吒之魔童降世》.png")
    st.write('《哪吒之魔童降世》主要讲能量巨大的混元珠被元始天尊收服，一分为二，分别是灵珠和魔丸。太乙真人受命将灵珠托生哪吒身上，然而阴差阳错的，灵珠被申公豹偷走，而魔丸托生在了哪吒身上，出生后的哪吒受魔丸的影响成为了混世魔王，而哪吒在面对百姓的误会以及即将来临的天雷时，奋起反抗，相信“我命由我不由天”，最后成为解救百姓的大英雄。')

    st.subheader('哪吒')
    st.image('哪吒1.png')
    st.write('古代神话故事中，哪吒生来异象，年幼时大闹东海龙宫，杀龙取筋；后参与封神大战，过关斩将护周伐纣和降妖除魔的经典故事广为流传到如今。封神里的哪吒身为灵珠子转世的玉虚弟子之一，是无魂魄无血肉之躯的莲花化身，具有师传的三头八臂神功和八件武器，元始天尊钦点的周军大先锋，深为周军战力依仗。')

    st.subheader('傲丙')
    st.image('傲丙1.png')
    st.write('敖丙是东海龙王的三太子。父亲为东海龙王敖光（不叫敖广），兵器为一杆方天画戟，坐骑为逼水兽。')
        
    st .subheader('音乐推荐')
    with open('歌曲.mp3','rb') as f:
        myMp3 = f.read()
    st.audio(myMp3, format = 'audio/mp3', start_time = 157)
    
def page2():
    '''我的图像处理工具'''
    st.write(":sunglasses:图像处理小程序:sunglasses:")
    uploader_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploader_file:
        file_name = uploader_file.name
        filr_type = uploader_file.type
        file_size = uploader_file.size
        img = Image.open(uploader_file)
        tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_chang(img,1,0,2))
        with tab3:
            st.image(img_chang(img,2,1,0))
        with tab4:
            st.image(img_chang(img,0,2,1))

def img_chang(img,rc,rg,rb):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取所有的像素值， RGB=（245,27,104--->RGB=(104,27,245)）
            r = img_array[x,y][rc]
            g = img_array[x,y][rg]
            b = img_array[x,y][rb]
            img_array[x, y] = (r,g,b)
    return img

def page3():
    '''我的智慧词典'''
    st.write('智慧词典')
    with open('words_space.txt', 'r', encoding='utf-8') as f:
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

    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
        
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    #显示输入框
    word = st.text_input('请输入要查询的单词！')
    #显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        st.write("查询次数",times_dict[n])
        st.code(
            '''
            #恭喜你触发一个彩蛋，这是一行python代码程序
            print(Hello word)
            '''
        )
        st.snow()
        
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
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split('#')
        
    #将数据展示到留言板
        for i in message_list:
            if i[1] == '阿短':
                with st.chat_message('☕'):
                    st.write(i[1],':',i[2])
            elif i[1] == '编程猫':
                with st.chat_message('💯'):
                    st.write(i[1],':',i[2])
    name = st.selectbox('我是.....', ['阿短','编程猫'])
    new_message = st.text_input('想要说的话.....')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in message_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page5():
    '''练习'''
    
    #单选题
    st.write('如果将“收入100元”记作“+100元”，那么“支出50元”应记作（）？')
    cb1 = st.checkbox('A.+50元')
    cb2 = st.checkbox('B.-50元')
    cb3 = st.checkbox('C.+150元')
    cb4 = st.checkbox('D.-150元')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == False and cb2 == True and cb3 == False and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')      

    #单选题
    st.write('下列算式正确的是')
    cb1 = st.checkbox('A.(-14)-5=-9')
    cb2 = st.checkbox('B.0-(-3)=3')
    cb3 = st.checkbox('C.(-3)-(-3)=-6')
    cb4 = st.checkbox('D.|5-3|=-(5-3)')
    b1 = st.button('第2题答案')
    if b1:
        if cb1 == False and cb2 == True and cb3 == False and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')   
 
if page == '我的兴趣推荐':
    page1()
elif page == '我的图像处理工具':
    page2()
elif page == '我的智慧词典':
    page3()
elif page == '我的留言区':
    page4()
elif page == '习题':
    page5()