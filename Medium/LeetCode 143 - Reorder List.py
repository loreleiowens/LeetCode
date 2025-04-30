class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
      # finds the midpoint but iterating over the list with two pointers
        point1, point2 = head, head.next
      
        while point2 and point2.next: # Will stop at midpoint 
            point1 = point1.next
            point2 = point2.next.next

      # Divides the list into sections at midpoint
        second = point1.next
        prev = None
        point1.next = None

      # Reverses the order of the second portion of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

      # Combines the two halves of the list 
        firstNo, secondNo = head, prev
        while secondNo:
            temp1, temp2 = firstNo.next, secondNo.next
            firstNo.next = secondNo
            secondNo.next = temp1
            firstNo, secondNo = temp1, temp2
