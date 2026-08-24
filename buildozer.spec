[app]
title = Python Auto Lock
package.name = autolock
package.domain = org.pyautolock

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml

version = 0.1
requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = USES_POLICY_FORCE_LOCK
android.add_xml_to_manifest = res/xml/device_admin.xml

[buildozer]
log_level = 2
warn_on_root = 1