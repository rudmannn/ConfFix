import uiautomator2 as u2
import uiautomator2.exceptions
import subprocess


def fairemail__fragment_btnQuick(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(20)

    if d(resourceId="eu.faircode.email.debug:id/btnQuick").exists:
        print(d(resourceId="eu.faircode.email.debug:id/btnQuick").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/btnQuick").bounds()
        d(resourceId="eu.faircode.email.debug:id/btnQuick").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvPrivacy(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(20)

    if d(resourceId="eu.faircode.email.debug:id/tvPrivacy").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvPrivacy").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvPrivacy").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvPrivacy").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvSupport(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(15)

    if d(resourceId="eu.faircode.email.debug:id/tvSupport").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvSupport").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvSupport").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvSupport").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvTutorials(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(15)

    if d(resourceId="eu.faircode.email.debug:id/tvTutorials").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvTutorials").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvTutorials").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvTutorials").screenshot().save(imagePath)

    d.sleep(1)

    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvQuickNew(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(15)

    if d(resourceId="eu.faircode.email.debug:id/tvQuickNew").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvQuickNew").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvQuickNew").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvQuickNew").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvManual(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(2)

    if d(resourceId="eu.faircode.email.debug:id/tvManual").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvManual").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvManual").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvManual").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvFree(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")

    if d(resourceId="eu.faircode.email.debug:id/tvFree").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvFree").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvFree").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvFree").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvImportContacts(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")

    if d(resourceId="eu.faircode.email.debug:id/tvImportContacts").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvImportContacts").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvImportContacts").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvImportContacts").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvBatteryUsage(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(2)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")
    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")

    if d(resourceId="eu.faircode.email.debug:id/tvBatteryUsage").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvBatteryUsage").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvBatteryUsage").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvBatteryUsage").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvSyncStopped(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")
    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")

    if d(resourceId="eu.faircode.email.debug:id/tvSyncStopped").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvSyncStopped").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvSyncStopped").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvSyncStopped").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvPermissionsWhy(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")
    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")

    if d(resourceId="eu.faircode.email.debug:id/tvPermissionsWhy").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvPermissionsWhy").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvPermissionsWhy").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvPermissionsWhy").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvDozeWhy(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(2)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")
    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")

    if d(resourceId="eu.faircode.email.debug:id/tvDozeWhy").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvDozeWhy").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvDozeWhy").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvDozeWhy").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_setup_10(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(2)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")
    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")

    if d(resourceId="eu.faircode.email.debug:id/tvStamina").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvStamina").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvStamina").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvStamina").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvExchangeSupport(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")

    d.screen_on()
    if d(resourceId="eu.faircode.email.debug:id/tvExchangeSupport").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvExchangeSupport").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvExchangeSupport").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvExchangeSupport").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvIdentityWhat(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    d(resourceId="eu.faircode.email.debug:id/scroll").swipe("up")
    d.screen_on()
    if d(resourceId="eu.faircode.email.debug:id/tvIdentityWhat").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvIdentityWhat").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvIdentityWhat").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvIdentityWhat").screenshot().save(imagePath)

    d.sleep(1)
    d.app_stop(appId)
    return bounds

def easer__35bb624(deviceId, apkPath, imagePath):
    appId = 'ryey.easer'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d(resourceId="android:id/button1").click_exists(3)
    # d(resourceId="android:id/button1").click_exists(3)
    bounds = ()

    if d(resourceId="ryey.easer:id/running_ind_banner").exists(3):
        print(d(resourceId="ryey.easer:id/running_ind_banner").bounds())
        bounds = d(resourceId="ryey.easer:id/running_ind_banner").bounds()
        d(resourceId="ryey.easer:id/running_ind_banner").screenshot().save(imagePath)

    d.sleep(1)
    d.app_uninstall(appId)
    return bounds

def fenix__settings_https_only_1(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(12)

    p = subprocess.Popen(
        "adb -s " + deviceId + " shell input tap 1380 2820",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))

    d.sleep(8)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell input tap 700 2769",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))
    d.sleep(5)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell input tap 500 1300",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))
    d.sleep(5)

    if d(resourceId="org.mozilla.fenix.debug:id/https_only_summary").exists:
        print(d(resourceId="org.mozilla.fenix.debug:id/https_only_summary").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/https_only_summary").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/https_only_summary").bounds()

    d.sleep(3)
    return bounds

