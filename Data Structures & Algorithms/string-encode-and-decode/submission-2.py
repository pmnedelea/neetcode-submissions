class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output = output + i + 'À'
        return output

    def decode(self, s: str) -> List[str]:
        temp = ""
        output = []
        for i in s:
            if i == 'À':
                output.append(temp)
                temp = ""
            else:
                temp = temp + i
        
        return output


