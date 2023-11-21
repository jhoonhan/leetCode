<?php

declare(strict_types=1);

class Solution
{
  /**
   * @param int[] $prices
   * @return int
   */
  function maxProfit($prices)
  {
    $p = 0;
    for ($i = 0; $i < count($prices) - 1; $i++) {
      if ($prices[$i] > $prices[$i + 1]) {
        $p += 0;
      } else {
        $p += $prices[$i + 1] - $prices[$i];
      }
    }
    return $p;
  }

  // function maxProfit(array $prices): int
  // {
  //   // Solution 3: Optimal but slow
  //   $l = 0;
  //   $r = 1;
  //   $max = 0;
  //   while ($r < count($prices)) {
  //     if ($prices[$l] < $prices[$r]) {
  //       $profit = $prices[$r] - $prices[$l];
  //       $max = max($max, $profit);
  //     } else {
  //       $l = $r;
  //     }
  //     $r++;
  //     echo ($max);
  //   }

  //   return $max;
  // }
}

$solution = new Solution();
$solution->maxProfit([7, 1, 5, 3, 6, 4]);
