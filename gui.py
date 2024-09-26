import tkinter as tk
from tkinter import ttk, messagebox

def start_timer():
    selected_hour = hour_var.get()
    selected_minute = minute_var.get()
    selected_second = second_var.get()
    
    messagebox.showinfo("예약", f"시간: {selected_hour}시 {selected_minute}분 {selected_second}초로 예약되었습니다.")

# 메인 윈도우 생성
window = tk.Tk()
window.title("새로고침 타이머")
window.geometry("400x150")

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