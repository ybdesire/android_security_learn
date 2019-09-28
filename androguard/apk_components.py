from androguard.misc import AnalyzeAPK



a, d, dx = AnalyzeAPK('Virus0e69af88dcbb469e30f16609b10c926c.apk')

activity = a.get_activities()
service = a.get_services()
provider = a.get_providers()
receiver = a.get_receivers()
permission = a.get_permissions()



print(activity)
print(service)
print(provider)
print(receiver)
print(permission)


'''
['com.security.service.MainActivity']
[]
[]
['com.security.service.receiver.ActionReceiver', 'com.security.service.receiver.SmsReceiver', 'com.security.service.receiver.RebootReceiver']
['android.permission.RECEIVE_SMS', 'android.permission.SEND_SMS']
'''
