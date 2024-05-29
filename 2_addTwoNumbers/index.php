<?php

declare(strict_types=1);


class ListNode
{
	public $val = 0;
	public $next = null;

	function __construct($val = 0, $next = null)
	{
		$this->val  = $val;
		$this->next = $next;
	}
}

class Solution
{

	/**
	 * @param   ListNode  $l1
	 * @param   ListNode  $l2
	 *
	 * @return ListNode
	 */
	function addTwoNumbers($l1, $l2)
	{
		$dummy = new ListNode();
		$cur   = $dummy;
		$carry = 0;

		while ($l1 || $l2 || $carry) {
			$v1 = $l1 ? $l1->val : 0;
			$v2 = $l2 ? $l2->val : 0;

//			New digit
			$val       = $v1 + $v2 + $carry;
			$carry     = intdiv($val, 10);
			$val       = $val % 10;
			$cur->next = new ListNode($val);

//			Update
			$cur = $cur->next;
			$l1  = $l1 ? $l1->next : null;
			$l2  = $l2 ? $l2->next : null;
		}

		return $dummy->next;
	}
}

$solution = new Solution();
$solution->addTwoNumbers([2, 4, 3], [5, 6, 4]);