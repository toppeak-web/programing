import tkinter as tk
from tkinter import messagebox
import json
import random

root = tk.Tk()
root.title("영어 단어 퀴즈")

# 오답 노트 파일 경로
mistakes_file = "mistakes.json"

# 데이터 파일에서 문제 불러오기
with open("output.json", "r", encoding="utf-8") as file:
    word_list = json.load(file)

# 오답 노트 파일에서 저장된 오답 데이터 불러오기
try:
    with open(mistakes_file, "r", encoding="utf-8") as mistakes_file:
        mistake_list = json.load(mistakes_file)
except FileNotFoundError:
    mistake_list = []

# 문제 범위 입력 받기
def start_quiz():
    global start, end, question_stack
    start = int(start_entry.get())
    end = int(end_entry.get())
    question_stack = random.sample(word_list[start - 1:end], len(word_list[start - 1:end]))
    ask_question()

def ask_question():
    global current_question
    if question_stack:
        current_question = question_stack.pop()
        question_label.config(text=f"Question: {current_question['예문']}")
    else:
        messagebox.showinfo("퀴즈 종료", "퀴즈가 종료되었습니다.")
        with open(mistakes_file, "w", encoding="utf-8") as mistakes_file:
            json.dump(mistake_list, mistakes_file)

def check_answer():
    user_input = answer_entry.get().strip().lower()
    correct_answer = current_question['의미'].lower()

    if user_input == correct_answer:
        messagebox.showinfo("정답", "정답입니다!")
        ask_question()
    else:
        messagebox.showerror("오답", f"틀렸습니다! 정답은 {current_question['의미']}입니다.")
        save_mistake()
        ask_question()

def save_mistake():
    mistake_list.append(current_question)

def show_mistakes():
    if mistake_list:
        messagebox.showinfo("오답 노트", "\n".join([f"예문: {item['예문']}\n정답: {item['의미']}" for item in mistake_list]))
    else:
        messagebox.showinfo("오답 노트", "오답이 없습니다.")

# GUI 구성 요소
start_label = tk.Label(root, text="시작 숫자를 입력하세요:")
start_label.pack()

start_entry = tk.Entry(root)
start_entry.pack()

end_label = tk.Label(root, text="끝 숫자를 입력하세요:")
end_label.pack()

end_entry = tk.Entry(root)
end_entry.pack()

start_button = tk.Button(root, text="시작하기", command=start_quiz)
start_button.pack()

question_label = tk.Label(root, text="")
question_label.pack()

answer_entry = tk.Entry(root)
answer_entry.pack()

submit_button = tk.Button(root, text="정답 확인", command=check_answer)
submit_button.pack()

show_mistakes_button = tk.Button(root, text="오답 노트 보기", command=show_mistakes)
show_mistakes_button.pack()

root.mainloop()
