class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_sorted = []
        answer = []
        for word in strs: words_sorted.append("".join(sorted(word)))     
        dict_words_with_index = {}
        for idx, word in enumerate(words_sorted):
            if word not in dict_words_with_index:
                dict_words_with_index[word] = [idx]
            else:
                new_idx = dict_words_with_index[word]
                new_idx.append(idx)
                dict_words_with_index[word] = new_idx
        for _, value in dict_words_with_index.items():
            temp = []
            for idx in value:
                temp.append(strs[idx])
            answer.append(temp)
        return answer