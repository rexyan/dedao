import _thread
import os

a = []
with open("down.txt", "r", encoding="utf-8") as b:
    for x in b.readlines():
        a.append(x.split("|")[2].strip())
    print(",".join(a))


def down_book(name):
    while a:
        print(f"{name}, 任务开始")
        book_id = a.pop()
        os.system(f"D:\soft\dedao\dedao-windows-amd64.exe dlo {book_id}")
        print(f"{name}, 下载完成 {book_id}, 剩余数量: {len(a)}")


_thread.start_new_thread(down_book, ("线程-1",))
_thread.start_new_thread(down_book, ("线程-2",))
_thread.start_new_thread(down_book, ("线程-3",))
_thread.start_new_thread(down_book, ("线程-4",))
_thread.start_new_thread(down_book, ("线程-5",))
_thread.start_new_thread(down_book, ("线程-6",))

while 1:
    pass
