#!/usr/bin/python3

from urllib import request, error

try:
	request.urlopen("http://google.com", timeout=2)
	print("Internet Connection working.")
except error.URLError:
	print("No Internet :(")
