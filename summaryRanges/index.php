<?php

class Solution
{

	/**
	 * @param   Integer[]  $nums
	 *
	 * @return String[]
	 */
	function summaryRanges($nums)
	{
		$result = [];
		$start  = $nums[0];
		$end    = $nums[0];
		for ($i = 1; $i <= count($nums); $i++) {
			if (isset($nums[$i])) {
				if ($nums[$i] - $nums[$i - 1] !== 1) {
					$result[] = $start === $end ? (string)$start
						: "$start->$end";
					$start    = $nums[$i];
				}
				$end = $nums[$i];
			} else {
				$result[] = $start === $end ? (string)$start : "$start->$end";
			}
		}

		return $result;
	}
}

$solution = new Solution();
$solution->summaryRanges([0, 1, 2, 4, 5, 7]);
