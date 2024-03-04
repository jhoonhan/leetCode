<?php

declare(strict_types=1);


class Solution
{

	/**
	 * @param   Integer[][]  $points
	 *
	 * @return Integer
	 */
	function findMinArrowShots($points)
	{
		usort($points, function ($a, $b) {
			return $a[0] - $b[0];
		});

		$res = [$points[0]];

		for ($i = 0; $i < count($points); $i++) {
			$lastMax = $res[array_key_last($res)][1];

			if ($points[$i][0] <= $lastMax) {
				$res[array_key_last($res)][1] = min(
					$lastMax, $points[$i][1]
				);
			} else {
				$res[] = $points[$i];
			}
		}

		echo(json_encode($res));

		return count($res);
	}
}

$solution = new Solution();
$solution->findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]);