class Solution:
    def divisorGame(self, N: int) -> bool:
        # https://www.acwing.com/solution/LeetCode/content/1750/
        # �o�{�p�GN���_�ơA�h�]�_�ƪ��]�ƵL���ƦӨϪ��U�@�ӼƤ@�w�����ơA�õo�{�g3���H�@�w��A�]�����ƥ�Ĺ
        # T:O(1) S:O(1)
        return N%2==0
        '''
        canWin = [None]*(N+1)
        canWin[0:3] = [True, False, True]
                
        for i in range(3,N+1):
            canWin[i] = False
            for j in range(1,i):
                if (i%j == 0) and (canWin[i-j] == False):
                    canWin[i] = True
                    break
        return canWin[N]
        '''