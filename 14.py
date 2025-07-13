#14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

#sloution 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=strs[0]
        prelen=len(pre)

        for s in strs[1:]:
            while pre!=s[0:prelen]:
                prelen-=1
                if prelen==0:
                    return ""

                pre=pre[0:prelen]
        
        return pre
