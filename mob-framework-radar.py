#!/usr/bin/python3
import zipfile
import argparse

# Command line argument parser 
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",type=str,required=True,help="""Input file (apk or ipa)""")
parser.add_argument("-v","--verbose",action='store_true',help="""Verbose mode""")
args = parser.parse_args()

# Colors
RED = "\033[0;31m"
END = "\033[0m"

# open apk/ipa file
zip = zipfile.ZipFile(args.input)

# list files present in the installer
list_files = zip.namelist()

# mobile frameworks references
frameworks = {
  "Flutter": ['libflutter.so', 'libapp.so', 'Frameworks/Flutter.framework', 'flutter_assets/kernel_blob.bin'], 
  "Cordova": ['www/cordova.js', 'www/index.html', 'www/cordova_plugins.js', 'public/cordova.js'],
  "React Native": ['libreactnativejni.so', 'assets/index.android.bundle', '/main.jsbundle', 'react-native/package.json'],
  "Expo": ['Expo.plist', 'META-INF/expo'], 
  "Xamarin": ['assemblies/Mono.Android.dll', 'mscorlib.dll', 'Mono.Security.dll', 'Xamarin.iOS.dll', 'libxamarin-app.so', 'libmonodroid.so', 'libmonosgen-2.0.so'],
  "Capacitor": ['capacitor.config.json', 'capacitor.plugins.json', 'Frameworks/Capacitor.framework']
}

# search files related to mobile frameworks
for key in frameworks:
	hitted_list = [] 
	for file in list_files:
		for elem in frameworks[key]:
			if elem in file:
				hitted_list.append(file)
	if hitted_list:
		print ("\n"+ RED + "[+] " + key + " references found " + END)
		if args.verbose:
			print(hitted_list)