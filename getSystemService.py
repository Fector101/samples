"""How to get getSystemService in service file"""
# https://github.com/Fector101/android_notify/blob/main/android_notify/config.py#L122

from jnius import cast, autoclass
from android_notify.config import get_python_activity_context
NotificationManager = autoclass('android.app.NotificationManager')

PythonActivity = autoclass('org.kivy.android.PythonService')
service = PythonActivity.mService
context = service.getApplication().getApplicationContext()
notification_service = context.getSystemService(context.NOTIFICATION_SERVICE)
notification_manager = cast(NotificationManager, notification_service)


# OR ----------------
 # Using `get_python_activity_context` This way it will always import the right activity context whether from service or app UI

context=get_python_activity_context()
notification_service = context.getSystemService(context.NOTIFICATION_SERVICE)
notification_manager = cast(NotificationManager, notification_service)

