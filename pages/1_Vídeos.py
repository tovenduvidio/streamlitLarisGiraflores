
import streamlit as st


st.set_page_config(layout='wide')




videos = ['https://www.youtube.com/watch?v=x04rGV9Lmrw', # 1
          'https://www.youtube.com/watch?v=4i2nN6LxSMQ', # 2
          'https://www.youtube.com/watch?v=4i2nN6LxSMQ', # 3
          'https://www.youtube.com/watch?v=5P3hLMF6ixY', # 4
          'https://www.youtube.com/watch?v=xP_ONJNV0-8', # 5
          'https://www.youtube.com/watch?v=X1PiF2h6LeI', # 6
          'https://www.youtube.com/watch?v=7zG6x26U8EE', # 7
          'https://www.youtube.com/watch?v=xdpZXh25e78', # 8
         ] 


st.title('Vídeos'.upper())

col = [None] * 2
contadorColuna = 0

col[0], col[1] = st.columns(2)

for valor in range(len(videos)):
    col[contadorColuna].video(videos[valor])

    contadorColuna += 1
    if contadorColuna > 1:
         contadorColuna = 0
    