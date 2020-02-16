from win10toast import ToastNotifier
import time

while True:
 	current_time=time.strftime("%H:%M:%S")
 	if current_time=="09:43:00":
 		break
 	else:
 		pass




hr=ToastNotifier()
hr.show_toast("REMINDER","hello")