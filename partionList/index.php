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
	 * @param   Integer   $x
	 *
	 * @return ListNode
	 */
	function partition($head, $x)
	{
		$l     = new ListNode();
		$r     = new ListNode();
		$lTail = $l;
		$rTail = $r;

		while ($head) {
			if ($head->val < $x) {
				$lTail->next = $head;
				$lTail       = $lTail->next;
			} else {
				$rTail->next = $head;
				$rTail       = $rTail->next;
			}
			$head = $head->next;
		}
		$lTail->next = $r->next;
		$rTail->next = null;

		return $l->next;
	}
}