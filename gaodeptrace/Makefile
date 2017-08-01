export THEOS_DEVICE_IP = 192.168.1.105
include $(THEOS)/makefiles/common.mk

TWEAK_NAME = gaodeptrace
gaodeptrace_FILES = Tweak.xm
ARCHS = arm64



include $(THEOS_MAKE_PATH)/tweak.mk

after-install::
	install.exec "killall -9 AMapiPhone"
