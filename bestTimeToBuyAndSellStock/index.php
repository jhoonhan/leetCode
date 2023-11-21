<?php

declare(strict_types=1);

class Solution
{

  function maxProfit(array $prices): int
  {
    // Solution 1: My solution
    // $lowest = $prices[0];
    // $prev = 0;
    // $maxProfit = 0;
    // for ($i = 0; $i < count($prices); $i++) {
    //   // echo ("$prices[$i] <br>");

    //   if ($prices[$i] < $lowest) {
    //     $lowest = $prices[$i];
    //     $prev = 0;
    //   } else if ($prices[$i] >= $prev) {
    //     if ($prices[$i] - $lowest > $maxProfit) {
    //       $maxProfit = $prices[$i] - $lowest;
    //     }
    //     $prev = $prices[$i];
    //   }
    // }
    // echo ($maxProfit);

    // return $maxProfit;

    // Solution 2: Slow but simple
    // $ptLow = PHP_INT_MAX;
    // $maxProf = 0;

    // for ($i = 0; $i < count($prices); $i++) {
    //   $ptLow = min($ptLow, $prices[$i]);
    //   $maxProf = max($maxProf, $prices[$i] - $ptLow);
    // }
    // return $maxProf;

    // Solution 3: Optimal but slow
    $l = 0;
    $r = 1;
    $max = 0;
    while ($r < count($prices)) {
      if ($prices[$l] < $prices[$r]) {
        $profit = $prices[$r] - $prices[$l];
        $max = max($max, $profit);
      } else {
        $l = $r;
      }
      $r++;
      echo ($max);
    }

    return $max;
  }
}

$solution = new Solution();
$solution->maxProfit([11, 7, 4, 2, 1]);
