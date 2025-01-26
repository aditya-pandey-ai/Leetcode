class Solution:
    def maximumInvitations(self, A: List[int]) -> int:
        # First, we find the largest circle.
        n, maxc = len(A), 0
        seen = [0] * n
        for idx in range(n):
            # If a person hasn't been visited:
            if seen[idx] == 0:
                # 'start' is for locating the first visited person,
                # 'cur_people' stands for the current person we are visiting,
                # 'curset' stores all the visited people in this iteration.
                start = idx
                cur_people = idx
                curset = set()
                
                # As long as we are visiting new people, keep finding their favorite.
                while seen[cur_people] == 0:
                    seen[cur_people] = 1
                    curset.add(cur_people)
                    cur_people = A[cur_people]
                
                # If we find the first visited person, check if it's part of this cycle.
                if cur_people in curset:  # Found a new cycle.
                    cursum = len(curset)
                    
                    # Use 'start' to find the distance from the first visited person to this person.
                    while start != cur_people:
                        cursum -= 1
                        start = A[start]
                    maxc = max(maxc, cursum)
        
        # Find the sum of the largest arms. First, find all mutual-favorite pairs.
        pair = []
        visited = [0] * n
        for i in range(n):
            # If a is b's favorite and vice versa, add to 'pair'.
            if A[A[i]] == i and visited[i] == 0:
                pair.append([i, A[i]])
                visited[i] = 1
                visited[A[i]] = 1
        
        # For every person i, find all the people whose favorite is i.
        res = 0
        child = collections.defaultdict(list)
        for i in range(n):
            child[A[i]].append(i)
        
        for a, b in pair:
            # Max arm length starting from person a.
            maxa = 0
            dq = collections.deque()
            for cand in child[a]:
                if cand != b:
                    dq.append([cand, 1])
            while dq:
                cur, length = dq.popleft()
                maxa = max(maxa, length)
                for nxt in child[cur]:
                    dq.append([nxt, length + 1])
            
            # Max arm length starting from person b.
            maxb = 0
            dq = collections.deque()
            for cand in child[b]:
                if cand != a:
                    dq.append([cand, 1])
            while dq:
                cur, length = dq.popleft()
                maxb = max(maxb, length)
                for nxt in child[cur]:
                    dq.append([nxt, length + 1])
            
            # Total length is the two longest arms plus 2 (a and b themselves).
            res += 2 + maxa + maxb
        
        # Select the larger value as the answer.
        return max(maxc, res)
