"""
Description:
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def solution(string,markers):
    lines = string.split('\n')
    for c in markers:
        lines = [l.split(c)[0].rstrip() for l in lines]
    return '\n'.join(lines)

"""
Unit Test
"""
from test import Test

# -*- coding: utf-8 -*-
Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
solution('bananas lemons watermelons apples bananas bananas\n? watermelons avocados strawberries lemons oranges\navocados watermelons cherries watermelons pears bananas\n# watermelons avocados lemons watermelons bananas', ['=', '.', '-', '^'])
