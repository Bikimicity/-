import requests
import time
import random
from datetime import datetime, timedelta

# 요청할 URL
url = "https://ticket.interpark.com/Contents/Sports/GoodsInfo?SportsCode=07006&TeamCode=PF001"

# 0.08~0.1초 간격으로 Date 헤더 정보를 가져와 출력하는 함수
def fetch_date_info():
    while True:
        try:
            # GET 요청을 보냄
            response = requests.get(url)
            
            # 응답 헤더에서 'Date' 헤더 값을 가져옴
            server_date = response.headers.get('Date')

            if server_date:
                # 'Date' 헤더의 형식에 맞게 파싱 (형식: 'Thu, 26 Sep 2024 06:41:20 GMT')
                server_time = datetime.strptime(server_date, '%a, %d %b %Y %H:%M:%S GMT')

                # 9시간 더해서 한국 시간으로 변환
                kst_time = server_time + timedelta(hours=9)

                # 한국 시간 출력
                print(f"서버 시간 (KST): {kst_time.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print("Date 헤더를 찾을 수 없습니다.")

            # 0.08~0.1초 사이의 랜덤한 시간 대기
            wait_time = random.uniform(0.08, 0.1)
            time.sleep(wait_time)
        
        except requests.exceptions.RequestException as e:
            print(f"요청 중 오류 발생: {e}")
            break

# 함수 실행
fetch_date_info()