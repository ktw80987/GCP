import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

st.subheader('DataFrame', divider='rainbow')

df = pd.DataFrame(
    [
        {'명령어': 'st.selectbox', '평점':4, 'is_widget' : True},
        {'명령어': 'st.ballons', '평점':5, 'is_widget' : False},
        {'명령어': 'st.selectbox', '평점':3, 'is_widget' : True}
    ]
)

st.code('st.date_editor(data, width, height, use_cointainer_width=False, '
        +'hide_index=None, column_color=None, num_rows=\'fixed\', disabled=False, key=None)')

st.caption(
    'data: DataFrame,\n'
    +'width: int,\n'
    +'height: int,\n'
    +'use_container_width: bool,\n'
    +'hide_index: bool,\n'
    +'column_color: dict,\n'
    +'num_rows: str,\n'
    +'disabled: bool,\n'
    +'key: str\n'
)

st.data_editor(df, use_container_width=True, num_rows='fixed', key=1)
st.divider()
st.subheader('hide_index=True')
st.data_editor(df, height=None, use_container_width=True, hide_index=True, column_order=None, key=2)
st.divider()
st.subheader('hide_index=False')
st.data_editor(df, height=None, use_container_width=True, hide_index=False, column_order=None, key=3)

st.divider()
st.subheader('column_config')
edit_df = st.data_editor(df, column_config={
    "명령어": "Streamlit 명령어",
    "평점": st.column_config.NumberColumn(
        label='여러분이 부여하는 평점',
        help='이 명령어에 몇 점을 부여하시겠습니까?(1-5)',
        min_value=1,
        max_value=5,
        step=1
        ),
    "is_widget": "위젯 여부"
    },
    use_container_width=True,
    disabled={'명령어', 
            'is_widget'},
    hide_index=True,
    key=4
    )