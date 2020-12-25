from datetime import datetime
import timeago

time = datetime.strptime('2020-12-24 10:59:35.554133', '%Y-%m-%d %H:%M:%S.%f')
print (timeago.format(datetime.utcnow(), time))
