import tkinter as tk
from tkinter import ttk, messagebox
import requests
import time
import random
from datetime import datetime, timedelta
import pyautogui

# 요청할 URL
url = "https://ticket.interpark.com/Contents/Sports/GoodsInfo?SportsCode=07006&TeamCode=PF001"

# 0.08~0.1초 간격으로 Date 헤더 정보를 가져와 출력하는 함수
def fetch_date_info():
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
            return kst_time
        else:
            print("Date 헤더를 찾을 수 없습니다.")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"요청 중 오류 발생: {e}")
        return None

def start_timer():
    selected_hour = int(hour_var.get())
    selected_minute = int(minute_var.get())
    selected_second = int(second_var.get())
    
    messagebox.showinfo("예약", f"시간: {selected_hour}시 {selected_minute}분 {selected_second}초로 예약되었습니다.")
    
    while True:
        server_time = fetch_date_info()
        if server_time:
            # 서버 시간과 사용자가 입력한 시간 비교
            if (server_time.hour == selected_hour and 
                server_time.minute == selected_minute and 
                server_time.second == selected_second):

                # F5 키로 새로고침
                pyautogui.press('f5')
                print(f"새로고침: {server_time.strftime('%Y-%m-%d %H:%M:%S')}")
                break
            # 0.08~0.1초 사이의 랜덤한 시간 대기
            wait_time = random.uniform(0.08, 0.1)
            time.sleep(wait_time)

# 메인 윈도우 생성
window = tk.Tk()
window.title("새로고침 타이머")
window.geometry("400x150")
window.attributes("-topmost", True)

# 시간, 분, 초 선택을 위한 변수
hour_var = tk.StringVar()
minute_var = tk.StringVar()
second_var = tk.StringVar()

# 24시간(00~23), 분/초(00~59) 리스트 생성
hours = [f"{i:02}" for i in range(24)]
minutes_seconds = [f"{i:02}" for i in range(60)]

# '시', '분', '초' 드롭다운과 라벨을 한 줄에 출력
label_frame = tk.Frame(window)
label_frame.pack(pady=10)

# 시 드롭다운 메뉴
hour_label = tk.Label(label_frame, text="시")
hour_label.grid(row=0, column=0, padx=5)
hour_dropdown = ttk.Combobox(label_frame, textvariable=hour_var, values=hours, state="readonly", width=5)
hour_dropdown.current(0)
hour_dropdown.grid(row=0, column=1, padx=5)

# 분 드롭다운 메뉴
minute_label = tk.Label(label_frame, text="분")
minute_label.grid(row=0, column=2, padx=5)
minute_dropdown = ttk.Combobox(label_frame, textvariable=minute_var, values=minutes_seconds, state="readonly", width=5)
minute_dropdown.current(0)
minute_dropdown.grid(row=0, column=3, padx=5)

# 초 드롭다운 메뉴
second_label = tk.Label(label_frame, text="초")
second_label.grid(row=0, column=4, padx=5)
second_dropdown = ttk.Combobox(label_frame, textvariable=second_var, values=minutes_seconds, state="readonly", width=5)
second_dropdown.current(0)
second_dropdown.grid(row=0, column=5, padx=5)

# 예약 버튼
start_button = tk.Button(window, text="예약", command=start_timer)
start_button.pack(pady=10)

# 메인 루프 시작
window.mainloop()