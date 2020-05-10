"""
Description:
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59

Examples:

The maximum time never exceeds 359999 (99:59:59)
"""
def make_readable(seconds):
	hours = int(seconds/3600)
	minutes = int((seconds-hours*3600)/60)
	seconds = int(seconds-(hours*3600 + minutes*60))
	return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

"""
Unit Test
"""
from test import Test

Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
