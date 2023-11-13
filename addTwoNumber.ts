class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// function getNumberFromList(list: ListNode): bigint {
//   let numberString = "";

//   let runner: ListNode | null = list;
//   while (runner) {
//     numberString = runner.val.toString() + numberString;
//     runner = runner.next;
//   }
//   return BigInt(numberString);
// }

// function addTwoNumbers(l1: ListNode, l2: ListNode): ListNode {
//   const n1 = getNumberFromList(l1);
//   const n2 = getNumberFromList(l2);
//   const sum = (n1 + n2).toString();

//   let output: ListNode | null = null;

//   for (let i = 0; i < sum.length; i++) {
//     const digit = sum[i];
//     3;

//     output = new ListNode(Number(digit), output);
//   }

//   return output as ListNode;
// }

function addTwoNumbers(l1: ListNode, l2: ListNode): ListNode {
  let r1: ListNode | null = l1;
  let r2: ListNode | null = l2;
  const output: ListNode = new ListNode();
  let runner: ListNode | null = output;

  while (r1 || r2) {
    let digit = (r1?.val || 0) + (r2?.val || 0);
    if (digit >= 10) {
      digit -= 10;

      if (r1?.next) {
        r1.next.val++;
      } else if (r2?.next) {
        r2.next.val++;
      } else if (r1) {
        r1.next = new ListNode(1);
      } else if (r2) {
        r2.next = new ListNode(1);
      }
    }
    runner.val = digit;
    if (r1?.next || r2?.next) {
      runner.next = new ListNode();
      runner = runner.next;
    }
    if (r1) {
      r1 = r1.next;
    }
    if (r2) {
      r2 = r2.next;
    }
  }

  return output;
}
