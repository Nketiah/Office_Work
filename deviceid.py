import win32com.client

qng = win32com.client.Dispatch("QWQNG.QNG")
deviceId = qng.DeviceId
print(deviceId)