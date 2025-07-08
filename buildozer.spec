[app]
title = MyApp
package.name = myapp
package.domain = com.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,flask

orientation = portrait
fullscreen = 0

# Enable network (Flask) access
android.permissions = INTERNET
