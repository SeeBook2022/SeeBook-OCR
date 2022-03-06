import streamlit as st
import cv2
from PIL import Image
import numpy as np

# 이미지 로드
def load_img(img):
    return Image.open(img)
    
# opencv2로 읽을 수 있게 변환
def cvt(img):
    img = np.array(img.convert('RGB'))
    img = cv2.cvtColor(img, 1)
    return img

# 사진 회전 
def rotation(img):
    return img.rotate(180)

# 클릭 좌표와 bbox 비교
def compare(bbox_list, click_point):
    for bbox in bbox_list:
        x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2],bbox[3]
        if (x1 < click_point[0] < x2) and (y1 < click_point[1] < y2):
            return bbox


# 읽어온 이미지 파일에 bbox 그리기
def make_bbox(img, point_list):
    for point in point_list:
        x1, y1, x2, y2 = int(point[0]), int(point[1]), int(point[2]), int(point[3])
        cv2.rectangle(img, (x1, y1), (x2, y2), color = (0, 255, 0), thickness = 2)   


# 책 선택 최종 결과물 이미지 나타내는 함수 -  선택된 bbox 표시 및 음영 처리
def final_result_img(img, click_list, bbox_list):
    for bbox in bbox_list:
        x1, y1, x2, y2 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        sub_img = img[y1:y2, x1:x2]

        if tuple(bbox) not in click_list:
            black_rect = np.zeros(sub_img.shape, dtype=np.uint8) * 255 
            res = cv2.addWeighted(sub_img, 0.3, black_rect, 0.7, 1.0)
            img[y1:y2, x1:x2] = res


# 타이틀 설정
st.title('책 선택 테스트...')

# 업로드 파트 
image_file = st.file_uploader("Upload Image", type=['jpg', 'jpeg'])

# 전역 변수 선언
global click_list
click_list = set()

if image_file is not None:
    our_image = load_img(image_file)  
    
    if st.button('사진 회전'):
        our_image = cvt(rotation(our_image)) 
        st.image(our_image)
    else:
        our_image = cvt((our_image)) 
        st.image(our_image)    

    def on_mouse(event, x, y, flags, param):
        global click_list
        make_bbox(our_image, stage1_bbox_list)
        
        if event == cv2.EVENT_LBUTTONDOWN:
            bbox = compare(stage1_bbox_list, (x, y))
            x1, y1, x2, y2 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])            
                    
            cv2.rectangle(our_image, (x1, y1), (x2, y2), color = (0, 255, 0), thickness = 30)  
            click_list.add(tuple(bbox)) 
    
    # 버튼 설정
    col1, col2 = st.columns([10, 1]) # 버튼 위치 조절 ()
    
    with col1:
        if st.button('Select'):
            cv2.namedWindow('image', flags=cv2.WINDOW_NORMAL)
            cv2.resizeWindow(winname='image', width=900, height=700)
            cv2.setMouseCallback('image', on_mouse)
            
            while(True):

                cv2.imshow('image', our_image)

                k = cv2.waitKey(1) & 0xFF
                if k == 27:    # ESC 키 눌러졌을 경우 종료
                    break
                
            cv2.destroyAllWindows()
            final_result_img(our_image, click_list, stage1_bbox_list)
            st.image(our_image)
    
    with col2:    
        if st.button('Next'):
            pass