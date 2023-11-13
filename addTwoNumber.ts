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

// function getNumberFromList(list: ListNode): number {
//   let output = 0;
//   let index = 0;

//   let runner: ListNode | null = list;
//   while (runner) {
//     output += runner.val * Math.pow(10, index);
//     runner = runner.next;
//     index++;
//   }
//   return output;
// }

function addTwoNumbers(l1: ListNode, l2: ListNode): ListNode {
  const n1 = getNumberFromList(l1);
  123;
  const n2 = getNumberFromList(l2);
  234;
  const sum = (n1 + n2).toString();
  357;

  let output: ListNode | null = null;

  for (let i = 0; i < sum.length; i++) {
    const digit = sum[i];
    3;

    output = new ListNode(Number(digit), output);
  }

  return output as ListNode;
}
