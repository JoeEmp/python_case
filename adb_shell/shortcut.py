import os


def get_activity_app_apk(target_name='', pkg_name=''):
    """ 
    获取当前app安装包
    adb shell dumpsys window | grep mCurrentFocus
    adb shell pm path com.v2ray.ang
    adb  pull mobile path local path
    """
    if not pkg_name:
        # debug
        # r = '  mCurrentFocus=Window{5f1166b u0 com.google.android.apps.authenticator2/com.google.android.apps.authenticator.AuthenticatorActivity}'
        r = os.popen('adb shell dumpsys window | grep mCurrentFocus').read()
        pkg_name = r.split(' ')[-1].split('/')[0]
    # debug
    # ret = 'package:/data/app/com.v2ray.ang-dsHyxvci2OWiZsb-FrirDA==/base.apk' + os.linesep
    print('adb shell pm path %s' % pkg_name)
    ret = os.popen('adb shell pm path %s' % pkg_name).read()
    pkg_path = ret.split(':')[1].strip(os.linesep)
    if not target_name:
        target_name = pkg_name + '.apk'
    print("adb pull %s %s" % (pkg_path, target_name))
    os.popen("adb pull %s %s" % (pkg_path, target_name))


if __name__ == "__main__":
    get_activity_app_apk()
