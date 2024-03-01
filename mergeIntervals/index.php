<?php

declare(strict_types=1);


class Solution
{

	/**
	 * @param   Integer[][]  $intervals
	 *
	 * @return Integer[][]
	 */
	function merge($intervals)
	{
		usort($intervals, function ($a, $b) {
			return $a[0] - $b[0];
		});
		$res = [$intervals[0]];

		for ($i = 0; $i < count($intervals); $i++) {
			$lastEnd = end($res)[1];

			if ($intervals[$i][0] <= $lastEnd) {
				echo(max($lastEnd, $intervals[$i][1]));
				$res[array_key_last($res)][1] = max(
					$lastEnd, $intervals[$i][1]
				);
				echo('<br>');
			} else {
				$res[] = [$intervals[$i][0], $intervals[$i][1]];
			}
		}

		return $res;
	}
}


$solution = new Solution();
$solution->merge([[1, 3], [2, 6], [8, 10], [15, 18]]);