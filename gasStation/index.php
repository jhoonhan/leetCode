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
    $difference = [];
    foreach ($gas as $i) {
      # code...
      $difference[$i] = $gas[i] - $cost[$i];
    }
    print_r($difference);

    return 0;
  }
}


$solution = new Solution();
$solution->canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]);
