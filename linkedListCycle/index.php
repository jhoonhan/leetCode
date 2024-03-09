<?php

declare(strict_types=1);

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */
class Solution
{
	/**
	 * @param   ListNode  $head
	 *
	 * @return Boolean
	 */
	function hasCycle($head)
	{
		$slow = $head;
		$fast = $head;
		while ($fast && $fast->next) {
			$slow = $slow->next;
			$fast = $fast->next->next;

			if ($slow === $fast) {
				return true;
			}
		}

		return false;
	}
}

$solution = new Solution();
$solution->hasCycle([3, 2, 0, -4]);