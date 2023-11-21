<?php

declare(strict_types=1);

class Solution
{

  function maxProfit(array $prices): int
  {
    $lowest = 10;
    $prev = 0;
    $maxProfit = 0;
    for ($i = 0; $i < count($prices); $i++) {
      if ($prices[$i] < $lowest) {
        $lowest = $prices[$i];
      } else {
        if ($prices[$i] >= $prev) {
          $maxProfit = $prices[$i] - $lowest;
          $prev = $prices[$i];
        }
      }
    }

    return $maxProfit;
  }
}

$solution = new Solution();
$solution->maxProfit([2, 1, 2, 1, 0, 1, 2]);
