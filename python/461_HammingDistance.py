class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #return sum([int(i) for i in list('{:032b}'.format(x^y))])  #40ms 14.1MB my method
        #return list('{:032b}'.format(x^y)).count('1')              #52ms 13.8MB reference
        return bin(x^y)[2:].count('1') #remove '0b'                 #28ms 13.9MB reference