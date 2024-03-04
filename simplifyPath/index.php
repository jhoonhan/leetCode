<?php

declare(strict_types=1);


class Solution
{


	function simplifyPath(string $path): string
	{
		$stack   = new SplStack();
		$curr    = '';
		$newPath = $path . '/';


		for ($i = 0; $i < strlen($newPath); $i++) {
			if ($newPath[$i] === '/') {
				if ($curr === '..') {
					if (!$stack->isEmpty()) {
						$stack->pop();
					}
				} elseif ($curr !== '' && $curr !== '.') {
					$stack->push($curr);
				}
				$curr = '';
			} else {
				$curr .= $newPath[$i];
			}
		}
		$arr          = iterator_to_array($stack);
		$arr_reversed = array_reverse($arr);

		$res = implode("/", $arr_reversed);

		return '/' . $res;
	}

}

$solution = new Solution();
$solution->simplifyPath("/a//b////c/d//././/..");