<?php

declare(strict_types=1);

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution
{
	function dfs($node)
	{
		if ($node) {
			$this->counter++;
			$this->dfs($node->left);
			$this->dfs($node->right);
		}
	}

	private $counter = 0;

	/**
	 * @param   TreeNode  $root
	 *
	 * @return Integer
	 */
	function countNodes($root)
	{
		if (!$root) {
			return $this->counter;
		}

		$this->dfs($root);

		return $this->counter;
	}
}