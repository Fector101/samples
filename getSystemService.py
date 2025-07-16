"""How to get getSystemService in service file"""

from jnius import cast, autoclass
from android_notify.config import get_python_activity_context

 # Using `get_python_activity_context` This way it will always import the right activity context whether from service or app UI

context=get_python_activity_context()
notification_service = context.getSystemService(context.NOTIFICATION_SERVICE)
notification_manager = cast(NotificationManager, notification_service)

OR ----------

PythonActivity = autoclass('org.kivy.android.PythonService')
service = PythonActivity.mService
context = service.getApplication().getApplicationContext()
    
def get_notification_manager():
    notification_service = context.getSystemService(context.NOTIFICATION_SERVICE)
    return cast(NotificationManager, notification_service)

# https://github.com/Fector101/android_notify/blob/main/android_notify/config.py#L122
