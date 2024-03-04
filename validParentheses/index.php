<?php

declare(strict_types=1);

class Solution
{
	public function isValid(string $s): bool
	{
		$stack = new SplStack();
		$pairs = [
			"]" => "[",
			"}" => "{",
			")" => "("
		];
		for ($i = 0; $i < strlen($s); $i++) {
			$v = $s[$i];
			if ($pairs[$v]) {
				if ($stack->isEmpty() || $stack->pop() !== $pairs[$v]) {
					return false;
				}
			} else {
				$stack->push($v);
			}
		}

		return $stack->isEmpty();
	}
}

$solution = new Solution();
$solution->isValid("(])");