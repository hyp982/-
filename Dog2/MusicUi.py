import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import Music

root = tk.Tk()
root.title('胡怡平音乐下载')
root.geometry('900x700+200+200')
root.iconbitmap('img\\hyp.ico')

img = tk.PhotoImage(file='img\\kugou.png')
tk.Label(root, image=img).pack()



def del_select():
    for item in tree_view.get_children(''):
        tree_view.delete(item)


def Search():
    Song_name = Song_va.get()
    if len(Song_name) > 1:
        MusicInfo = Music.Music(Song_name)
        # tickets = [
        #     {'SerialNo': 0, 'TravelNumber': 'G539', 'DepartureTime': '06:52', 'ArrivalTime': '08:11', 'TimeTime': '01:19', 'PremiumSeat': '无', 'FirstClassSeat': '无', 'SecondClassSeat': '有', 'SoftSleeper': '', 'HardSleeper': '', 'HardSeat': '', 'Noseat': ''},
        #  ]
        # 往树状图中插入数据
        del_select()
        for index, dit in enumerate(MusicInfo):
            tree_view.insert('', index + 1, values=(
                dit['Num'],
                dit['MusicId'],
                dit['MusicHash'],
                dit['SingerName'],
                dit['SongName'],
            ))
    else:
        tkinter.messagebox.showerror(title='警告', message='输入有误')


def Download():
    Num = Down_va.get()
    Song_name = Song_va.get()
    if len(Num) >= 1 and len(Song_name) >= 1:
        MusicInfo = Music.Music(Song_name)
        dit = MusicInfo[int(Num)]
        Music.GetMusic(dit['MusicHash'], dit['MusicId'])
        tkinter.messagebox.showinfo(title='温馨提示', message=f'歌曲{dit["SongName"]}下载完成')
    else:
        tkinter.messagebox.showerror(title='警告', message='输入有误')


def GetAll():
    Song_name = Song_va.get()
    if len(Song_name) > 1:
        MusicInfo = Music.Music(Song_name)
        for dit in MusicInfo:
            Music.GetMusic(dit['MusicHash'], dit['MusicId'])
    else:
        tkinter.messagebox.showerror(title='警告', message='输入有误')



search_frame = tk.Frame(root)
search_frame.pack(pady=20)

Song_va = tk.StringVar()
tk.Label(search_frame, text='歌手/音乐名:', font=('黑体', 15)).pack(side=tk.LEFT)
tk.Entry(search_frame, relief='flat', textvariable=Song_va).pack(side=tk.LEFT, padx=10)
tk.Button(search_frame, text='搜索', font=('黑体', 12), relief='flat', bg='#f5b488', padx=10, command=Search).pack(
    side=tk.LEFT, padx=2)

Down_va = tk.StringVar()
tk.Label(search_frame, text='歌曲序号:', font=('黑体', 15)).pack(side=tk.LEFT, anchor='e')
tk.Entry(search_frame, relief='flat', textvariable=Down_va).pack(side=tk.LEFT, padx=10)
tk.Button(search_frame, text='下载', font=('黑体', 12), relief='flat', bg='#f5b488', padx=10, command=Download).pack(
    side=tk.LEFT)
tk.Button(search_frame, text='全部', font=('黑体', 12), relief='flat', bg='#f5b488', padx=10, command=GetAll).pack(
    side=tk.LEFT, padx=5)

columns = ('Num', 'MusicId', 'MusicHash', 'SingerName', 'SongName',)
columns_value = ('序号', '音乐ID', 'Hash', '歌手', '歌曲名')
# 使用ttk创建一个树状图
tree_view = ttk.Treeview(root, height=18, show="headings", columns=columns)
# 设置列名
tree_view.column('Num', width=80, anchor='center')
tree_view.column('MusicId', width=80, anchor='center')
tree_view.column('MusicHash', width=80, anchor='center')
tree_view.column('SingerName', width=80, anchor='center')
tree_view.column('SongName', width=80, anchor='center')
# 给列名设置显示的名字
tree_view.heading('Num', text='序号')
tree_view.heading('MusicId', text='音乐ID')
tree_view.heading('MusicHash', text='Hash')
tree_view.heading('SingerName', text='歌手')
tree_view.heading('SongName', text='歌曲名')

tree_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
root.mainloop()
