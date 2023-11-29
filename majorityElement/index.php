<?php

declare(strict_types=1);

class Solution
{

  /**
   * @param Integer[] $nums
   * @return Integer
   */
  function majorityElement($nums)
  {
    $map = array();
    $largest = 0;
    $result = 0;

    for ($i = 0; $i < count($nums); $i++) {
      $mapCount = 1;
      if (isset($map[$nums[$i]])) {
        $mapCount = $map[$nums[$i]] + 1;
      };
      $map[$nums[$i]] = $mapCount;

      if ($mapCount > $largest) {
        $largest = $mapCount;
        $result = $nums[$i];
      }
      // print($mapCount);
    }
    return $result;

    $nv = array_count_values($nums);
    arsort($nv);
    return array_keys($nv)[0];
  }
}


$solution = new Solution();
$solution->majorityElement([3, 2, 3, 2, 2]);
