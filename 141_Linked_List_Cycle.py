# ---------------------------- SOLUTION ----------------------------
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
# ---------------------------- SOLUTION ----------------------------


if __name__ == "__main__":
    no1 = ListNode(3)
    no2 = ListNode(2)
    no3 = ListNode(0)
    no4 = ListNode(-4)
    
    no1.next = no2
    no2.next = no3
    no3.next = no4
    
    no4.next = no2
    
    head = no1
    
    validador = Solution()
    resultado = validador.hasCycle(head)
    
    print(f"A lista possui ciclo? {resultado}")  # Deve printar: True
