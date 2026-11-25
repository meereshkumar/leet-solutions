class Solution:

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap: list[tuple[int, int, ListNode]] = []

        
        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next