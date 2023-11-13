<?php declare(strict_types=1);

// Definition for a singly-linked list.
class ListNode {
      public int $val = 0;
      public ListNode | null $next = null;
      function __construct($val = 0, $next = null) {
          $this->val = $val;
          $this->next = $next;
      }
}

$l1 =
    new ListNode(1,
        new ListNode(2,
            new ListNode(3,
                new ListNode(0,
                    new ListNode(0,
                        new ListNode(0,
                            new ListNode(0,
                                new ListNode(0,
                                    new ListNode(0,
                                        new ListNode(0,
                                            new ListNode(0,
                                                new ListNode(0,
                                                    new ListNode(1,
                                                        new ListNode(0,
                                                            new ListNode(0,
                                                                new ListNode(9,
                                                                    new ListNode(1, null)))))))))))))))
        )
    );
$l2 =
    new ListNode(2,
        new ListNode(3,
            new ListNode(4,
                null)
        )
    );



class Solution {
    function getNumber(ListNode $numList): string {
        /**
         * @param string $numStr
         * @param ListNode | null $runner
         * @return void
         */
        $numStr = "";
        $runner = $numList;
        while ($runner) {
            $numStr = $runner->val . $numStr;
            $runner = $runner->next;
        }
        echo(bcmul($numStr, "1"). "<br>");
        return bcmul($numStr, "1");
    }

    function addTwoNumbers(ListNode $l1, ListNode $l2): ListNode {
        /**
         * @param ListNode | null $output
         */
        $n1 = $this->getNumber($l1);
        $n2 = $this->getNumber($l2);

        $addStr = bcadd($n1, $n2);

        $output = null;

        for($i = 0; $i < strlen($addStr); $i++) {
            $output = new ListNode((int) $addStr[$i], $output);
        }
//        var_dump($output);
        return $output;
    }
}

$solution = new Solution();
$solution->addTwoNumbers($l1, $l2);
