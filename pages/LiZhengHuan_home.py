'''my_homepage'''
# streamlit==1.28.2
import streamlit as st
# from time import sleep
# from stqdm import stqdm
from PIL import Image, ImageFilter
# from random import randint
from torch import nn, optim, tensor
import torch
# from LiZhengHuan_test import Model

# nat-pt

# 符号集：https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/        https://www.iconfont.cn/

# streamlit组件文档：http://cw.hubwiz.com/card/c/streamlit-manual/          https://docs.streamlit.io/

st.set_page_config(
    page_title="LZH's page",
    page_icon="📊",
    layout="centered",
)

with st.sidebar:
    page = st.radio(
        'My_Homepage', 
        [
            '兴趣推荐', 
            '图像处理工具', 
            '智慧词典', 
            '留言区', 
            '点一点', 
            # '线性回归模型', 
        ], 
        captions = ['看看我喜欢什么吧', '在线处理工具!', '在线查询!', '说说什么吧~', '你也来点一下吧!'] # , '体验一下什么是人工智能吧'
    )
    st.write("已选择***{}***".format(page))

# st.write("我的兴趣推荐")
#     st.image("天象奇景.jpg")
def page_1():
    '''兴趣推荐'''
    st.header("我的兴趣推荐🎨♥📆")
    with open("LiZhengHuan_霞光.mp3", "rb") as f:
        Xiaguang = f.read()
    st.audio(Xiaguang, format="audio/mp3", start_time=0)

    tab1, tab2 = st.tabs(["小说推荐", "音乐推荐"])
    with tab1:
        st.subheader("我最喜欢的小说推荐")
        st.write("我看过的最好看的小说是获得了第73届雨果奖最佳长篇小说奖的《三体》")
        st.write("《三体》一共拥有3部，而我最推荐《三体3：死神永生》。因为这一部所涉及的内容非常广，也是我认为《三体》三部中最有科幻感的一部。")
        st.image("LiZhengHuan_img.png")
        st.divider()
    with tab2:
        st.subheader("我最喜欢的音乐推荐")
        st.write("我最喜欢的音乐是钢琴曲《贝多芬病毒》，这个曲子是我练习过的曲子中我认为最好听的，同时也是我练习最久的曲子。")
        st.link_button("试听音乐", url='https://www.youtube.com/watch?v=a9JoHtHly-w')
        st.write("**Youtube平台的PianiCast**")
        st.divider()


def page_2():
    '''图像处理工具'''
    st.header(":sunglasses:图像处理小工具🔁🔀")
    uploader_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploader_file:
        file_name = uploader_file.name
        file_type = uploader_file.type
        file_size = uploader_file.size
        img = Image.open(uploader_file)
        st.info(f'已导入图片 {file_name}')
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['原图', '改色1', '改色2', '改色3', '黑白', '模糊'])
        with tab1:
            st.image(img_change(img.copy(), 0, 1, 2))
            st.divider()
            if st.toggle("下载此文件(原图)"):
                Down_load(img_change(img.copy(), 0, 1, 2), "(原图)")
        with tab2:
            st.image(img_change(img.copy(), 1, 0, 2))
            st.divider()
            if st.toggle("下载此文件(改色1)"):
                Down_load(img_change(img.copy(), 1, 0, 2), "(改色1)")
        with tab3:
            st.image(img_change(img.copy(), 2, 1, 0))
            st.divider()
            if st.toggle("下载此文件(改色2)"):
                Down_load(img_change(img.copy(), 2, 1, 0), "(改色2)")
        with tab4:
            st.image(img_change(img.copy(), 0, 2, 1))
            st.divider()
            if st.toggle("下载此文件(改色3)"):
                Down_load(img_change(img.copy(), 0, 2, 1), "(改色3)")
        with tab5:
            st.image(img.copy().convert('L'))
            st.divider()
            if st.toggle("下载此文件(黑白)"):
                Down_load(img.copy().convert('L'), "(黑白)")
        with tab6:
            slider = st.slider("滤镜强度", 0, 50, 10)
            st.image(img.copy().filter(ImageFilter.GaussianBlur(radius=slider)))
            st.divider()
            if st.toggle("下载此文件(模糊)"):
                Down_load(img.copy().filter(ImageFilter.GaussianBlur(radius=slider)), "(模糊)")

def Down_load(file, name):
    file_name = st.text_input("请输入保存时的文件名" + name)
    file_last = st.selectbox("选择文件后缀" + name, ["PNG", "JPEG", "JPG"], index=0)
    if file_name and file_last:
        # file.convert(file_last)
        file.save("download.png")
        with open("download.png", "rb") as f:
            down_load = st.download_button("下载文件" + name, f, file_name = file_name + "." + str(file_last).lower())

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB像素值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

