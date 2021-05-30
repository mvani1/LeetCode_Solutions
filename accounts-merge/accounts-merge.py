class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mapping = collections.defaultdict(set)
        em_toname = {}
        for i in accounts:
            name = i[0]
            for email in i[1:]:
                mapping[i[1]].add(email)
                mapping[email].add(i[1])
                em_toname[email] = name
        seen  = set()
        ans = []
        for email in mapping:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for neigh in mapping[node]:
                        if neigh not in seen:
                            seen.add(neigh)
                            stack.append(neigh)
                ans.append([em_toname[email]]+sorted(component))
        return ans