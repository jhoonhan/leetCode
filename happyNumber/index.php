<?php

declare(strict_types=1);

class Solution
{
	private $hashMap = [];

	function isHappy(int $n)
	{
		$numbersStr = str_split((string)$n);
		$sum        = 0;
		for ($i = 0; $i < count($numbersStr); $i++) {
			$sum += (int)$numbersStr[$i] * (int)$numbersStr[$i];
		}
		if ($sum === 1) {
			return true;
		} else {
			if (in_array($sum, $this->hashMap)) {
				return false;
			}
			$this->hashMap[] = $sum;

			return $this->isHappy($sum);
		}
	}
}


$aang = new Solution;

$aang->isHappy(19);
