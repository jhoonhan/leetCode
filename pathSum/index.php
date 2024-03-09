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
	private $isFirst = true;

	/**
	 * @param   TreeNode  $root
	 * @param   Integer   $targetSum
	 *
	 * @return Boolean
	 */
	function hasPathSum($root, $targetSum)
	{
		if (!$root) {
			return false;
		}

		if (!$root->left && !$root->right) {
			echo($targetSum - $root->val);
			echo('<br>');

			return $targetSum === $root->val;
		}

		return ($this->hasPathSum($root->left, $targetSum - $root->val)
			&& $this->hasPathSum($root->right, $targetSum - $root->val));
	}
}

$solution = new Solution();
$solution->hasPathSum([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1], 22
);