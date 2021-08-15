import datetime
import time

def format_message(message):
    author = "python.direct"
    def message_with_date(text):
        nonlocal author
        author = "learningthoughts"
        return f"{datetime.datetime.now()} {text} {author}"
    return message_with_date(message)


if __name__ == "__main__":
    print(format_message("Started application"))
    time.sleep(1)
    print(format_message("Stopped application"))