
import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
from collections import OrderedDict


st.set_page_config(layout='wide')


r = requests.get("https://docs.google.com/spreadsheets/d/1BsFhkBI0fAKxfo6iMegsqk3RjKWSczlWvBnfnysq0DA/export?format=xlsx&id=1BsFhkBI0fAKxfo6iMegsqk3RjKWSczlWvBnfnysq0DA")
open('karaoke.xlsx', 'wb').write(r.content)



baseMusicas = pd.read_excel('karaoke.xlsx')
baseMusicas['Artista e Música'] = baseMusicas['Artista'] + ' - ' + baseMusicas['Música']

listaArtistaMusica = baseMusicas[['Artista e Música']].values.tolist()
listaArtistaMusica = str(listaArtistaMusica).replace('[', '').replace(']', '').replace("'",'')
listaArtistaMusica = listaArtistaMusica.split(sep=', ')
listaArtistaMusica = list(OrderedDict.fromkeys(listaArtistaMusica))


listaLinkVideos = baseMusicas[['Link']].values.tolist()
listaLinkVideos = str(listaLinkVideos).replace('[', '').replace(']', '').replace("'",'')
listaLinkVideos = listaLinkVideos.split(sep=', ')
listaLinkVideos = list(OrderedDict.fromkeys(listaLinkVideos))




st.title('Karaoke'.upper())
filtrarMusica = st.selectbox('Filtre uma música', listaArtistaMusica)

guia1, guia2 = st.tabs(['Músicas', 'Planilha'])




with guia1:
    if filtrarMusica == '':
       st.markdown(':blue[Selecione uma música]')

    else:
        st.video(listaLinkVideos[int(listaArtistaMusica.index(filtrarMusica))])

with guia2:
    components.iframe("https://docs.google.com/spreadsheets/d/1BsFhkBI0fAKxfo6iMegsqk3RjKWSczlWvBnfnysq0DA", height=670, scrolling=True)
    
