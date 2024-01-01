def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """

        #维护一个哈系表，记录当前的值

        hash_map = {}

        max_len = 0
        start = 0
        now_len = 0
        i = 0

        while i < len(s):
            if  s[i] not in hash_map.keys():
                hash_map[s[i]] = i + 1
                now_len += 1
            else:
                start = hash_map[s[i]]
                if s[i] == s[i-1]:
                    hash_map[s[i]] = i + 1
                else:
                    del hash_map[s[i]]
                i = start
                if not i < len(s):
                    break
                now_len = 0
            if max_len < now_len:
                    max_len = now_len 
            i += 1   
            

if __name__ == '__main__':
     lengthOfLongestSubstring("abcabcbb")