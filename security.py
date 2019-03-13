from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import smtplib
import threading
import getpass
from email.mime.image import MIMEImage
occupy = None
skip = 0
lock = threading.Lock()
def ocu(vc, none):
	lock.acquire()

	msg = getmimeimage('有動靜', '監視器', '警察局', vc)
	smtp_gmail.sendmail(user, user, msg)
	lock.release()

def getmimeimage(sub, fr, to, img):
	img_encode = cv2.imencode('.jpg', img)[1]
	img_bytes = img_encode.tobytes()
	mime_img = MIMEImage(img_bytes)
	mime_img['Content-type'] = 'application/octet-stream'
	mime_img['Cotent-Disposition'] = 'attashment; filename=pic.jpg'
	mime_img['Subject'] = sub
	mime_img['From'] = fr
	mime_img['To'] = to
	return mime_img.as_string()
try:
	smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
except:
	print("連接失敗")
smtp_gmail.ehlo()
smtp_gmail.starttls()
usemail = input("Using gmail(Y/N): ")
if usemail == "Y":
	use = True
elif usemail == "N":
	use = False
else:
	use = True
if use:
	user = input("insert gmail username: ")
	pwd = getpass.getpass("insert password: ")
	smtp_gmail.login(user, pwd)

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
vs = VideoStream(src=0).start()
time.sleep(2.0)
cap = cv2.VideoCapture(0)

firstFrame = None

while True:
	frame = vs.read()
	succ, vc = cap.read()
	if frame is None:
		break
	frame = frame if args.get("video", None) is None else frame[1]
	text = "Unoccupied"

	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	if firstFrame is None:
		firstFrame = gray
		continue

	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 10, 255, cv2.THRESH_BINARY)[1]

	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	for c in cnts:
		if cv2.contourArea(c) < args["min_area"]:
			continue

		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"
		occupy = True
		if use:
			if occupy and skip == 0:
				threading.Thread(target=ocu, args=(vc, None)).start()
				skip = 200
			elif skip > 0:
				skip -= 1
				pass
		else:
			pass

	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	cv2.imshow("Security Feed", frame)
	key = cv2.waitKey(50) & 0xFF

	if key == ord("q"):
		break

vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()
