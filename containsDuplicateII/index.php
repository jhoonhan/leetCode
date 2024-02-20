<?php


class Solution
{

	/**
	 * @param   Integer[]  $nums
	 * @param   Integer    $k
	 *
	 * @return Boolean
	 */
	function containsNearbyDuplicate($nums, $k)
	{
		$hashMap = [];
		for ($i = 0; $i < count($nums); $i++) {
			if (isset($hashMap[$nums[$i]]) && $i - $hashMap[$nums[$i]] <= $k) {
				return true;
			}
			$hashMap[$nums[$i]] = $i;
		}

		return false;
	}
}

$solution = new Solution();
$solution->containsNearbyDuplicate([1, 1], 1);