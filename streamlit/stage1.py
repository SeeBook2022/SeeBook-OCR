# import streamlit as st
import pandas as pd
import numpy as np
import webbrowser
import torch
import os
import cv2
import matplotlib.pyplot as plt

# stage1 모델 설정
stage1_model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/parkjinwoo/Desktop/streamlit/stage1_m_epochs_50.pt')
stage1_model.conf = 0.3

# 테스트 이미지 가져오기
test_image = []
image_path = '/Users/parkjinwoo/Desktop/streamlit/test_image/test6.jpg'
test_image.append(cv2.imread(image_path)[..., ::-1])


def spine_detect(stage1_model, image_list):
    
    results = stage1_model(test_image)
    stage1_df = results.pandas().xyxy[0]

    # 전달할 리스트
    stage1_bbox_coord_list = []
    for i in range(stage1_df.shape[0]):
        stage1_bbox_coord_list.append(stage1_df.iloc[i][:4].tolist())
    
    return stage1_bbox_coord_list