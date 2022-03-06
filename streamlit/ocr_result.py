import streamlit as st
import pandas as pd
import numpy as np
import webbrowser


def search_url(result_list):

    kyobo_url = []
    aladin_url = []
    yes24_url = []
    google_url = []
    youtube_url = []
    naver_url = []

    for result in result_list:
        url_k = f'https://search.kyobobook.co.kr/web/search?vPstrKeyWord={result}&orderClick=LET'
        kyobo_url.append(url_k)
        url_a = f'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord={result}&x=0&y=0'
        aladin_url.append(url_a)
        url_24 = f'http://www.yes24.com/Product/Search?domain=ALL&query={result}'
        yes24_url.append(url_24)
        url_g = f'https://www.google.com/search?q={result}&source=hp&ei=6ksiYtuOHKHhwAPkgJjoAg&iflsig=AHkkrS4AAAAAYiJZ-i2WkBkA6jENubG14wHc9kQ5xu4y&ved=0ahUKEwjbq4mX_az2AhWhMHAKHWQABi0Q4dUDCAk&uact=5&oq=%EC%8B%A4%EB%A7%88%EB%A6%B4%EB%A6%AC%EC%98%A8&gs_lcp=Cgdnd3Mtd2l6EAMyBQguEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOhEILhCABBCxAxCDARDHARDRAzoLCAAQgAQQsQMQgwE6CwguEIAEEMcBENEDOgQIABADOggIABCABBCxA1DKBFjFGWCqGmgFcAB4A4ABvwGIAZYRkgEEMC4xM5gBAKABAbABAA&sclient=gws-wiz'
        google_url.append(url_g)
        url_n = f'https://book.naver.com/search/search.nhn?query={result}'
        naver_url.append(url_n)
        url_y = f'https://www.youtube.com/results?search_query=책+리뷰+{result}'
        youtube_url.append(url_y)

    st.info('검색할 책을 선택해 주세요')


    if len(result_list) == 10:
        button10 = st.button(label = result_list[9])
        result_list.pop()

    if len(result_list) == 9:
        button9 = st.button(label = result_list[8])
        result_list.pop()

    if len(result_list) == 8:
        button8 = st.button(label = result_list[7])
        result_list.pop()

    if len(result_list) == 7:
        button7 = st.button(label = result_list[6])
        result_list.pop()

    if len(result_list) == 6:
        button6 = st.button(label = result_list[5])
        result_list.pop()

    if len(result_list) == 5:
        button5 = st.button(label = result_list[4])
        result_list.pop()

    if len(result_list) == 4:
        button4 = st.button(label = result_list[3])
        result_list.pop()

    if len(result_list) == 3:
        button3 = st.button(label = result_list[2])
        result_list.pop()

    if len(result_list) == 2:
        button2 = st.button(label = result_list[1])
        result_list.pop()

    if len(result_list) == 1:
        button1 = st.button(label = result_list[0])
        result_list.pop()



    st.info('검색할 url을 선택해 주세요')

    try:
        if button1:
            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[0])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[0])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[0])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[0])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[0])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[0])


        elif button2:

            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[1])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[1])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[1])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[1])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[1])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[1])

        elif button3:

            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[2])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[2])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[2])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[2])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[2])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[2])


        elif button4:

            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[3])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[3])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[3])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[3])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[3])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[3])

        elif button5:

            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[4])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[4])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[4])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[4])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[4])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[4])


        elif button6:

            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[5])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[5])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[5])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[5])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[5])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[5])


        elif button7:

            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[6])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[6])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[6])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[6])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[6])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[6])

        elif button8:

            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[7])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[7])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[7])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[7])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[7])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[7])

        elif button9:
            
            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[8])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[8])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[8])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[8])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[8])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[8])

        elif button10:
            
            if st.button('교보문고'):
                webbrowser.open_new_tab(kyobo_url[9])

            if st.button('알라딘'):
                webbrowser.open_new_tab(aladin_url[9])

            if st.button('Yes24'):
                webbrowser.open_new_tab(yes24_url[9])

            if st.button('구글'):
                webbrowser.open_new_tab(google_url[9])

            if st.button('유튜브'):
                webbrowser.open_new_tab(youtube_url[9])

            if st.button('네이버'):
                webbrowser.open_new_tab(naver_url[9])
    except:
        pass