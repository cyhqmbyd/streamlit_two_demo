'''我的首页'''
import streamlit as st
from PIL import Image
import copy

page = st.sidebar.radio('阿短首页', ['阿短的兴趣推荐', '阿短的图片处理工具', '阿短的智慧词典', '阿短的留言区'])

def page_1():
    '''阿短的推荐'''
    with open('aduan_歌曲.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('阿短的世界之旅')
    st.write('我在各种假期中可没闲着，而是在世界各地留下自己的足迹，如果你也喜欢游览名胜古迹、到网红点打卡、亲近大自然……那么就来看看我的丰富流程，参考一下吧！')
    st.write('')
    
    # 图片处理
    imgs_name_lst = ['aduan_去海边游泳.png', 'aduan_去森林里露营.png', 'aduan_去沙漠看金字塔.png', 'aduan_去雪山上滑雪.png']
    imgs_lst = []
    for i in imgs_name_lst:
        img = Image.open(i)
        img = img.resize((400, 300))
        imgs_lst.append(img)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.image(imgs_lst[0])
        st.write('去海边游泳')
        st.write('在海边游泳和在游泳池游泳感觉完全不同，海面有波浪，脚下是软软的沙子，在水里什么都看不清，而且，海水咸得发苦，别问我是怎么知道的……')
    with col2:
        st.image(imgs_lst[1])
        st.write('去森林里露营')
        st.write('森林里的夏天真的出乎意料的凉爽，甚至晚上还得加衣服，和家人们一起来顿野炊也是别有一番风味，即使是蚊虫的骚扰也无法赶走好心情！~')
    with col3:
        st.image(imgs_lst[2])
        st.write('去沙漠看金字塔')
        st.write('沙漠的白天非常热，但是当地人都把自己裹得严严实实，我们在这里看到了金字塔，比想象中要大得多，真实太壮观了！')
    with col4:
        st.image(imgs_lst[3])
        st.write('去雪山上滑雪')
        st.write('装备多到好半天才能穿上，飞吹在脸上就像刀割，人摔在雪上也非常狼狈，但当你掌握了技巧你会发现这一切都是值得的，太刺激了！')

def page_2():
    '''阿短的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # 显示图片处理界面
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键"另存为"保存图片')
            st.image(img)

def page_3():
    '''阿短的智慧词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('aduan_words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('aduan_check_out_times.txt', 'r', encoding='utf-8') as f:
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
        cixing, ciyi = words_dict[word][1].split('.')
        st.write('单词的意思是：', ciyi)
        st.text('单词的词性是：' + cixing + '.')
        st.text('这是词典中的第' + str(words_dict[word][0]) + '个单词')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('aduan_check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.text('单词被查询次数为：' + str(times_dict[n]))

def page_4():
    '''阿短的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('aduan_leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('aduan_leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img

if page == '阿短的兴趣推荐':
    page_1()
elif page == '阿短的图片处理工具':
    page_2()
elif page == '阿短的智慧词典':
    page_3()
elif page == '阿短的留言区':
    page_4()