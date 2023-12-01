<?php

declare(strict_types=1);

class Solution
{

  /**
   * @param array $gas
   * @param array $cost
   * @return int    
   */
  function canCompleteCircuit(array $gas, array $cost): int
  {
    if (array_sum($gas) < array_sum($cost)) {
      return -1;
    }

    $total = 0;
    $res = 0;

    for ($i = 0; $i < count($gas); $i++) {
      $total += $gas[$i] - $cost[$i];
      if ($total < 0) {
        $total = 0;
        $res = $i + 1;
      }
    }
    return $res;

    return 0;
  }
}


$solution = new Solution();
$solution->canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]);
