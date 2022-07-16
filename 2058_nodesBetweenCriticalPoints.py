class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # First acquiring the values from the linked list
        # Detect the critical points and storing the index of them
        # Return the minimum distance by looping through the array as well as the maximum distance
        
        val = []
        val.append(head.val)
        while (head.next != None):
            head = head.next
            val.append(head.val)
        
        critical = []
        
        for i in range(1,len(val)-1):
            if val[i-1] < val[i] and val [i+1] < val[i]:
                critical.append(i)
            elif val[i-1] > val[i] and val[i+1] > val[i]:
                critical.append(i)
        if len(critical) < 2:
            return [-1,-1]
        else:
            minDistance = float('inf')
            for i in range(1,len(critical)):
                if critical[i] - critical[i-1] < minDistance:
                    minDistance = critical[i] - critical[i-1]
            return[minDistance,critical[-1]-critical[0]]
