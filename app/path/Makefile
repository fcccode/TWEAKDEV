export THEOS_DEVICE_IP=10.57.2.66
include $(THEOS)/makefiles/common.mk

APPLICATION_NAME = path
path_FILES = main.m aabbAppDelegate.m aabbRootViewController.m
path_FRAMEWORKS = UIKit CoreGraphics

include $(THEOS_MAKE_PATH)/application.mk

after-install::
	install.exec "killall \"path\"" || true
