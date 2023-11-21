<?php

declare(strict_types=1);

class Solution
{

  function maxProfit(array $prices): int
  {
    $lowest = $prices[0];
    $prev = 0;
    $maxProfit = 0;
    for ($i = 0; $i < count($prices); $i++) {
      // echo ("$prices[$i] <br>");

      if ($prices[$i] < $lowest) {
        $lowest = $prices[$i];
        $prev = 0;
      } else if ($prices[$i] >= $prev) {
        if ($prices[$i] - $lowest > $maxProfit) {
          $maxProfit = $prices[$i] - $lowest;
        }
        $prev = $prices[$i];
      }
    }
    echo ($maxProfit);

    return $maxProfit;
  }
}

$solution = new Solution();
$solution->maxProfit([11, 7, 4, 2, 1]);
