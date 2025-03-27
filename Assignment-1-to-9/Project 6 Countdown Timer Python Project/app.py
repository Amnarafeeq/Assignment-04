import time

def count_down():
    print("*" * 50,"\n")
    print("\tWelcome to the Countdown Timer!")
    print("\n","*" * 50,"\n")
    seconds = int(input("⏱ Enter the number of seconds: "))
    print("\n⏳ Countdown Timer Started! 🎉\n")

    for x in range(seconds, 0, -1):
        sec = x % 60
        mins = (x // 60) % 60
        hours = x // 3600
        print(f"⏰ Time Left: {hours:02}:{mins:02}:{sec:02} ⏳")
        time.sleep(1)

    print("\n🚀 Time's up! 🎉🎊\n")

count_down()