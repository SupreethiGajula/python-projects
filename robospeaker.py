import os

if __name__ == "__main__":
    print("this robospeaker is created by supreethi")
    while True:
        x = input("enter what to speak: ")
        if x == 'q':
            break
        command = f"say {x}"#say is a command in macos system terminal used to speak something out
        os.system(command)