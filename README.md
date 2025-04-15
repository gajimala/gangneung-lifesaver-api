# 인명구조 대작전 Lifesaver Map

강릉 및 주문진 지역의 인명구조함 위치 데이터를 API로 제공하고,  
이를 네이버 지도 및 카카오 지도에 시각화하는 프로젝트입니다.

## 구조

```
lifesaver-map-project/
├── app/
│   ├── main.py                  # FastAPI 서버
│   └── gangneung_lifesavers.json  # 구조함 위치 데이터
├── public/
│   ├── lifesaver-map-naver.html # 네이버 지도 HTML
│   └── lifesaver-map-kakao.html # 카카오 지도 HTML
```

## 배포 API 주소
https://gangneung-lifesaver-api-vcj2.onrender.com/lifesavers

## 지도 설정
- 중심 좌표: 강릉 (37.75, 128.9)
- 마커 클릭 시 주소 및 구조함 종류 출력
