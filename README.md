# mob-framework-radar

**Mob**ile **Framework Radar** is a tool that allows you to easily detect the cross-platform framework of the mobile application it takes in input. Furthermore, it detects if the app contains some security libraries (e.g. RootBeer, IOSSecuritySuite, etc.)

## Overview

Nowadays, with the increase of cross-platform and hybrid apps, it becomes important to be able to identify the development framework of a mobile application during a security analysis because once you have identified the development framework, you can focus on the analysis of specific files or platform-specific vulnerabilities based on the framework that has been identified.
Therefore, this tool can be useful during the initial reverse engineering phase of the app to quickly recognize the cross-platform framework and then proceed with the security analysis based on the identified framework.


## Usage

```
usage: mob-framework-radar.py [-h] -i INPUT [-v]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file (apk or ipa)
  -v, --verbose         Verbose mode
```

![Screenshot of mob-framework-radar](/images/screenshot.png)


## Supported frameworks / 

Currently mob-framework-radar is able to identify the following frameworks/platforms/references on Android/iOS applications:
- Flutter
- Cordova
- React Native
- Xamarin
- Capacitor
- Expo Platform
- Uno Platform 
- Security libraries ([RootBeer](https://github.com/scottyab/rootbeer), [IOSSecuritySuite](https://github.com/securing/IOSSecuritySuite), [freeRASP](https://github.com/talsec/Free-RASP-Community))


