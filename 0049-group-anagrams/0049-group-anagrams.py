class Solution(object):
    def groupAnagrams(self, strs):
        str_map=dict()
        for word in strs:
            sorted_str=''.join(sorted(word))
            # If the key isn't in the map yet, create it with an empty list
            if sorted_str not in str_map:
                str_map[sorted_str] = []
            str_map[sorted_str].append(word)
        return list(str_map.values())        
        
        