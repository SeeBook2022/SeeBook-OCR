import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import torch
import os
import cv2
import matplotlib.pyplot as plt
from ocr_module import detect_text, img2gray2, preprocess_sentence

def title_ocr(stage2_model, image_list, api_key):
    # google api key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = api_key

    # 결과값을 저장할 리스트들 선언
    stage2_bbox_coord_list = []
    stage2_to_stage3 = []
    stage3_result = []

    # 실행버튼 생성
    execute_button = st.button('실행')


    if execute_button == True:

        # stage2
        results = stage2_model(image_list) # title detection
        stage2_df = results.pandas().xyxy
        for i, row in enumerate(stage2_df):
            stage2_bbox_coord_list.append(row.iloc[0].tolist()[:4]) # bbox coordinates

        for i, stage1_crop in enumerate(image_list):
            stage2_img_crop = stage1_crop[int(stage2_bbox_coord_list[i][1]):int(stage2_bbox_coord_list[i][3]), int(stage2_bbox_coord_list[i][0]):int(stage2_bbox_coord_list[i][2])].copy()
            stage2_to_stage3.append(stage2_img_crop) # image crop

        # stage3
        for img_array in stage2_to_stage3:
            img_transform = img2gray2(img_array) # 이미지 변환 적용
            stage3_output = detect_text(img_transform) # ocr 적용
            stage3_result.append(preprocess_sentence(stage3_output)) # 특수문자 제거

    
    return stage3_result