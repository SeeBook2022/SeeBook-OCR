from google.cloud import vision
import os
import io
import cv2
import re

def detect_text(img_bytes):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    # with io.open(path, 'rb') as image_file:
    #     content = image_file.read()
        
    image = vision.Image(content=img_bytes) # byte로 받아서 바로 실행

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    # 제목을 한 문장으로 추출할 수 있도록 코드 수정 (공백 제거)
    result = ''
    for idx, text in enumerate(texts):
        if idx > 0: result += text.description 
    return result

# 이미지 변환 함수1(grayscale, bright, contrast)

def img2gray(image_array):
    img_gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    add_dst = cv2.add(img_gray, 100) # 밝기 조절
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(4, 4)) # 대비 조절
    gray_cont_dst = clahe.apply(add_dst)

    img_bytes = cv2.imencode('.jpg', gray_cont_dst)[1].tobytes()

    return img_bytes

# 이미지 변환 함수2(grayscale, resize, bright)

def img2gray2(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 흑백 처리
    img_gray = cv2.resize(img_gray, dsize=(0,0), fx = 1.5, fy= 1.5, interpolation=cv2.INTER_AREA) # resize
    add_dst = cv2.add(img_gray, 30) # 밝기 조절
    
    img_bytes = cv2.imencode('.jpg', add_dst)[1].tobytes()

    return img_bytes

# 특수문자 제거 함수

def preprocess_sentence(sentence):
    sentence = re.sub('[-=+,「#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》 ]','', sentence)
    sentence = sentence.replace(' ', '') # 공백 제거
    sentence = sentence.strip() # 양쪽 공백 제거
    return sentence

