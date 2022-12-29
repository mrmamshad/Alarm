
import datetime
import winsound
def Alarm(Time):
    print("Alarm is running.....")
    AlarmTime = str(Time)

    while True :
        currentTime = datetime.datetime.now().strftime("%H:%M")
        if str(currentTime) == str(AlarmTime):
            duration = 1000  # milliseconds
            freq = 440  # Hz
            winsound.Beep(freq, duration)
            print("Time to wake up.....")
            

        elif str(currentTime) > str(AlarmTime):
            break
User_input_time = input("Enter your time: ")
Alarm(User_input_time)        