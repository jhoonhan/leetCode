/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {

    if (!head) return null;
    let count = 1;
    let cur = head;
    while (cur) {
        if (count <= left && count >= right) {
            console.log(count);
        }
        cur = cur.next;
    }
};