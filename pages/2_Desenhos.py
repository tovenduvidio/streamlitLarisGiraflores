import streamlit as st

st.set_page_config(layout='wide')


escolherDesenho = st.sidebar.radio('Desenhos', ('Tom e Jerry'.upper(),
                                                'Pica-Pau'.upper(),
                                                'Looney Tunes'.upper(),
                                                'Kick Buttowski'.upper()))

videosTomJerry = ['https://www.youtube.com/watch?v=W7uA0Om69DM', # 1
                  'https://www.youtube.com/watch?v=Hd0v0tVyNb8', # 2
                  'https://www.youtube.com/watch?v=nwTatevEkT0', # 3
                  'https://www.youtube.com/watch?v=5jTmaMeBqHo', # 4
                  'https://www.youtube.com/watch?v=iSmK-yH-yns', # 5
                  'https://www.youtube.com/watch?v=877W92yLPmY', # 6
                  'https://www.youtube.com/watch?v=pMG_5us-cxQ', # 7
                  'https://www.youtube.com/watch?v=DLHArGxoVdY', # 8
                  'https://www.youtube.com/watch?v=fhER6PRgHms', # 9
                  'https://www.youtube.com/watch?v=zbiD3Lzs_04', # 10
                  'https://www.youtube.com/watch?v=OhsTz4BF_Yk', # 11
                  'https://www.youtube.com/watch?v=272pwW5yRYY', # 12
                  'https://www.youtube.com/watch?v=YS7K9zuD0rk', # 13
                  'https://www.youtube.com/watch?v=fEYIt0OAnRI', # 14
                  ] 



videosPicaPau = ['https://www.youtube.com/watch?v=xAHxPE3NL6M', # 1
                 'https://www.youtube.com/watch?v=LfSxCq21GWY', # 2
                 ]


videosLooneyTunes = ['https://www.youtube.com/watch?v=aL-s-LexxL8', # 1
                    'https://www.youtube.com/watch?v=fn0vMWDYMV4', # 2
                    'https://www.youtube.com/watch?v=NxpkQaOEN_A', # 3
                    'https://www.youtube.com/watch?v=0E-LJ6nUV1Q', # 4
                    'https://www.youtube.com/watch?v=clq76orKd4k', # 5
                    'https://www.youtube.com/watch?v=cWgtzKk9TSo', # 6
                    'https://www.youtube.com/watch?v=KPaoG6IlzfM', # 7
                    'https://www.youtube.com/watch?v=w0colKbVluY', # 8
                    'https://www.youtube.com/watch?v=qg4RHDWk6fk', # 9
                    'https://www.youtube.com/watch?v=xPp6SKHOD4U', # 10
                    'https://www.youtube.com/watch?v=y2kHpdJuvTc', # 11
                    'https://www.youtube.com/watch?v=49j-f1x-NpU', # 12
                    'https://www.youtube.com/watch?v=1UXaB4WrXAE', # 13
                    'https://www.youtube.com/watch?v=ZIBVwBq-mVs', # 14
                    ] 



videosKickButtowski = ['https://www.youtube.com/watch?v=1HLPH_3J_WQ', # 1
                     'https://www.youtube.com/watch?v=JdHlXqiw-mw', # 2
                     'https://www.youtube.com/watch?v=FjC1bNWZB4k', # 3
                     'https://www.youtube.com/watch?v=nrd1PINTprc', # 4
                    ] 


if escolherDesenho == 'Tom e Jerry'.upper():
    st.title(escolherDesenho.upper())

    col = [None] * 2
    contadorColuna = 0

    col[0], col[1] = st.columns(2)

    for valor in range(len(videosTomJerry)):
        col[contadorColuna].video(videosTomJerry[valor])

        contadorColuna += 1
        if contadorColuna > 1:
            contadorColuna = 0
    

if escolherDesenho == 'Pica-Pau'.upper():
    st.title(escolherDesenho.upper())

    col = [None] * 2
    contadorColuna = 0

    col[0], col[1] = st.columns(2)

    for valor in range(len(videosPicaPau)):
        col[contadorColuna].video(videosPicaPau[valor])

        contadorColuna += 1
        if contadorColuna > 1:
            contadorColuna = 0
    


if escolherDesenho == 'Looney Tunes'.upper():
    st.title(escolherDesenho.upper())

    col = [None] * 2
    contadorColuna = 0

    col[0], col[1] = st.columns(2)

    for valor in range(len(videosLooneyTunes)):
        col[contadorColuna].video(videosLooneyTunes[valor])

        contadorColuna += 1
        if contadorColuna > 1:
            contadorColuna = 0


if escolherDesenho == 'Kick Buttowski'.upper():
    st.title(escolherDesenho.upper())

    col = [None] * 2
    contadorColuna = 0

    col[0], col[1] = st.columns(2)

    for valor in range(len(videosKickButtowski)):
        col[contadorColuna].video(videosKickButtowski[valor])

        contadorColuna += 1
        if contadorColuna > 1:
            contadorColuna = 0
    


