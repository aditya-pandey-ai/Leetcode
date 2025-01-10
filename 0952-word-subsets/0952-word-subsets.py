class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)

        for i in words2:
            count_w = Counter(i)
            for c,cnt in count_w.items():
                count_2[c] = max(count_2[c],cnt)
        res = []

        for i in words1:
            count_w = Counter(i)
            flag = True
            for c,cnt in count_2.items():
                if count_w[c] < cnt:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res