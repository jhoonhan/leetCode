<?php

declare(strict_types=1);


class Solution
{

	/**
	 * @param   TreeNode  $root
	 *
	 * @return Float[]
	 */
	function averageOfLevels($root)
	{
		$res = [];
		$q   = new \SplQueue();
		$q->enqueue($root);


		while (!$q->isEmpty()) {
			$qLen  = $q->count();
			$level = [];
			for ($i = 0; $i < $qLen; $i++) {
				$node = $q->dequeue();
				if ($node) {
					$level[] = $node->val;
					$q->enqueue($node->left);
					$q->enqueue($node->right);
				}
			}
			if ($level) {
				$res[] = array_sum($level) / count($level);
			}
		}

		return $res;
	}
}