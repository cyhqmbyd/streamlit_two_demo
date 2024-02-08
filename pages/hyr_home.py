'''我的主页'''
import streamlit as st
from PIL import Image
import time

page=st.sidebar.radio(
    '我的主页',
    [
        '我的兴趣推荐内容',
        '我的图像处理工具',
        '我的智慧词典',
        '我的留言区',
        '好书分享会',
    ]
)

def page1():
    '''我的兴趣推荐内容'''
    st.balloons()
    st.title('我的兴趣推荐内容:')
    st.write('欢迎来到hyr的兴趣推荐内容，下面是我推荐的电影和书籍.....')
    with open('高山流水(古筝).mp3','rb') as f:
        myMp3=f.read()
    st.audio(myMp3,format='audio/mp3',start_time=2)
    st.write(':one:我最喜欢的电影:')
    st.write('《长安三万里》:clapper:')
    st.write('《长安三万里》讲述了在唐朝安史之乱爆发后数年，吐蕃大军攻打西南。大唐节度使高适交战不利，长安岌岌可危，困守孤城的高适向监军太监回忆起自己与李白的系列往事。')
    st.image('长安三万里海报.jpg')
    st.write(':two:我最喜欢的书籍:')
    st.write(':microphone:《基督山伯爵》:microphone:')
    st.write('主人公唐代斯因替波拿巴党人送信而造诬陷，在订婚当日遭逮捕，蒙冤入狱十四年，未婚妻嫁给仇人，父亲抑郁而亡。最终，获得宝藏，化身"基督山伯爵"，复仇，并带爱人海戴远走高飞，笑傲江湖。')
    st.write('（《基督山伯爵》是法国作家大仲马于1844年创作的长篇小说，感兴趣的话可以看一下，书挺厚的~~~）:school:')    
    st.image('基督山伯爵.jpg')
    st.write(':three:我的爱好:')
    st.write('弹古筝,编程和打羽毛球')
    st.image('古筝.jpg')
    st.write(':four:我最难忘的旅行:')
    st.write('这个假期去深圳爬了一趟七娘山')
    st.image('深圳七娘山风景图.jpeg')

def page2():
    '''我的图像处理工具'''
    st.title(":sunglasses:图像处理工具:sunglasses:")
    st.write("点击下面的Browse files就可以上传图片了！")    
    uploader_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploader_file:
        file_name=uploader_file.name
        file_type=uploader_file.type
        file_size=uploader_file.size
        img=Image.open(uploader_file)
        tab1,tab2,tab3,tab4,tab5=st.tabs(["原图","改色1","改色2","改色3"])
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
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB值
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
    
def page3():
    '''我的智慧词典'''
    st.title(':sunglasses:智慧词典:sunglasses:')
    #进度条
    roading = st.progress(0, '开始加载')
    for i in range(1, 101, 1):
        time.sleep(0.02)
        roading.progress(i, '正在加载'+str(i)+'%')
    roading.progress(100, '加载完毕！')
    st.write('请在下面方框中写入要查询的单词，如有单词未出现注释，是词典中未含有此单词，请见谅!')
    with open('words_space.txt',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    #获取每行数据的序号，单词和解释
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    #将列表里面的数据导入字典中，{单词:[序号,n解释]}
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    #从本地文本中读取单词查询次数
    with open("check_out_times.txt") as f:
        times_list=f.read().split('\n')
    #将列表数据转为二维列表,获取到编号和查询次数
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    #创建输入框
    word=st.text_input('请输入要查询的单词!')
    #显示结果
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n] +=1
        else:
            times_dict[n]=1
        st.write("查询次数",times_dict[n])
        st.code(
            '''
            恭喜你中了一个限量版彩蛋，下面是一行python代码程序
            print('Hello World')
            '''
        )
        st.balloons()
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in times_dict.items():
                message+=str(k)+"#"+str(v)+'\n'
            message=message[:-1]
            f.write(message)
    
def page4():
    '''我的留言区'''
    st.title('留言区')
    st.write('欢迎来到留言区,可以再这里发表你的看法:coffee::coffee:')
    #内容读取，并整理成列表
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        message_list=f.read().split('\n')
    for i in range(len(message_list)):
        message_list[i]=message_list[i].split('#')
    #将数据展示在显示留言板上
    st.write('在下方选择人物并留言,如果没有立刻出现留言内容，可以点击网页上方刷新的按钮')    
    for i in message_list:
        if i[1]=='阿短':
            with st.chat_message('✨'):
                st.write(i[1],':',i[2])
        elif i[1]=='编程猫':
            with st.chat_message('☕'):
                st.write(i[1],':',i[2])
    name=st.selectbox('我是.....',['阿短','编程猫'])
    new_message=st.text_input('想要说的话.....')
    if st.button('留言'):
        message_list.append([str(int(message_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message=''
            for i in message_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)

def page5():
    '''好书分享会'''
    st.title('好书分享会:open_book:')
    #跳转按钮
    st.write('欢迎来到好书分享会,请点击下方按钮前往分享会主页~~:books::books::books::books:')
    go = st.selectbox('点击方框下方的按钮即可去往好书分享会主页面~~', ['我的贴吧'])
    if go == '我的贴吧':
        st.link_button('前往主页', 'https://tieba.baidu.com/p/8889415226?fid=21841105&pid=149743289565&cid=0#149743289565')
        
        
if page =='我的兴趣推荐内容':
    page1()
elif page=='我的图像处理工具':
    page2()
elif page=='我的智慧词典':
    page3()
elif page=='我的留言区':
    page4()
elif page=='好书分享会':
    page5()