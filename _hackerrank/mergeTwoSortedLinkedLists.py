def mergeLists(head1, head2):
    start = head1 if head1.data < head2.data else head2

    while head1 or head2:

        if head1.data < head2.data:
            prev = head1
            while head1 and head1.data < head2.data:
                prev = head1
                head1 = head1.next
            prev.next = head2
            head1 = head2
        else:
            prev = head2
            while head2 and head1.data >= head2.data:
                prev = head2
                head2 = head2.next
            prev.next = head1
            head2 = head1
        break

    return start


[1, 2, 3]
[3, 4]
