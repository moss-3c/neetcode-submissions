class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'EMPTY_LIST'
        return '!@#$_'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'EMPTY_LIST':
            return []
        return [string for string in s.split('!@#$_')]