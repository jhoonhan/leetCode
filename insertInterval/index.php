<?php

declare(strict_types=1);

class Solution
{

	/**
	 * @param   Integer[][]  $intervals
	 * @param   Integer[]    $newInterval
	 *
	 * @return Integer[][]
	 */
	function insert($intervals, $newInterval)
	{
		$intervals[] = $newInterval;
		usort($intervals, function ($a, $b) {
			return $a[0] - $b[0];
		});

		$res = [$intervals[0]];

		for ($i = 0; $i < count($intervals); $i++) {
			$lastEnd = $res[array_key_last($res)][1];

			if ($intervals[$i][0] <= $lastEnd) {
//				Overlapping
				$res[array_key_last($res)][1] = max(
					$lastEnd, $intervals[$i][1]
				);
			} else {
				$res[] = [$intervals[$i][0], $intervals[$i][1]];
			}
		}

//		echo(json_encode($res));

		return $res;
	}
}

$solution = new Solution();
$solution->insert([[1, 3], [6, 9]], [2, 5]);