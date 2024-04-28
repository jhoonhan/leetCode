<?php

declare(strict_types=1);

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution
{


	/**
	 * @param   ListNode  $head
	 * @param   Integer   $n
	 *
	 * @return ListNode
	 */
	function removeNthFromEnd($head, $n)
	{
		$dummy = new ListNode(0, $head);
		$left  = $dummy;
		$right = $head;
		while ($n > 0 && $right) {
			$right = $right->next;
			$n--;
		}

		while ($right) {
			$right = $right->next;
			$left  = $left->next;
		}

		$left->next = $left->next->next;


		return $dummy->next;
	}

}
