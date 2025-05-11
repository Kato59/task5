import time

def consume_with_timeout(iterator, timeout_seconds):
    start_time = time.time()
    for value in iterator:
        current_time = time.time()
        if current_time - start_time > timeout_seconds:
            print("Таймаут завершено.")
            break
        print("Отримано значення:", value)
        time.sleep(0.5)  # штучна пауза, щоб бачити процес
