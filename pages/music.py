import streamlit as st

st.title(':star: NewJeans Music Playlist :star:')
st.header('뉴진스 뮤직 플리')
music = ["OMG", "Ditto", "Attention", "Hype Boy", "Cookie", "Hurt"]
a = st.text_input('**찾고 싶은 뉴진스 노래를 입력하세요** : ', 'ex : OMG')
st.subheader("**Your pick is**")

if a == music[0] or a == 'omg' or a == 'Omg' or a == '오엠쥐':
    st.subheader("'OMG'")
    st.image('images.jpg', caption="NewJeans 'OMG', 2023.01.02")
    audio_file = open('01 OMG.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
elif a == music[1] or a == 'ditto' or a == 'DITTO' or a == '디토':
    st.subheader("'Ditto'")
    st.image('images.jpg', caption="NewJeans 'OMG', 2023.01.02")
    audio_file = open('02 Ditto.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
elif a == music[2] or a == 'attention' or a == 'ATTENTION' or a == '어텐션':
    st.subheader("'Attention'")
    st.image('다운로드.jpg', caption="NewJeans 1st EP 'New Jeans', 2022.08.01")
    audio_file = open('01 Attention.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
elif a == music[3] or a == 'hype boy' or a == 'HYPE BOY' or a == '하입보이':
    st.subheader("'Hype Boy'")
    st.image('다운로드.jpg', caption="NewJeans 1st EP 'New Jeans', 2022.08.01")
    audio_file = open('02 Hype Boy.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
elif a == music[4] or a == 'cookie' or a == 'COOKIE' or a == '쿠키':
    st.subheader("'Cookie'")
    st.image('다운로드.jpg', caption="NewJeans 1st EP 'New Jeans', 2022.08.01")
    audio_file = open('03 Cookie.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
elif a == music[5] or a == 'hurt' or a == 'HURT' or a == '헐트':
    st.subheader("'Hurt'")
    st.image('다운로드.jpg', caption="NewJeans 1st EP 'New Jeans', 2022.08.01")
    audio_file = open('04 Hurt.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
elif a == 'ex : OMG':
    st.write('')
else:
    st.write('찾을 수 없습니다...')






