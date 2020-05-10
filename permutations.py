"""
Description:
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); // ['a']
permutations('ab'); // ['ab', 'ba']
permutations('aabb'); // ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
permutations("a"); // => vector<string> {"a"}
permutations("ab"); // => vector<string> {"ab", "ba"}
permutations("aabb"); // => vector<string> {"aabb", "abab", "abba", "baab", "baba", "bbaa"}
permutations('a'); // => ['a']
permutations('ab'); // => ['ab', 'ba']
permutations('aabb'); // => ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
permutations    "a" `shouldBe` ["a"]
permutations   "ab" `shouldBe` ["ab", "ba"]
permutations "aabb" `shouldBe` ["aabb","abab","abba","baab","baba","bbaa"]
Permutations.singlePermutations("a") `shouldBe` ["a"]
Permutations.singlePermutations("ab") `shouldBe` ["ab", "ba"]
Permutations.singlePermutations("aabb") `shouldBe` ["aabb","abab","abba","baab","baba","bbaa"]
Permutations.SinglePermutations("a"); // => new List {"a"}
Permutations.SinglePermutations("ab"); // => new List {"ab", "ba"}
Permutations.SinglePermutations("aabb"); // => new List {"aabb", "abab", "abba", "baab", "baba", "bbaa"}
The order of the permutations doesn't matter.
"""

def permutations(string):
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):
            for s in permutations(string[:i] + string[i + 1:]):
                result.add(c + s)

    return list(result)


"""
Unit Test
"""
from test import Test

Test.describe('Basic tests')
Test.it('unique letters')
Test.assert_equals(sorted(permutations('a')), ['a'])
Test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
Test.assert_equals(sorted(permutations('abc')), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    
abcd = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
      'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
Test.assert_equals(sorted(permutations('abcd')), abcd)
Test.assert_equals(sorted(permutations('bcad')), abcd)
Test.assert_equals(sorted(permutations('dcba')), abcd)
Test.it('duplicate letters')
Test.assert_equals(sorted(permutations('aa')), ['aa'])
Test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
Test.assert_equals(sorted(permutations('aaaab')), ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa'])
Test.assert_equals(sorted(permutations('aaaaab')), ['aaaaab', 'aaaaba', 'aaabaa', 'aabaaa', 'abaaaa', 'baaaaa'])

Test.describe("Random tests")
from random import randint
def permsol(string): from itertools import permutations as perm; return sorted(set(map(lambda x: "".join(x), perm(string))))
base="abcdefghijklmnopqrstuvwxyz"

for i in range(40):
    string="".join([base[randint(0,len(base)-1)] for i in range(randint(1,8))])
    Test.it("Testing for "+string)
    Test.assert_equals(sorted(permutations(string)),permsol(string))

