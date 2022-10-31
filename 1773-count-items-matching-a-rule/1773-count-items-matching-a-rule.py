class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        itemsCount = 0
        ruleKeyDictionary = {"type":0, "color":1, "name":2}
        for item in items:
            if ruleValue == item[ruleKeyDictionary[ruleKey]]:
                itemsCount += 1
        return itemsCount
                    