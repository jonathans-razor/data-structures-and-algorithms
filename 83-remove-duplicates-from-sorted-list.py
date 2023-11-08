import sys
from typing import Optional
from typing import Optional, List

if len(sys.argv) < 2:
  print("- Parameter(s) expected.")
  sys.exit(1)

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
  if head is None:
    return None
  current = head
  while current.next is not None:
    if current.val == current.next.val:
      current.next = current.next.next
    else:
      current = current.next
  return head

print(deleteDuplicates(sys.argv[1]))