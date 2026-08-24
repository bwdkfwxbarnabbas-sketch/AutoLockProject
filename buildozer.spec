[app]

# Application title
title = AutoLockProject

# Package name and domain
package.name = autolockproject
package.domain = org.test

# Source code location
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,xml

# Application version
version = 0.1

# Core application requirements
requirements = python3,kivy

# Orientation and display
orientation = portrait
fullscreen = 0

#
# Android configuration
#

# Target API and Minimum API
android.api = 33
android.minapi = 24

# Pinned NDK and Build Tools versions for compatibility
android.ndk = 25b
android.build_tools_version = 33.0.2

# License acceptance
android.accept_sdk_license = True

# Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# AndroidX support
android.enable_androidx = True

[buildozer]

# Verbose logging output
log_level = 2

# Disable root warning prompt
warn_on_root = 0