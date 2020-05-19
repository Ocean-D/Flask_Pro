import threading,time

def worker():
    time.sleep(5)
    print("i am threading")
    t = threading.current_thread()
    print(t.getName())

new_t = threading.Thread(target=worker,name='Ocean_thread')#实例化一个对像
new_t.start()

t = threading.current_thread()
print(t.getName())




