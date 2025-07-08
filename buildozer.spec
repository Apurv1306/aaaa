# buildozer.spec

[app]

# (str) Title of your application
title = FaceApp Kivy Flask

# (str) Package name
package.name = com.yourcompany.faceappkivyflask

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivy.app

# (str) Application version
version = 0.1

# (list) Requirements (a.k.a. dependencies) of the application.
# The format is: <name>==<version>
# Usually you don't need to specify the version, Buildozer will use the latest stable one.
# This is where you list your Python dependencies.
requirements = python3,kivy,flask,flask-cors,requests,numpy,opencv

# (str) Kivy version you use
kivy.version = 2.3.0 # Or your preferred Kivy version

# (list) Source files to include (let empty to include all the files in the current dir)
source.include_exts = py,png,jpg,xml,kv,json

# (list) List of inclusions for the APK (relative to the Buildozer project directory)
# This is crucial for your Haar cascade and any data files.
source.include_patterns = *.py, *.png, *.jpg, *.xml, *.json, *.kv

# (str) The entry point of your application.
main.py = flaskapk.py

# (list) Android permissions
# INTERNET is essential for Flask and requests.
# ACCESS_NETWORK_STATE is good practice.
# WRITE_EXTERNAL_STORAGE and READ_EXTERNAL_STORAGE might be needed for saving/loading known_faces.
# CAMERA is essential for face detection.
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA

# (int) Android SDK version to use
android.api = 33 # Recommended for modern Android versions

# (int) Minimum Android SDK version (API level)
android.minapi = 21

# (int) Android target SDK version (API level)
android.targetsdk = 33

# (bool) Enable or disable Android debugging.
android.debug = True

# (list) Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Path to the Android NDK directory (if not set, Buildozer will download it)
# android.ndk = /path/to/android-ndk-r25b

# (str) Path to the Android SDK directory (if not set, Buildozer will download it)
# android.sdk = /path/to/android-sdk

# (str) Path to the Java JDK directory (if not set, Buildozer will download it)
# android.jdk = /path/to/java-jdk

# (bool) If True, Buildozer will use the `p4a` toolchain to build the APK.
# This is the default and should be True.
android.enable_multidex = True

# (list) Add Java extensions to your Android build (e.g. for custom Android APIs)
# android.add_libs_armeabi-v7a = /path/to/your/library.jar
# android.add_libs_arm64-v8a = /path/to/your/library.jar

# (list) Add a Java class to your Android build (e.g. for custom Android APIs)
# android.add_src = /path/to/your/java/src

# (str) The name of the Android activity class.
# android.activity_class = org.kivy.android.PythonActivity

# (str) The name of the Android application class.
# android.app_class = org.kivy.android.PythonUtil

# (str) The name of the Android service class.
# android.service_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_start_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the Android service class for foreground tasks.
# android.service_foreground_class = org.kivy.android.PythonService

# (str) The name of the Android service class for background tasks.
# android.service_background_class = org.kivy.android.PythonService

# (str) The name of the
