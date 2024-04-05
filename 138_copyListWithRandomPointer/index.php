<?php

declare(strict_types=1);

/**
 * Definition for a Node.
 * class Node {
 *     public $val = null;
 *     public $next = null;
 *     public $random = null;
 *     function __construct($val = 0) {
 *         $this->val = $val;
 *         $this->next = null;
 *         $this->random = null;
 *     }
 * }
 */
class Solution
{
	/**
	 * @param   Node  $head
	 *
	 * @return Node
	 */
	function copyRandomList($head)
	{
		echo('dafuck');
		$mapOfOld = [null => null];


		$cur = $head;
		while ($cur && $cur->val) {
			$copy                = new Node($head->val);
			$mapOfOld[$cur->val] = $copy;
			$cur                 = $cur->next;
		}

		$cur = $head;
		while ($cur && $cur->val) {
			$copy         = $mapOfOld[$cur->val];
			$copy->next   = $mapOfOld[$cur->next->val];
			$copy->random = $mapOfOld[$cur->random->val];
			$cur          = $cur->next;
		}

		return $mapOfOld[$head->val];
	}
}