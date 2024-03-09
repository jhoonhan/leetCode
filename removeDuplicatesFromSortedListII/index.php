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
	 *
	 * @return ListNode
	 */
	function deleteDuplicates($head)
	{
		$dummy = new ListNode(0, $head);
		$l     = $dummy;
		$r     = $head;

		while ($r) {
			if ($r->val === $r->next->val) {
				while ($r->val === $r->next->val) {
					$r = $r->next;
				}
				$r = $r->next;
			}

			if ($r->val !== $r->next->val || !$r) {
				$l->next = $r;
				$l       = $l->next;
				$r       = $r->next;
			}
		}


		return $dummy->next;
	}
}