def page_3():
    '''智慧词典'''
    st.header("智慧词典🎓")
    st.error("查询次数记录功能无法使用")
    with open('LiZhengHuan_words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 获取数据
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 列表-->字典{单词:释义}
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [i[0], i[2]]

    # 获取查询数据
    with open("LiZhengHuan_check_out_times.txt", "r") as f:
        times_list = f.read().split('\n')
    # 列表 --> 字典{序号:查询次数}
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[i[0]] = int(i[1])
        
    # 获取用户输入
    word = st.text_input('请输入要查询的单词')
    # 显示搜索结果
    if word in words_dict:
        with st.expander("单词'{}'的释义".format(word), expanded = True):
            st.write('   NO.{}'.format(words_dict[word][0]))
            st.write('   **{}**'.format(words_dict[word][1]))
            if words_dict[word][0] in times_dict:
                times_dict[words_dict[word][0]] += 1
            else:
                times_dict[words_dict[word][0]] = 1
                
            st.write('   此单词已被查询**{}**次'.format(times_dict[words_dict[word][0]]))
            with open('LiZhengHuan_check_out_times.txt', 'w') as f:
                message = ''
                for k,v in times_dict.items():
                    message += k + "#" + str(v) + "\n"
                message = message[:-1]
                f.write(message)

    elif word == '':
        pass
    elif word == 'python':
        st.balloons()
        st.code(
            '''
            # 恭喜你触发了彩蛋!
            print("surprise!")
            '''
        )
    else:
        st.warning("{}不存在, 请尝试其他单词".format(word))
    st.divider()

def page_4():
    st.error("留言区功能无法使用")
    '''留言区'''
    st.header('我的留言区💬💭')
    with st.expander('注意事项:', expanded = False):
        st.write(
            '''
            1. 请确保在输入了你的名称与发送内容后点击"发送"
            2. 此聊天区的消息上限为150条，超过上限的信息将被删除
            3. 请确保您的发送消息与名称中不包含"#"
            4. 请不要恶意刷屏，请文明用语
            '''
        )
    st.divider()
    # 内容读取
    if "value" not in st.session_state:
        st.session_state.value = []
    with open("LiZhengHuan_leave_messages.txt", "r", encoding='utf-8') as f:
        st.session_state.value = f.read().split("\n")
    for i in (range(len(st.session_state.value))):
        st.session_state.value[i] = st.session_state.value[i].split("#")
    
    # chat_box = st.container()
    for i in st.session_state.value:
        if i[1] == '阿短':
            with st.chat_message("🧑"):
                st.write(i[1], ': {}'.format(i[2]))
        elif i[1] == '编程猫':
            with st.chat_message("😺"):
                st.write(i[1], ': {}'.format(i[2]))
        else:
            with st.chat_message("user"):
                st.write(i[1], ': {}'.format(i[2]))

    def chat_update(name="", my_message=""):
        if name and my_message:
            st.session_state.value.append([int(st.session_state.value[-1][0])+1, name, my_message])
            with open('LiZhengHuan_leave_messages.txt', 'w', encoding='utf-8') as f:
                message = ''
                if len(st.session_state.value) > 150:
                    del st.session_state.value[0]
                for i in st.session_state.value:
                    message += "{}#{}#{}\n".format(i[0], i[1], i[2])
                message = message[:-1]
                f.write(message)
        elif not name and my_message:
            st.warning("请输入你的名字")

    name = st.text_input('我是...', max_chars=10)
    col1, col2 = st.columns([9, 1])
    with col1:
        my_message = st.text_input("说些什么...", max_chars=100)
    with col2:
        send = st.button("发送", on_click = chat_update, args = [name, my_message])

# def print_chat_message(message_list, chat_box, name = "", my_message = ""):
#     # 展示数据
#     if name and my_message:
#         message_list.append([int(message_list[-1][0])+1, name, my_message])
#     for i in message_list:
#         if i[1] == '阿短':
#             with chat_box:
#                 with st.chat_message("🧑"):
#                     st.write(i[1], ': {}'.format(i[2]))
#         elif i[1] == '编程猫':
#             with chat_box:
#                 with st.chat_message("😺"):
#                     st.write(i[1], ': {}'.format(i[2]))
#         else:
#             with chat_box:
#                 with st.chat_message("user"):
#                     st.write(i[1], ': {}'.format(i[2]))
        
            
def page_5():
    st.error("次数记录功能无法使用")
    if 'Count' not in st.session_state:
        st.session_state.Count = 0
        
    with open('LiZhengHuan_ClickTime.txt', 'r', encoding='utf-8') as f:
        st.session_state.Count = int(f.read())

    def count():
        st.session_state.Count += 1
        with open('LiZhengHuan_ClickTime.txt', 'w', encoding='utf-8') as f:
            f.write(str(st.session_state.Count))

    plus_button = st.button(":rainbow[你也点一下吧]👍🏻", on_click=count)
    st.header("点击次数 : {}".format(st.session_state.Count))

# def page_6():
#     '''线性回归模型'''
#     st.header("线性回归模型")
#     with st.expander('使用说明', expanded = False):
#         st.write(
#             """
            
#             """
#         )
#     x_data = st.text_input("请输入训练用数据1**(请严格遵守格式)**")
#     x_data = list(map(list, x_data.split(" ")))
#     for i in x_data:
#         i[0] = float(i[0])
#     x_data = tensor(x_data)
    
#     y_data = st.text_input("请输入训练用数据2**(请严格遵守格式)**")
#     y_data = list(map(list, y_data.split(" ")))
#     for i in y_data:
#         i[0] = float(i[0])
#     y_data = tensor(y_data)
    
#     Lr = st.number_input("请输入学习率**(请按情况调整)**", min_value = 0.0001, value = 0.01, step = 0.001)
#     times = st.number_input("请输入训练次数**(一般情况下越多越好)**", min_value = 50, value = 500, step = 10)

#     x_data, y_data, Lr, times
    
#     model = Model()
#     criterion = nn.BCELoss(reduction='mean')
#     optimizer = optim.SGD(model.parameters(), lr=Lr)
#     for epoch in range(times):      
#         y_pred = model(x_data)
#         loss = criterion(y_pred, y_data)
#         # print(f'Epoch: {epoch + 1}/100 | Loss: {loss.item():.4f}')
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#     test_x_data = tensor[[float(st.number_input("请输入测试数据"))]]
#     y_test_pred = model(test_x_data)
#     y_test_pred

if page == '兴趣推荐':
    page_1()
elif page == '图像处理工具':
    page_2()
elif page == '智慧词典':
    page_3()
elif page == '留言区':
    page_4()
elif page == '点一点':
    page_5()
# elif page == '线性回归模型':
#     page_6()