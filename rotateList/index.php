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
	private $counter = 0;

	/**
	 * @param   ListNode  $head
	 * @param   Integer   $k
	 *
	 * @return ListNode
	 */
	function rotateRight($head, $k)
	{
		if (!$head) {
			return null;
		}

		$length = 1;
		$tail   = $head;

		while ($tail->next) {
			$tail = $tail->next;
			$length++;
		}

		$k = $k % $length;
		if ($k === 0) {
			return $head;
		}
		$cur = $head;
		for ($i = $length - $k - 1; $i > 0; $i--) {
			$cur = $cur->next;
		}
		$newHead    = $cur->next;
		$cur->next  = null;
		$tail->next = $head;

		return $newHead;
	}
}