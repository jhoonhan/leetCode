class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function getNumberFromList(list: ListNode): number {
  let numberString = "";

  let runner: ListNode | null = list;
  while (runner) {
    numberString = runner.val.toString() + numberString;
    runner = runner.next;
  }
  return Number(numberString);
}

function addTwoNumbers(l1: ListNode, l2: ListNode): ListNode {
  return l1.next;
}
