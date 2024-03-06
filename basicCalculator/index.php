<?php

declare(strict_types=1);


class Solution
{
	private $operators = ['+', '-'];

	function calcStack($stk): int
	{
		$res    = 0;
		$curVal = '';
		while (count($stk) > 0) {
			$curr = $stk->pop();
			if (is_numeric($curr)) {
				$curVal = $curr . $curVal;
			} else {
				if ($curr === '-') {
					$curVal = '-' . $curVal;
				}
				$res    += (int)$curVal;
				$curVal = '';
			}

			if (count($stk) === 0 && is_numeric($curr)) {
				$res += (int)$curr;
			}
		}

		return $res;
	}

	/**
	 * @param   String  $s
	 *
	 * @return Integer
	 */
	function calculate($s)
	{
		$ns          = str_replace(' ', '', $s);
		$chars       = str_split($ns);
		$stack       = new SplStack();
		$pStack      = new SplStack();
		$isP         = false;
		$parenthesis = ['(', ')'];
		foreach ($chars as $char) {
			if ($char === '(') {
				$isP = true;
				foreach ($pStack as $el) {
					$pStack->pop();
				}
			} elseif ($char === ')') {
				$isP = false;
				$res = $this->calcStack($pStack);
				$stack->push($res);
			}
			if ($isP && !in_array($char, $parenthesis)) {
				$pStack->push($char);
			}
		}
		var_dump($stack);
	}
}

$solution = new Solution();
$solution->calculate("(5 + (0 - 3) + 2)");