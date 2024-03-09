/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function (head) {
    if (!head) return null;
    const oldToNew = new Map();

    let cur = head;
    while (cur) {
        oldToNew.set(cur, new Node(cur.val))
        cur = cur.next;
    }

    cur = head;
    while (cur) {
        const copy = oldToNew.get(cur);
        copy.next = oldToNew.get(cur.next) || null;
        copy.random = oldToNew.get(cur.random) || null;
        cur = cur.next
    }
    return oldToNew.get(head);

};