def fenix__settings_https_only_2(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d(resourceId="org.mozilla.fenix.debug:id/finish_button").click_exists(10)
    d(resourceId="org.mozilla.fenix.debug:id/menuButton").click_exists(10)
    d.xpath(
        '//*[@resource-id="org.mozilla.fenix.debug:id/mozac_browser_menu_recyclerView"]/android.widget.LinearLayout[8]').click_exists(
        10)

    d.sleep(2)
    if d(resourceId="org.mozilla.fenix.debug:id/recycler_view").exists:
        d(resourceId="org.mozilla.fenix.debug:id/recycler_view").swipe("up")

    d.sleep(2)
    d.xpath(
        '//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.widget.LinearLayout[10]').click_exists(10)

    if d(resourceId="org.mozilla.fenix.debug:id/https_only_title").exists:
        print(d(resourceId="org.mozilla.fenix.debug:id/https_only_title").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/https_only_title").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/https_only_title").bounds()

    d.sleep(1)
    d.app_uninstall(appId)
    return bounds

def fenix__custom_search_engine_1(deviceId, apkPath, imagePath):
    #TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d(resourceId="org.mozilla.fenix.debug:id/finish_button").click_exists(30)

    d(resourceId="org.mozilla.fenix.debug:id/toolbar_wrapper").click_exists(30)

    d(resourceId="org.mozilla.fenix.debug:id/search_engines_shortcut_button").click_exists(30)

    d(resourceId="org.mozilla.fenix.debug:id/awesome_bar").wait(30)
    d.xpath(
        '//*[@resource-id="org.mozilla.fenix.debug:id/awesome_bar"]/android.view.View[1]/android.view.View[1]/android.view.View[1]').swipe(
        "up")
    d.sleep(2)

    d(resourceId="org.mozilla.fenix.debug:id/awesome_bar").wait(30)
    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/awesome_bar"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[7]').click_exists(20)

    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.view.ViewGroup[1]').click_exists(20)

    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/search_engine_group"]/android.view.ViewGroup[1]').click_exists(20)

    if d(resourceId="org.mozilla.fenix.debug:id/search_add_custom_engine_search_string_example").exists:
        d(resourceId="org.mozilla.fenix.debug:id/search_add_custom_engine_search_string_example").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/search_add_custom_engine_search_string_example").bounds()
        print(bounds)

    d.sleep(8)
    d.app_uninstall(appId)
    return bounds

def fenix__toolbar_background(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(15)

    d(resourceId="org.mozilla.fenix.debug:id/finish_button").click_exists(20)

    d(resourceId="org.mozilla.fenix.debug:id/toolbar_wrapper").click_exists(20)

    d.sleep(3)
    d(resourceId="org.mozilla.fenix.debug:id/mozac_browser_toolbar_edit_url_view").wait(8)
    if d(resourceId="org.mozilla.fenix.debug:id/mozac_browser_toolbar_edit_url_view").exists:
        d(resourceId="org.mozilla.fenix.debug:id/mozac_browser_toolbar_edit_url_view").set_text("just a test")

    d.press('enter')
    d.sleep(2)
    if d(resourceId="org.mozilla.fenix.debug:id/toolbar").exists:
        bounds = d(resourceId="org.mozilla.fenix.debug:id/toolbar").bounds()
        print(d(resourceId="org.mozilla.fenix.debug:id/toolbar").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/toolbar").screenshot().save(imagePath)

    d.sleep(8)
    return bounds

def fenix__toolbar_background_top(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(5)

    d(resourceId="org.mozilla.fenix.debug:id/finish_button").click_exists(10)

    d(resourceId="org.mozilla.fenix.debug:id/menuButton").click_exists(10)

    d.xpath(
        '//*[@resource-id="org.mozilla.fenix.debug:id/mozac_browser_menu_recyclerView"]/android.widget.LinearLayout[8]').click_exists(10)

    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.widget.LinearLayout[4]').click_exists(
        10)

    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.view.ViewGroup[4]').click_exists(10)

    d.press("back")
    d.sleep(2)
    d.press("back")
    d.sleep(2)
    if d(resourceId="org.mozilla.fenix.debug:id/toolbarLayout").exists:
        print(d(resourceId="org.mozilla.fenix.debug:id/toolbarLayout").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/toolbarLayout").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/toolbarLayout").bounds()

    d.sleep(2)
    d.app_uninstall(appId)
    return bounds

def fenix__fragment_onboarding_home_dialog_1(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    bounds = ()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(10)

    if d(resourceId=appId + ":id/home_description").exists(10):
        print(d(resourceId=appId + ":id/home_description").bounds())
        d(resourceId=appId + ":id/home_description").screenshot().save(imagePath)
        bounds = d(resourceId=appId + ":id/home_description").bounds()

    d.sleep(1)
    return bounds

def fenix__fragment_onboarding_home_dialog_2(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    bounds = ()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(10)

    if d(resourceId=appId+":id/cleaner_tab_tray_description").exists(10):
        print(d(resourceId=appId+":id/cleaner_tab_tray_description").bounds())
        d(resourceId=appId + ":id/cleaner_tab_tray_description").screenshot().save(imagePath)
        bounds = d(resourceId=appId + ":id/cleaner_tab_tray_description").bounds()

    d.sleep(1)
    return bounds

def fenix__fragment_onboarding_home_dialog_3(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    bounds = ()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(10)

    if d(resourceId=appId+":id/useful_history_description").exists(10):
        print(d(resourceId=appId+":id/useful_history_description").bounds())
        d(resourceId=appId + ":id/useful_history_description").screenshot().save(imagePath)
        bounds = d(resourceId=appId + ":id/useful_history_description").bounds()
    d.sleep(1)
    return bounds

def fenix__fragment_onboarding_home_dialog_4(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    bounds = ()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(10)

    if d(resourceId=appId+":id/description").exists(10):
        print(d(resourceId=appId+":id/description").bounds())
        d(resourceId=appId + ":id/description").screenshot().save(imagePath)
        bounds = d(resourceId=appId + ":id/description").bounds()

    d.sleep(1)
    return bounds

def fenix__fragment_onboarding_home_dialog_5(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    bounds = ()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(10)

    if d(resourceId=appId+":id/home_title").exists(10):
        print(d(resourceId=appId+":id/home_title").bounds())
        d(resourceId=appId + ":id/home_title").screenshot().save(imagePath)
        bounds = d(resourceId=appId + ":id/home_title").bounds()

    d.sleep(1)
    return bounds

# def fenix__fragment_onboarding_home_dialog_6(deviceId, apkPath, imagePath):
#     appId = 'org.mozilla.fenix.debug'
#     print("begin executing test case")
#     d = u2.connect(deviceId)
#     d.screen_on()
#     bounds = ()
#     print("apkPath: " + str(apkPath))
#     d.app_install(apkPath)
#     d.app_start(appId)
#
#     if d(resourceId=appId+":id/welcome_title").exists(10):
#         print(d(resourceId=appId+":id/welcome_title").bounds())
#         d(resourceId=appId + ":id/welcome_title").screenshot().save(imagePath)
#         bounds = d(resourceId=appId + ":id/welcome_title").bounds()
#
#     d.sleep(1)
#     d.app_uninstall(appId)
#     return bounds
#
# def fenix__fragment_onboarding_home_dialog_7(deviceId, apkPath, imagePath):
#     appId = 'org.mozilla.fenix.debug'
#     print("begin executing test case")
#     d = u2.connect(deviceId)
#     d.screen_on()
#     bounds = ()
#     print("apkPath: " + str(apkPath))
#     d.app_install(apkPath)
#     d.app_start(appId)
#
#     if d(resourceId=appId+":id/cleaner_tab_tray_title").exists(10):
#         print(d(resourceId=appId+":id/cleaner_tab_tray_title").bounds())
#         d(resourceId=appId + ":id/cleaner_tab_tray_title").screenshot().save(imagePath)
#         bounds = d(resourceId=appId + ":id/cleaner_tab_tray_title").bounds()
#
#     d.sleep(1)
#     d.app_uninstall(appId)
#     return bounds

def proton_mail_mail_logo(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(5)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell pm grant ch.protonmail.android android.permission.POST_NOTIFICATIONS",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))
    d.sleep(3)

    if d(resourceId="ch.protonmail.android:id/mail_logo").exists(3):
        print(d(resourceId="ch.protonmail.android:id/mail_logo").bounds())
        d(resourceId="ch.protonmail.android:id/mail_logo").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonmail.android:id/mail_logo").bounds()

    d.sleep(2)
    return bounds

def proton_mail_drive_logo(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(5)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell pm grant ch.protonmail.android android.permission.POST_NOTIFICATIONS",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))
    d.sleep(3)

    if d(resourceId="ch.protonmail.android:id/drive_logo").exists(3):
        print(d(resourceId="ch.protonmail.android:id/drive_logo").bounds())
        d(resourceId="ch.protonmail.android:id/drive_logo").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonmail.android:id/drive_logo").bounds()

    d.sleep(2)
    return bounds

def proton_mail_calendar_logo(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(5)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell pm grant ch.protonmail.android android.permission.POST_NOTIFICATIONS",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))
    d.sleep(3)

    if d(resourceId="ch.protonmail.android:id/calendar_logo").exists(3):
        print(d(resourceId="ch.protonmail.android:id/calendar_logo").bounds())
        d(resourceId="ch.protonmail.android:id/calendar_logo").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonmail.android:id/calendar_logo").bounds()

    d.sleep(2)
    return bounds

def proton_mail_vpn_logo(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: "+str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(5)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell pm grant ch.protonmail.android android.permission.POST_NOTIFICATIONS",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))
    d.sleep(3)

    if d(resourceId="ch.protonmail.android:id/vpn_logo").exists(3):
        print(d(resourceId="ch.protonmail.android:id/vpn_logo").bounds())
        d(resourceId="ch.protonmail.android:id/vpn_logo").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonmail.android:id/vpn_logo").bounds()

    d.sleep(2)
    return bounds

def proton_mail_img_onboarding_encryption(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: "+str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(5)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(10)
    if d(resourceId="ch.protonmail.android:id/onboarding_image_view").exists(timeout=10):
        print(d(resourceId="ch.protonmail.android:id/onboarding_image_view").bounds())
        d(resourceId="ch.protonmail.android:id/onboarding_image_view").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonmail.android:id/onboarding_image_view").bounds()

    d.sleep(5)
    return bounds

def proton_mail_onboarding_logo_image_view(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: "+str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(5)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(10)

    # d(resourceId="ch.protonmail.android:id/onboarding_logo_image_view").wait(timeout=15)
    # print(d(resourceId="ch.protonmail.android:id/onboarding_logo_image_view").bounds())
    # d(resourceId="ch.protonmail.android:id/onboarding_logo_image_view").screenshot().save(imagePath)
    # bounds = d(resourceId="ch.protonmail.android:id/onboarding_logo_image_view").bounds()
    #
    d.sleep(5)
    return bounds

def proton_mail_contacts(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: "+str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)

    d.sleep(8)

    if d(resourceId="ch.protonmail.android:id/img_no_contacts").exists(10):
        print(d(resourceId="ch.protonmail.android:id/img_no_contacts").bounds())
        d(resourceId="ch.protonmail.android:id/img_no_contacts").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonmail.android:id/img_no_contacts").bounds()

    d.sleep(5)
    return bounds

def proton_mail_contacts_no_groups(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: "+str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)

    d.sleep(8)

    if d(resourceId="ch.protonmail.android:id/img_no_groups").exists(10):
        print(d(resourceId="ch.protonmail.android:id/img_no_groups").bounds())
        d(resourceId="ch.protonmail.android:id/img_no_groups").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonmail.android:id/img_no_groups").bounds()

    d.sleep(5)
    return bounds

def proton_mail_no_search(deviceId, apkPath, imagePath):
    appId = 'ch.protonmail.android'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: " + str(apkPath))
    d.app_uninstall(appId)
    d.app_install(apkPath)
    d.app_start(appId)

    d.sleep(15)

    if d(resourceId="ch.protonmail.android:id/img_empty_search").exists(10):
        print(d(resourceId="ch.protonmail.android:id/img_empty_search").bounds())
        d(resourceId="ch.protonmail.android:id/img_empty_search").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonmail.android:id/img_empty_search").bounds()

    d.sleep(5)

def fenix__ab6101b_welcom_icon(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(5)
    try:
        if d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Get the most out of Firefox Preview.").exists(15):
            print(d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Get the most out of Firefox Preview.").bounds())
            d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Get the most out of Firefox Preview.").screenshot().save(imagePath)
            bounds = d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Get the most out of Firefox Preview.").bounds()
    except uiautomator2.exceptions.UiObjectNotFoundError:
        pass
    d.sleep(5)
    return bounds

def fenix__ab6101b_protect(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(20)

    if d(resourceId="org.mozilla.fenix.debug:id/home_component").exists(15):
        d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
        d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
        d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
        d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Protect yourself").wait(15)
        print(d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Protect yourself").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Protect yourself").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Protect yourself").bounds()
    d.sleep(7)
    return bounds

def fenix__ab6101b_browse_privately(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(10)
    if d(resourceId="org.mozilla.fenix.debug:id/home_component").exists(15):
        d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
        d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
        d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
    if d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Browse privately").exists(15):
        print(d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Browse privately").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Browse privately").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Browse privately").bounds()
    d.sleep(5)
    return bounds

def fenix__ab6101b_your_privacy(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(10)
    # if d(resourceId="org.mozilla.fenix.debug:id/home_component").exists(20):
    #     d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
    #     d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
    #     d(resourceId="org.mozilla.fenix.debug:id/home_component").swipe("up")
    #     d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Your privacy").wait(10)
    # d.sleep(3)
    if d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Your privacy").exists(15):
        print(d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Your privacy").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Your privacy").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/header_text", text="Your privacy").bounds()

    return bounds

def fenix__7cea2ed(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(8)
    # d(resourceId="org.mozilla.fenix.debug:id/menuButton").click_exists(15)
    # d(resourceId="org.mozilla.fenix.debug:id/turn_on_sync_button").click_exists(15)
    # d(resourceId="org.mozilla.fenix.debug:id/sign_in_image").click_exists(13)

    # print(d(resourceId="org.mozilla.fenix.debug:id/sign_in_image").bounds())
    # d(resourceId="org.mozilla.fenix.debug:id/sign_in_image").screenshot().save(imagePath)
    # bounds = d(resourceId="org.mozilla.fenix.debug:id/sign_in_image").bounds()

    d.sleep(5)
    return bounds

def fenix__fragment_add_new_device(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(8)
    # d(resourceId="org.mozilla.fenix.debug:id/home_component").wait(3)
    # d(resourceId="org.mozilla.fenix.debug:id/turn_on_sync_button").wait(5)
    # d(resourceId="org.mozilla.fenix.debug:id/errorSummary").wait(3)
    if d(resourceId="org.mozilla.fenix.debug:id/errorSummary").exists(15):
        print(d(resourceId="org.mozilla.fenix.debug:id/errorSummary").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/errorSummary").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/errorSummary").bounds()

    d.sleep(5)
    return bounds

def fenix__7cea2ed_account_icon(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: "+str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d(resourceId="org.mozilla.fenix.debug:id/menuButton").click_exists(10)
    d.xpath(
        '//*[@resource-id="org.mozilla.fenix.debug:id/mozac_browser_menu_recyclerView"]/android.widget.LinearLayout[1]').click_exists(3)
    d(resourceId="org.mozilla.fenix.debug:id/imageView").wait(3)
    print(d(resourceId="org.mozilla.fenix.debug:id/imageView").bounds())
    d(resourceId="org.mozilla.fenix.debug:id/imageView").screenshot().save(imagePath)
    bounds = d(resourceId="org.mozilla.fenix.debug:id/imageView").bounds()

    return bounds

def neko__81418a7(deviceId, apkPath, imagePath):
    appId = 'eu.kanade.tachiyomi.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(5)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(10)

    try:
        d(resourceId="eu.kanade.tachiyomi.debug:id/page_seekbar").wait(10)
        print(d(resourceId="eu.kanade.tachiyomi.debug:id/page_seekbar").bounds())
        d(resourceId="eu.kanade.tachiyomi.debug:id/page_seekbar").screenshot().save(imagePath)
        bounds = d(resourceId="eu.kanade.tachiyomi.debug:id/page_seekbar").bounds()
    except uiautomator2.exceptions.UiObjectNotFoundError:
        print("failed on editing the XML elements, terminate")
        exit(0)

    return bounds

def fenix__140da0d_ic_etp_artwork(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d(resourceId="org.mozilla.fenix.debug:id/menuButton").click_exists(10)
    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/mozac_browser_menu_recyclerView"]/android.view.ViewGroup[1]').click_exists(10)
    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.widget.LinearLayout[10]').click_exists(10)
    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.view.ViewGroup[1]').wait(10)
    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.view.ViewGroup[1]').screenshot().save(imagePath)
    bounds = d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.view.ViewGroup[1]').bounds
    print(bounds)
    return bounds

def fenix__140da0d_ic_settings(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d(resourceId="org.mozilla.fenix.debug:id/toolbar_wrapper").click_exists(10)
    d(resourceId="org.mozilla.fenix.debug:id/mozac_browser_toolbar_edit_url_view").set_text("aaaa")
    d.press("enter")
    d(resourceId="org.mozilla.fenix.debug:id/mozac_browser_toolbar_tracking_protection_indicator").click_exists(10)
    d(resourceId="org.mozilla.fenix.debug:id/protection_settings").wait(10)
    d.sleep(2)
    d(resourceId="org.mozilla.fenix.debug:id/protection_settings").screenshot().save(imagePath)
    bounds = d(resourceId="org.mozilla.fenix.debug:id/protection_settings").bounds()
    print(bounds)
    return bounds

def fenix__1b96db9_mozac_ic_link(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    bounds = ()
    d.sleep(5)

    d(resourceId="org.mozilla.fenix.debug:id/menuButton").click_exists(10)
    d.xpath(
        '//*[@resource-id="org.mozilla.fenix.debug:id/mozac_browser_menu_recyclerView"]/android.view.ViewGroup[1]').click_exists(
        10)
    d(resourceId="org.mozilla.fenix.debug:id/recycler_view").wait(10)
    d(resourceId="org.mozilla.fenix.debug:id/recycler_view").swipe("up")
    d(resourceId="org.mozilla.fenix.debug:id/recycler_view").swipe("up")
    d.sleep(3)
    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.widget.LinearLayout[9]').click_exists(10)
    d(resourceId="org.mozilla.fenix.debug:id/add_on_item").click_exists(10)
    d.xpath('//android.widget.ScrollView').wait(10)
    d.xpath('//android.widget.ScrollView').swipe("up")
    d.sleep(6)
    try:
        d(resourceId="org.mozilla.fenix.debug:id/home_page_text").wait(15)
        d(resourceId="org.mozilla.fenix.debug:id/home_page_text").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/home_page_text").bounds()
        #
    except uiautomator2.exceptions.UiObjectNotFoundError:
        pass
    return bounds

def proton_vpn__activity_tv_login(deviceId, apkPath, imagePath):
    bounds = (0,0,0,0)
    appId = 'ch.protonvpn.android'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(5)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(10)

    d(resourceId="ch.protonvpn.android:id/logo").wait(10)
    if d(resourceId="ch.protonvpn.android:id/logo").exists:
        d(resourceId="ch.protonvpn.android:id/logo").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonvpn.android:id/logo").bounds()
        print(bounds)
    d.sleep(5)
    return bounds

def proton_vpn__dialog_tv_upgrade(deviceId, apkPath, imagePath):
    bounds = (0,0,0,0)
    appId = 'ch.protonvpn.android'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(5)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(10)
    d(resourceId="ch.protonvpn.android:id/logo").wait(10)
    if d(resourceId="ch.protonvpn.android:id/logo").exists:
        d(resourceId="ch.protonvpn.android:id/logo").screenshot().save(imagePath)
        bounds = d(resourceId="ch.protonvpn.android:id/logo").bounds()
        print(bounds)
    d.sleep(5)
    return bounds

def fenix__bdb2fa7_component_collection_creation(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)

    d(resourceId="org.mozilla.fenix.debug:id/toolbar").click_exists(15)
    if d(resourceId="org.mozilla.fenix.debug:id/mozac_browser_toolbar_edit_url_view").exists(10):
        d(resourceId="org.mozilla.fenix.debug:id/mozac_browser_toolbar_edit_url_view").set_text('test1')
        d.sleep(2)
    d.press("enter")
    d.sleep(3)
    d.press("back")
    d(resourceId="org.mozilla.fenix.debug:id/save_tab_group_button").click_exists(15)
    if d(resourceId="org.mozilla.fenix.debug:id/back_button").exists(15):
        d.sleep(8)
        d(resourceId="org.mozilla.fenix.debug:id/back_button").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/back_button").bounds()
        print(bounds)
    return bounds

def fenix__fragment_add_on_permissions(deviceId, apkPath, imagePath):
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)
    bounds = ()

    d.app_start(appId)
    d(resourceId="org.mozilla.fenix.debug:id/menuButton").click_exists(20)
    d.xpath(
        '//*[@resource-id="org.mozilla.fenix.debug:id/mozac_browser_menu_recyclerView"]/android.view.ViewGroup[1]').click_exists(
        20)
    d(resourceId="org.mozilla.fenix.debug:id/recycler_view").wait(20)
    d(resourceId="org.mozilla.fenix.debug:id/recycler_view").swipe("up")
    d(resourceId="org.mozilla.fenix.debug:id/recycler_view").swipe("up")
    d.sleep(12)
    # d(text="Add-ons").click_exists(10)
    d.xpath('//*[@resource-id="org.mozilla.fenix.debug:id/recycler_view"]/android.widget.LinearLayout[10]').click_exists(
        20)
    d(resourceId="org.mozilla.fenix.debug:id/add_button").click_exists(20)
    d(resourceId="org.mozilla.fenix.debug:id/allow_button").click_exists(20)
    d.sleep(8)
    d(resourceId="org.mozilla.fenix.debug:id/add_on_item").click_exists(20)
    d(resourceId="org.mozilla.fenix.debug:id/permissions").click_exists(20)
    if d(resourceId="org.mozilla.fenix.debug:id/learn_more_label").exists(12):
        d.sleep(6)
        d(resourceId="org.mozilla.fenix.debug:id/learn_more_label").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/learn_more_label").bounds()
        print(bounds)
    return bounds

def collect__item_view_option_paddingStart(deviceId, apkPath, imagePath):
    appId = 'org.odk.collect.android'
    bounds = ()
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(5)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(10)
    d.sleep(2)
    if d(resourceId="org.odk.collect.android:id/conffix_test", text="Save Changes").exists(5):
        d.sleep(10)
        d(resourceId="org.odk.collect.android:id/conffix_test", text="Save Changes").screenshot().save(imagePath)
        bounds = d(resourceId="org.odk.collect.android:id/conffix_test", text="Save Changes").bounds()
        print(bounds)
    return bounds

def cwa__fragment_submission_test_result_available(deviceId, apkPath, imagePath):
    appId = 'de.rki.coronawarnapp'
    bounds = ()
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    if d(resourceId="de.rki.coronawarnapp:id/submission_test_result_illustration_result_available").exists(10):
        d.sleep(6)
        d(resourceId="de.rki.coronawarnapp:id/submission_test_result_illustration_result_available").screenshot().save(imagePath)
        bounds = d(resourceId="de.rki.coronawarnapp:id/submission_test_result_illustration_result_available").bounds()
        print(bounds)
    return bounds

def cwa__home_fragment_layout(deviceId, apkPath, imagePath):
    appId = 'de.rki.coronawarnapp'
    bounds = ()
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    if d(resourceId="de.rki.coronawarnapp:id/main_header_logo").exists(10):
        d.sleep(8)
        d(resourceId="de.rki.coronawarnapp:id/main_header_logo").screenshot().save(
            imagePath)
        bounds = d(resourceId="de.rki.coronawarnapp:id/main_header_logo").bounds()
        print(bounds)
    return bounds

# def cwa__home_statistics_cards_keysubmissions_layout(deviceId, apkPath, imagePath):
#     appId = 'de.rki.coronawarnapp'
#     bounds = ()
#     print("begin executing test case")
#     d = u2.connect(deviceId)
#     d.screen_on()
#     d.app_uninstall(appId)
#     print("apkPath: " + str(apkPath))
#     d.app_install(apkPath)
#
#     d.app_start(appId)
#     d.sleep(5)
#     d(resourceId="de.rki.coronawarnapp:id/recycler_view").wait(10)
#     d(resourceId="de.rki.coronawarnapp:id/recycler_view").swipe("up")
#     d(resourceId="de.rki.coronawarnapp:id/recycler_view").swipe("up")
#     d.sleep(3)
#     d(resourceId="de.rki.coronawarnapp:id/statistics_recyclerview").swipe("left")
#     d(resourceId="de.rki.coronawarnapp:id/statistics_recyclerview").swipe("left")
#     d.sleep(8)
#     if d.xpath('//*[@resource-id="de.rki.coronawarnapp:id/keysubmissions_container"]/android.widget.ImageView[1]').exists:
#         d.sleep(7)
#         d.xpath('//*[@resource-id="de.rki.coronawarnapp:id/keysubmissions_container"]/android.widget.ImageView[1]').screenshot().save(
#             imagePath)
#         bounds = d.xpath('//*[@resource-id="de.rki.coronawarnapp:id/keysubmissions_container"]/android.widget.ImageView[1]').bounds
#         print(bounds)
#     return bounds

def cwa__tan_input_digit(deviceId, apkPath, imagePath):
    appId = 'de.rki.coronawarnapp'
    bounds = ()
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(3)
    d(resourceId="de.rki.coronawarnapp:id/submission_tan_input").wait(10)
    d.send_keys('3')
    d.sleep(12)

    return bounds

def cwa__tan_input_digit_error(deviceId, apkPath, imagePath):
    appId = 'de.rki.coronawarnapp'
    bounds = ()
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d(resourceId="de.rki.coronawarnapp:id/submission_tan_input").wait(10)
    d.send_keys('1')
    d.sleep(12)

    return bounds

def music_player_go__shuffle_option(deviceId, apkPath, imagePath):
    appId = 'com.iven.musicplayergo'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    bounds = ()
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)
    d(resourceId="com.iven.musicplayergo:id/dlg_one_button_btn_ok").click_exists(10)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(5)
    d.sleep(3)
    if d(resourceId="com.iven.musicplayergo:id/skip_prev_button").exists(5):
        d.sleep(6)
        d(resourceId="com.iven.musicplayergo:id/skip_prev_button").screenshot().save(imagePath)
        bounds = d(resourceId="com.iven.musicplayergo:id/skip_prev_button").bounds()
        # print(bounds)
    return bounds

def music_player_go__eq_option(deviceId, apkPath, imagePath):
    appId = 'com.iven.musicplayergo'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    bounds = ()
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)
    d(resourceId="com.iven.musicplayergo:id/dlg_one_button_btn_ok").click_exists(10)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(5)
    d.sleep(3)
    if d(resourceId="com.iven.musicplayergo:id/skip_prev_button").exists(5):
        d.sleep(6)
        d(resourceId="com.iven.musicplayergo:id/skip_prev_button").screenshot().save(imagePath)
        bounds = d(resourceId="com.iven.musicplayergo:id/skip_prev_button").bounds()
        # print(bounds)
    return bounds

def music_player_go__search_option(deviceId, apkPath, imagePath):
    appId = 'com.iven.musicplayergo'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    bounds = ()
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)
    d(resourceId="com.iven.musicplayergo:id/dlg_one_button_btn_ok").click_exists(10)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(5)
    d.sleep(3)
    if d(resourceId="com.iven.musicplayergo:id/skip_prev_button").exists(5):
        d.sleep(6)
        d(resourceId="com.iven.musicplayergo:id/skip_prev_button").screenshot().save(imagePath)
        bounds = d(resourceId="com.iven.musicplayergo:id/skip_prev_button").bounds()
        # print(bounds)
    return bounds

def music_player_go__invert_option(deviceId, apkPath, imagePath):
    appId = 'com.iven.musicplayergo'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    bounds = ()
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)
    d(resourceId="com.iven.musicplayergo:id/dlg_one_button_btn_ok").click_exists(10)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(5)
    d.sleep(3)
    if d(resourceId="com.iven.musicplayergo:id/skip_prev_button").exists(5):
        d.sleep(6)
        d(resourceId="com.iven.musicplayergo:id/skip_prev_button").screenshot().save(imagePath)
        bounds = d(resourceId="com.iven.musicplayergo:id/skip_prev_button").bounds()
        # print(bounds)
    return bounds

def music_player_go__skip_prev_button(deviceId, apkPath, imagePath):
    appId = 'com.iven.musicplayergo'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    bounds = ()
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)
    d(resourceId="com.iven.musicplayergo:id/dlg_one_button_btn_ok").click_exists(10)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(5)
    d.sleep(3)
    if d(resourceId="com.iven.musicplayergo:id/skip_prev_button").exists(5):
        d.sleep(6)
        d(resourceId="com.iven.musicplayergo:id/skip_prev_button").screenshot().save(imagePath)
        bounds = d(resourceId="com.iven.musicplayergo:id/skip_prev_button").bounds()
        print(bounds)
    return bounds

def music_player_go__play_pause_button(deviceId, apkPath, imagePath):
    appId = 'com.iven.musicplayergo'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    bounds = ()
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)
    d(resourceId="com.iven.musicplayergo:id/dlg_one_button_btn_ok").click_exists(10)
    d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(5)
    d.sleep(3)
    if d(resourceId="com.iven.musicplayergo:id/play_pause_button").exists(5):
        d.sleep(6)
        # d(resourceId="com.iven.musicplayergo:id/play_pause_button").screenshot().save(imagePath)
        bounds = d(resourceId="com.iven.musicplayergo:id/play_pause_button").bounds()
        print(bounds)
    d.sleep(6)
    return bounds

def music_player_go__skip_next_button(deviceId, apkPath, imagePath):
    appId = 'com.iven.musicplayergo'
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    bounds = ()
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)
    # d(resourceId="com.iven.musicplayergo:id/dlg_one_button_btn_ok").click_exists(10)
    # d(resourceId="com.android.permissioncontroller:id/permission_allow_button").click_exists(5)
    # d.sleep(3)
    if d(resourceId="com.iven.musicplayergo:id/skip_next_button").exists(5):
        d.sleep(6)
        d(resourceId="com.iven.musicplayergo:id/skip_next_button").screenshot().save(imagePath)
        bounds = d(resourceId="com.iven.musicplayergo:id/skip_next_button").bounds()
        print(bounds)
    return bounds

def fenix__tracking_protection_standard_option(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    bounds = ()
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(2)
    if d(resourceId="org.mozilla.fenix.debug:id/tracking_protection_standard_option").exists:
        print(d(resourceId="org.mozilla.fenix.debug:id/tracking_protection_standard_option").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/tracking_protection_standard_option").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/tracking_protection_standard_option").bounds()

    d.sleep(7)
    # d.app_uninstall(appId)
    return bounds

def fenix__tracking_protection_strict_default(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    d = u2.connect(deviceId)
    bounds = ()
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(2)
    if d(resourceId="org.mozilla.fenix.debug:id/tracking_protection_strict_default").exists:
        print(d(resourceId="org.mozilla.fenix.debug:id/tracking_protection_strict_default").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/tracking_protection_strict_default").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/tracking_protection_strict_default").bounds()

    d.sleep(7)
    # d.app_uninstall(appId)
    return bounds


def fenix__theme_light_radio_button(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(10)

    d.swipe(160,800,160,400)
    d.swipe(160, 800, 160, 400)
    if d(resourceId="org.mozilla.fenix.debug:id/theme_light_radio_button").exists:
        print(d(resourceId="org.mozilla.fenix.debug:id/theme_light_radio_button").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/theme_light_radio_button").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/theme_light_radio_button").bounds()

    d.sleep(7)
    # d.app_uninstall(appId)
    return bounds

def fenix__theme_dark_radio_button(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(10)
    d.swipe(160, 800, 160, 400)
    d.swipe(160, 800, 160, 400)

    if d(resourceId="org.mozilla.fenix.debug:id/theme_dark_radio_button").exists:
        print(d(resourceId="org.mozilla.fenix.debug:id/theme_dark_radio_button").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/theme_dark_radio_button").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/theme_dark_radio_button").bounds()

    d.sleep(7)
    # d.app_uninstall(appId)
    return bounds

def fenix__theme_automatic_radio_button(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(10)
    d.swipe(160, 800, 160, 400)
    d.swipe(160, 800, 160, 400)


    if d(resourceId="org.mozilla.fenix.debug:id/theme_automatic_radio_button").exists:
        print(d(resourceId="org.mozilla.fenix.debug:id/theme_automatic_radio_button").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/theme_automatic_radio_button").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/theme_automatic_radio_button").bounds()

    d.sleep(7)
    # d.app_uninstall(appId)
    return bounds

def fenix__toolbar_top_radio_button(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(10)
    # d.swipe(160, 800, 160, 400)
    # d.swipe(160, 800, 160, 400)
    # d.swipe(160, 800, 160, 400)
    # d.sleep(5)

    if d(resourceId="org.mozilla.fenix.debug:id/toolbar_top_radio_button").exists(20):
        print(d(resourceId="org.mozilla.fenix.debug:id/toolbar_top_radio_button").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/toolbar_top_radio_button").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/toolbar_top_radio_button").bounds()

    d.sleep(7)
    # d.app_uninstall(appId)
    return bounds

def fenix__toolbar_bottom_radio_button(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT!!] make sure the font size has been set to be large. Otherwise the bug cannot be reproduced
    appId = 'org.mozilla.fenix.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(10)
    # d.swipe(160, 800, 160, 400)
    # d.swipe(160, 800, 160, 400)
    # d.swipe(160, 800, 160, 400)
    # d.sleep(5)

    if d(resourceId="org.mozilla.fenix.debug:id/toolbar_bottom_radio_button").exists(20):
        print(d(resourceId="org.mozilla.fenix.debug:id/toolbar_bottom_radio_button").bounds())
        d(resourceId="org.mozilla.fenix.debug:id/toolbar_bottom_radio_button").screenshot().save(imagePath)
        bounds = d(resourceId="org.mozilla.fenix.debug:id/toolbar_bottom_radio_button").bounds()

    d.sleep(7)

    # d.app_uninstall(appId)
    return bounds


def buran(deviceId, apkPath, imagePath):
    appId = 'corewala.gemini.buran'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)

    d.sleep(5)

    if d(resourceId="corewala.gemini.buran:id/gemtext_text_textview").exists:
        print(d(resourceId="corewala.gemini.buran:id/gemtext_text_textview").bounds())
        # d(resourceId="corewala.gemini.buran:id/gemtext_text_textview").screenshot().save(imagePath)
        bounds = d(resourceId="corewala.gemini.buran:id/gemtext_text_textview").bounds()

    d.sleep(5)
    # d.sleep(7)
    # d.app_uninstall(appId)
    return bounds


def libre(deviceId, apkPath, imagePath):
    appId = 'com.github.libretube.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(5)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell pm grant com.github.libretube.debug android.permission.POST_NOTIFICATIONS",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))

    d.sleep(8)

    p = subprocess.Popen(
        "adb -s " + deviceId + " shell input tap 1210 820",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))

    d.sleep(8)

    if d(resourceId="com.github.libretube.debug:id/conffix_test").exists(timeout=10):
        print("bounds:::"+str(d(resourceId="com.github.libretube.debug:id/conffix_test").bounds()))
        bounds = d(resourceId="com.github.libretube.debug:id/conffix_test").bounds()

    d.sleep(5)
    # d.sleep(7)
    return bounds


def airmessage(deviceId, apkPath, imagePath):
    appId = 'me.tagavari.airmessage.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)

    d.app_start(appId)
    d.sleep(8)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell pm grant me.zhanghai.android.files android.permission.POST_NOTIFICATIONS",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))
    # if d(text='Use manual configuration').exists(timeout=10):
    #     d(text='Use manual configuration').click()

    d.sleep(6)

    if d(resourceId="me.tagavari.airmessage.debug:id/conffix_test").exists(timeout=10):
        print("bounds:::"+str(d(resourceId="me.tagavari.airmessage.debug:id/conffix_test").bounds()))
        bounds = d(resourceId="me.tagavari.airmessage.debug:id/conffix_test").bounds()

    return bounds


def MaterialFiles(deviceId, apkPath, imagePath):
    appId = 'me.zhanghai.android.files'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(appId)
    print("apkPath: " + str(apkPath))
    d.app_install(apkPath)
    d.app_start(appId)
    d.screen_on()
    d.sleep(8)
    p = subprocess.Popen("adb -s "+deviceId+" shell pm grant me.zhanghai.android.files android.permission.POST_NOTIFICATIONS", shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))

    d.sleep(6)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell input tap 1210 820",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))

    d.sleep(6)
    p = subprocess.Popen(
        "adb -s " + deviceId + " shell input tap 1300 600",
        shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))

    if d(resourceId="me.zhanghai.android.files:id/conffix_test").exists(timeout=5):
        print("bounds:::" + str(d(resourceId="me.zhanghai.android.files:id/conffix_test").bounds()))
        bounds = d(resourceId="me.zhanghai.android.files:id/conffix_test").bounds()

    return bounds


def fairemail__fragment_tvLanguageToolPrivacy(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvLanguageToolPrivacy").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvLanguageToolPrivacy").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvLanguageToolPrivacy").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvLanguageToolPrivacy").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvDeepLPrivacy(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvDeepLPrivacy").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvDeepLPrivacy").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvDeepLPrivacy").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvDeepLPrivacy").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvVirusTotalPrivacy(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvVirusTotalPrivacy").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvVirusTotalPrivacy").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvVirusTotalPrivacy").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvVirusTotalPrivacy").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvSdcard(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvSdcard").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvSdcard").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvSdcard").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvSdcard").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvCaptionAdvanced(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvCaptionAdvanced").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvCaptionAdvanced").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvCaptionAdvanced").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvCaptionAdvanced").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvExperimentsHint(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvExperimentsHint").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvExperimentsHint").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvExperimentsHint").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvExperimentsHint").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvCaptionDebug(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvCaptionDebug").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvCaptionDebug").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvCaptionDebug").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvCaptionDebug").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvBimiHint(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvBimiHint").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvBimiHint").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvBimiHint").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvBimiHint").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvBimiVerified(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvBimiVerified").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvBimiVerified").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvBimiVerified").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvBimiVerified").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvGravatarPrivacy(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvGravatarPrivacy").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvGravatarPrivacy").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvGravatarPrivacy").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvGravatarPrivacy").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvLibravatarPrivacy(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvLibravatarPrivacy").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvLibravatarPrivacy").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvLibravatarPrivacy").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvLibravatarPrivacy").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvFaviconsHint(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvFaviconsHint").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvFaviconsHint").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvFaviconsHint").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvFaviconsHint").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvAdvanced(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvAdvanced").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvAdvanced").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvAdvanced").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvAdvanced").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_swAuthentication(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/swAuthentication").exists:
        print(d(resourceId="eu.faircode.email.debug:id/swAuthentication").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/swAuthentication").bounds()
        d(resourceId="eu.faircode.email.debug:id/swAuthentication").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvAuthSome(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvAuthSome").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvAuthSome").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvAuthSome").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvAuthSome").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvAuthAll(deviceId, apkPath, imagePath):
    # TODO [IMPORTANT] use local android emulator instead, make it run first
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvAuthAll").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvAuthAll").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvAuthAll").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvAuthAll").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds


def fairemail__fragment_tvCaptionDebug_encry(deviceId, apkPath, imagePath):
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvCaptionDebug").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvCaptionDebug").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvCaptionDebug").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvCaptionDebug").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds


def fairemail__fragment_swExternalStorage(deviceId, apkPath, imagePath):
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/swExternalStorage").exists:
        print(d(resourceId="eu.faircode.email.debug:id/swExternalStorage").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/swExternalStorage").bounds()
        d(resourceId="eu.faircode.email.debug:id/swExternalStorage").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def fairemail__fragment_tvBimiUnverified(deviceId, apkPath, imagePath):
    appId = 'eu.faircode.email.debug'
    print("begin executing test case")
    bounds = ()
    d = u2.connect(deviceId)
    # d.app_uninstall(appId)
    d.screen_on()
    # d.app_install(apkPath)
    d.app_start(appId)
    d.sleep(8)

    if d(resourceId="eu.faircode.email.debug:id/tvBimiUnverified").exists:
        print(d(resourceId="eu.faircode.email.debug:id/tvBimiUnverified").bounds())
        bounds = d(resourceId="eu.faircode.email.debug:id/tvBimiUnverified").bounds()
        d(resourceId="eu.faircode.email.debug:id/tvBimiUnverified").screenshot().save(imagePath)

    d.sleep(3)
    d.app_stop(appId)
    return bounds

def test_case_driver(test_case_name,deviceId, apkPath, imagePath='./tmps/repair.png'):
    if test_case_name == 'proton_mail_calendar_logo':  #finish
        return proton_mail_calendar_logo(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_mail_drive_logo': #finish
        return proton_mail_drive_logo(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_mail_contacts':  #finish
        return proton_mail_contacts(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_mail_contacts_no_groups':
        return proton_mail_contacts_no_groups(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_mail_no_search':
        return proton_mail_no_search(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_mail_mail_logo':  #finish
        return proton_mail_mail_logo(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_mail_vpn_logo':  #finish
        return proton_mail_vpn_logo(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_mail_img_onboarding_encryption':  #finish
        return proton_mail_img_onboarding_encryption(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_mail_onboarding_logo_image_view':  #finish
        return proton_mail_onboarding_logo_image_view(deviceId, apkPath, imagePath)
    elif test_case_name == 'neko__81418a7':
        return neko__81418a7(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_vpn__activity_tv_login': #finish
        return proton_vpn__activity_tv_login(deviceId, apkPath, imagePath)
    elif test_case_name == 'proton_vpn__dialog_tv_upgrade': #finish
        return proton_vpn__dialog_tv_upgrade(deviceId, apkPath, imagePath)
    elif test_case_name == 'cwa__fragment_submission_test_result_available': #finish
        return cwa__fragment_submission_test_result_available(deviceId, apkPath, imagePath)
    elif test_case_name == 'cwa__home_fragment_layout': #finish
        return cwa__home_fragment_layout(deviceId, apkPath, imagePath)
    elif test_case_name == 'cwa__tan_input_digit': #finish
        return cwa__tan_input_digit(deviceId, apkPath, imagePath)
    elif test_case_name == 'cwa__tan_input_digit_error': #finish
        return cwa__tan_input_digit_error(deviceId, apkPath, imagePath)
    elif test_case_name == 'music_player_go__shuffle_option': #finish
        return music_player_go__shuffle_option(deviceId, apkPath, imagePath)
    elif test_case_name == 'music_player_go__search_option': #finish
        return music_player_go__search_option(deviceId, apkPath, imagePath)
    elif test_case_name == 'music_player_go__invert_option': #finish
        return music_player_go__invert_option(deviceId, apkPath, imagePath)
    elif test_case_name == 'music_player_go__eq_option': #finish
        return music_player_go__eq_option(deviceId, apkPath, imagePath)
    elif test_case_name == 'music_player_go__skip_prev_button': #finish
        return music_player_go__skip_prev_button(deviceId, apkPath, imagePath)
    elif test_case_name == 'music_player_go__play_pause_button': #finish
        return music_player_go__play_pause_button(deviceId, apkPath, imagePath)
    elif test_case_name == 'music_player_go__skip_next_button': #finish
        return music_player_go__skip_next_button(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__ab6101b_welcom_icon': #finish
        return fenix__ab6101b_welcom_icon(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__ab6101b_protect': #finish
        return fenix__ab6101b_protect(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__ab6101b_browse_privately': #finish
        return fenix__ab6101b_browse_privately(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__ab6101b_your_privacy': #finish
        return fenix__ab6101b_your_privacy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__7cea2ed': # finish (fragment_turn_on_sync)
        return fenix__7cea2ed(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__140da0d_ic_settings': #finish
        return fenix__140da0d_ic_settings(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__1b96db9_mozac_ic_link': #finish (fragment_add_on_details)
        return fenix__1b96db9_mozac_ic_link(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__fragment_add_new_device': #finish (false)
        return fenix__fragment_add_new_device(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__7cea2ed_account_icon': # fail because of preference
        return fenix__7cea2ed_account_icon(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__140da0d_ic_etp_artwork': #fail because of preference
        return fenix__140da0d_ic_etp_artwork(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__tracking_protection_standard_option':
        return fenix__tracking_protection_standard_option(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__tracking_protection_strict_default':
        return fenix__tracking_protection_strict_default(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__theme_light_radio_button':
        return fenix__theme_light_radio_button(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__theme_dark_radio_button':
        return fenix__theme_dark_radio_button(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__theme_automatic_radio_button':
        return fenix__theme_automatic_radio_button(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__fragment_onboarding_home_dialog_1':
        return fenix__fragment_onboarding_home_dialog_1(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__fragment_onboarding_home_dialog_2':
        return fenix__fragment_onboarding_home_dialog_2(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__fragment_onboarding_home_dialog_3':
        return fenix__fragment_onboarding_home_dialog_3(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__fragment_onboarding_home_dialog_4':
        return fenix__fragment_onboarding_home_dialog_4(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__fragment_onboarding_home_dialog_5':
        return fenix__fragment_onboarding_home_dialog_5(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__toolbar_bottom_radio_button':
        return fenix__toolbar_bottom_radio_button(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__toolbar_top_radio_button':
        return fenix__toolbar_top_radio_button(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__bdb2fa7_component_collection_creation':
        return fenix__bdb2fa7_component_collection_creation(deviceId, apkPath, imagePath)
    elif test_case_name == 'fenix__settings_https_only_1':
        return fenix__settings_https_only_1(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_btnQuick':
        return fairemail__fragment_btnQuick(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvPrivacy':
        return fairemail__fragment_tvPrivacy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvSupport':
        return fairemail__fragment_tvSupport(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvTutorials':
        return fairemail__fragment_tvTutorials(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvQuickNew':
        return fairemail__fragment_tvQuickNew(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvImportContacts':
        return fairemail__fragment_tvImportContacts(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvFree':
        return fairemail__fragment_tvFree(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvBatteryUsage':
        return fairemail__fragment_tvBatteryUsage(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvSyncStopped':
        return fairemail__fragment_tvSyncStopped(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvDozeWhy':
        return fairemail__fragment_tvDozeWhy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvPermissionsWhy':
        return fairemail__fragment_tvPermissionsWhy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvIdentityWhat':
        return fairemail__fragment_tvIdentityWhat(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvExchangeSupport':
        return fairemail__fragment_tvExchangeSupport(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvLanguageToolPrivacy':
        return fairemail__fragment_tvLanguageToolPrivacy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvDeepLPrivacy':
        return fairemail__fragment_tvDeepLPrivacy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvVirusTotalPrivacy':
        return fairemail__fragment_tvVirusTotalPrivacy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvSdcard':
        return fairemail__fragment_tvSdcard(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvCaptionAdvanced':
        return fairemail__fragment_tvCaptionAdvanced(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvExperimentsHint':
        return fairemail__fragment_tvExperimentsHint(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvCaptionDebug':
        return fairemail__fragment_tvCaptionDebug(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvCaptionDebug_encry':
        return fairemail__fragment_tvCaptionDebug_encry(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvBimiHint':
        return fairemail__fragment_tvBimiHint(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvBimiVerified':
        return fairemail__fragment_tvBimiVerified(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvBimiUnverified':
        return fairemail__fragment_tvBimiUnverified(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvGravatarPrivacy':
        return fairemail__fragment_tvGravatarPrivacy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvLibravatarPrivacy':
        return fairemail__fragment_tvLibravatarPrivacy(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvFaviconsHint':
        return fairemail__fragment_tvFaviconsHint(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvAdvanced':
        return fairemail__fragment_tvAdvanced(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_swAuthentication':
        return fairemail__fragment_swAuthentication(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvAuthSome':
        return fairemail__fragment_tvAuthSome(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_tvAuthAll':
        return fairemail__fragment_tvAuthAll(deviceId, apkPath, imagePath)
    elif test_case_name == 'fairemail__fragment_swExternalStorage':
        return fairemail__fragment_swExternalStorage(deviceId, apkPath, imagePath)
    elif test_case_name == 'buran':
        return buran(deviceId, apkPath, imagePath)
    elif test_case_name == 'libre':
        return libre(deviceId, apkPath, imagePath)
    elif test_case_name == 'airmessage':
        return airmessage(deviceId, apkPath, imagePath)
    elif test_case_name == 'MaterialFiles':
        return MaterialFiles(deviceId, apkPath, imagePath)


if __name__ == '__main__':
    deviceId = 'emulator-5562'
    apkPath = './subject_apks/fenix-toolbar_background.apk'
    imagePath = './repair.png'
    fenix__toolbar_background(deviceId, apkPath, imagePath)