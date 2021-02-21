from tkinter import *
from tkinter import ttk, messagebox
import random


def get_dictionary():
    dictionary = {}
    with open("./五十音.csv", "r") as f1:
        list1 = f1.readlines()
        list1.remove(list1[0])
        for index in range(0, len(list1)):
            list1[index] = list1[index].rstrip('\n')
            temp_list = str(list1[index]).split(",")
            dictionary[temp_list[0]] = temp_list[1]
    return dictionary


def recite_start():
    def button_on_clicked(event=0):
        nonlocal current_character
        if dic[lst_for_recite[current_character]] == input_entry.get():  # 输入正确
            current_character += 1
            if len(lst_for_recite) == current_character:  # 列表遍历完成
                random.shuffle(lst_for_recite)
                current_character = 0
            lbl.configure(text=lst_for_recite[current_character])
            rounds.configure(text='Current: '+str(current_character))
        input_entry.delete(0, "end")

    def button1_on_clicked(event=0):
        nonlocal current_character
        if len(lst_for_recite) == 1:
            messagebox.showinfo(title='hint', message='Congratulations, you\'ve done with task!')
            window.destroy()
            return
        lst_for_recite.remove(lst_for_recite[current_character])
        if len(lst_for_recite) == current_character:
            random.shuffle(lst_for_recite)
            current_character = 0
        lbl.configure(text=lst_for_recite[current_character])
        rounds.configure(text='Current: '+str(current_character))
        total_rounds.configure(text='Total: '+str(len(lst_for_recite)))
        input_entry.delete(0, "end")

    current_character = 0
    lst_for_recite = []
    for index in range(0, 7):
        if selected[index].get() == 1:
            lst_for_recite = lst_for_recite + lst[index * 5:index * 5 + 5]
    if selected[7].get() == 1:
        lst_for_recite = lst_for_recite + lst[35:38]
    if selected[8].get() == 1:
        lst_for_recite = lst_for_recite + lst[38:43]
    if selected[9].get() == 1:
        lst_for_recite = lst_for_recite + lst[43:45]
    if selected[10].get() == 1:
        lst_for_recite = lst_for_recite + list(lst[45])

    if not lst_for_recite:
        messagebox.showinfo(title='hint', message='Please select at least one line')
        return

    random.shuffle(lst_for_recite)

    # 单词窗体创建
    window = Tk()
    window.title("あいうえお-learning")
    window.geometry("300x300")

    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    lbl = Label(window, text=lst_for_recite[current_character], font=("Arial Bold", 50))
    lbl.grid(row=0, column=0)

    rounds = Label(window, text='Current: '+str(current_character), font=("Arial Bold", 10))
    rounds.grid(row=0, column=0, sticky=(N, W))

    total_rounds = Label(window, text='Total: '+str(len(lst_for_recite)), font=("Arial Bold", 10))
    total_rounds.grid(row=0, column=0, sticky=(N, E))

    input_entry = Entry(window, width=3)
    input_entry.grid(row=0, column=0, sticky=S)
    input_entry.focus()

    btn = Button(window, text="ok", command=button_on_clicked)
    btn.grid(row=0, column=0, sticky=(E, S))
    window.bind("<Return>", button_on_clicked)

    btn1 = Button(window, text="get this out", command=button1_on_clicked)
    btn1.grid(row=0, column=0, sticky=(W, S))

    window.mainloop()


if __name__ == '__main__':
    # 生成五十音字典和输入列表
    dic = get_dictionary()
    length_of_dic = len(dic)
    original_lst = list(dic.keys())
    lst = original_lst

    #  五十音选择
    welcome = Tk()
    welcome.title("あいうえお-selection")
    welcome.geometry("600x500")

    title_frame = ttk.Frame(welcome)
    Label(title_frame, text='Select characters you want to recite', font=("Arial Bold", 20)).pack()
    title_frame.pack()

    character_frame = ttk.Frame(welcome)
    character_frame.pack()
    character_frame_l = ttk.Frame(character_frame)
    character_frame_r = ttk.Frame(character_frame)
    character_frame_l.pack(side='left')
    character_frame_r.pack(side='right')

    selected = [IntVar() for x in range(0, 11)]

    for i in range(0, 8, 2):
        Label(character_frame_l, text=lst[5 * i:5 * i + 5], font=("Arial Bold", 20)).pack()
        ttk.Checkbutton(character_frame_l, variable=selected[i], onvalue=1, offvalue=0).pack()

    for i in range(1, 7, 2):
        Label(character_frame_r, text=lst[5 * i:5 * i + 5], font=("Arial Bold", 20)).pack()
        ttk.Checkbutton(character_frame_r, variable=selected[i], onvalue=1, offvalue=0).pack()

    Label(character_frame_r, text=lst[35:38], font=("Arial Bold", 20)).pack()
    ttk.Checkbutton(character_frame_r, variable=selected[7], onvalue=1, offvalue=0).pack()

    Label(character_frame_l, text=lst[38:43], font=("Arial Bold", 20)).pack()
    ttk.Checkbutton(character_frame_l, variable=selected[8], onvalue=1, offvalue=0).pack()

    Label(character_frame_r, text=lst[43:45], font=("Arial Bold", 20)).pack()
    ttk.Checkbutton(character_frame_r, variable=selected[9], onvalue=1, offvalue=0).pack()

    Label(character_frame_l, text=lst[45], font=("Arial Bold", 20)).pack()
    ttk.Checkbutton(character_frame_l, variable=selected[10], onvalue=1, offvalue=0).pack()

    Button(welcome, text="go", command=recite_start).pack()

    welcome.mainloop()
