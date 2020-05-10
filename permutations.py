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

print(permutations('a'))
print(set(permutations('a')) == set(['a']))
print(permutations('ab'))
print(set(permutations('ab')) == set(['ab', 'ba']))
print(permutations('aabb'))
print(set(permutations('aabb')) == set(['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']))
