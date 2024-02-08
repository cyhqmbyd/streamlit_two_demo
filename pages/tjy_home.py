'''我的主页'''
import streamlit as st
from PIL import Image
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
    st.write('《长津湖》')
    st.write('-----------------------------')
    st.write('你最喜欢看什么类型的电影呢？')
    cb1 = st.checkbox('科幻')
    cb2 = st.checkbox('动漫')
    cb3 = st.checkbox('动作')
    cb4 = st.checkbox('其他')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if True in l:
            st.write('真是个小电影迷')
        else:
            st.write('可以尝试看看一些电影哦')
    st.write('----------------------------')
    st.write('我的游戏推荐')
    st.write('FIFA足球')
    st.write('-----------------------------')
    st.write('我的书籍推荐')
    st.write('《明朝那些事儿》')
    st.write('-----------------------------')
    st.write('我的音乐推荐')
    with open('小粥会冒泡调查中.mp3','rb')as f:
        myMp3 = f.read()
    st.audio(myMp3, format = 'audio/mp3', start_time = 10)
    
def page2():
    #布局练习
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write('第一列')
    with col2:
        st.write('第二列')
    with col3:
        st.write('第三列')
        
    '''我的图像处理工具'''
    st.write(":sunglasses:图像处理小程序:sunglasses:")
    uploader_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploader_file:
        file_name=uploader_file.name
        file_type=uploader_file.type
        file_size=uploader_file.size
        img = Image.open(uploader_file)
        tab1,tab2,tab3,tab4=st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:    
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,0,1,2))
        with tab4:
            st.image(img_change(img,2,0,1))
        
def img_change(img,rc,rg,rb):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取所有的RGB值
            r = img_array[x,y][rc]
            g = img_array[x,y][rg]
            b = img_array[x,y][rb]
            img_array[x,y] = (r,g,b)
    return img

def page3():
    '''我的智慧词典'''
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8')as f:
        words_list = f.read().split('\n')

    #获取每行数据的序号、单词和解释
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')

    #将列表里面的数据导入字典中，{单词:[序号,n解释]}
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]

    #从本地文本中读取单词查询次数
    with open("check_out_times.txt",'r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    #将列表数据转换为二维列表
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    #转化为字典
    times_dict = {}
    #i--> ["1","13"]
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    
        
    #创建输入框
    word = st.text_input('请输入要查询的单词')
    #显示结果{"book":[1,"书本"]}
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
            
        st.write("查询次数:",times_dict[n])
        st.code(
            '''
            #恭喜你触发一个彩蛋，
            print("Hello World")
            '''
        )

    with open('check_out_times.txt','w',encoding='utf-8') as f:
        message =''
        for k ,v in times_dict.items():
            message += str(k)+'#'+str(v)+'\n'
        message=message[:-1]
        f.write(message)
def page4():
    '''我的留言区'''
    st.write('我的留言区')
    #内容读取,并整理成列表
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        message_list = f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i] = message_list[i].split('#')

    #将数据展示到留言板上
    for i in message_list:
        if i[1] =='男':
            with st.chat_message('🆚'):
                st.write(i[1],':',i[2])
            st.code(
            '''
            #恭喜你触发一个彩蛋，
            祝你在新的一年里财源滚滚、锦绣前程、一帆风顺、喜气洋洋、恭贺新禧、才高八斗
            '''
            )    
        elif i[1] =='女':
            with st.chat_message('❗'):
                st.write(i[1],':',i[2])
            st.code(
            '''
            #恭喜你触发一个彩蛋，
            祝你在新的 一年里一帆风顺,二龙腾飞,三羊开泰,四季平安,五 福临门,六六大顺,七星高照,八方来财,九九同心,十全十美
            '''
            )
    name = st.selectbox('我是……',['男','女'])
    new_message = st.text_input('想要说的话……')
    if st.button("留言"):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message = ''
            for i in message_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
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