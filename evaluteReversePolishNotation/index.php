<?php

declare(strict_types=1);

class Solution
{

	/**
	 * @param   String[]  $tokens
	 *
	 * @return Integer
	 */
	function evalRPN($tokens)
	{
		$stack = new SplStack();
		foreach ($tokens as $el) {
			if (is_numeric($el)) {
				$stack->push($el);
			} else {
				$el1 = $stack->pop();
				$el2 = $stack->pop();
				$res = 0;
				if ($el === '+') {
					$res = $el2 + $el1;
				} elseif ($el === '-') {
					$res = $el2 - $el1;
				} elseif ($el === '*') {
					$res = $el2 * $el1;
				} elseif ($el === '/') {
					$res = intval($el2 / $el1);
				}
				$stack->push($res);
			}
		}

		return $stack->top();
	}
}

$solution = new Solution();
$solution->evalRPN(["4", "13", "5", "/", "+"]);