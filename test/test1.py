import time
import threading

def worker():
    print('I am a thread')
    t = threading.current_thread()
    print(t.getName())


new_t = threading.Thread(target=worker,name='my_thread')
new_t.start()

t = threading.current_thread()
print(t.getName())

