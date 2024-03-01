<?php

declare(strict_types=1);

class Solution
{

	/**
	 * @param   Integer[]  $nums
	 *
	 * @return Integer
	 */
	function longestConsecutive($nums)
	{
		$set     = [];
		$longest = 0;

		foreach ($nums as $num) {
			$set[$num] = true;
		}

		foreach ($nums as $num) {
			if (!isset($set[$num - 1])) {
				$length = 0;
				while (isset($set[$num + $length])) {
					$length++;
				}
				$longest = max($length, $longest);
			}
		}

//		foreach ($nums as $num) {
//			echo('dafuck');
//			if (!in_array($num - 1, $set)) {
//				$length = 0;
//				while (in_array($num + $length, $set)) {
//					$length++;
//				}
//				$longest = max($length, $longest);
//			}
//			echo(json_encode($longest));
//		}
//		echo(json_encode($longest));
		echo(json_encode($longest));

		return $longest;
	}
}

$solution = new Solution();
$solution->longestConsecutive([100, 4, 200, 1, 3, 2]);