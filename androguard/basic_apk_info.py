from androguard.misc import AnalyzeAPK



a, d, dx = AnalyzeAPK('Virus0e69af88dcbb469e30f16609b10c926c.apk')


app_name = a.get_app_name()
pkg = a.get_package()
aversion = a.get_androidversion_code()

print(app_name)
print(pkg)
print(aversion)


'''
Certificado
com.security.service
1
'''
