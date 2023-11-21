<?php

declare(strict_types=1);

class Solution
{

  /**
   * @param Integer[] $nums
   * @param int $k
   * @return NULL
   */
  function rotate(&$nums, $k)
  {
    $k = $k % count($nums);

    $l = 0;
    $r = count($nums) - 1;
    $nums = $this->reverseArr($nums, $l, $r);

    $l = 0;
    $r = $k - 1;
    $nums = $this->reverseArr($nums, $l, $r);

    $l = $k;
    $r = count($nums) - 1;
    $nums = $this->reverseArr($nums, $l, $r);
  }

  function reverseArr(array $nums, int $l, int $r): array
  {
    while ($l < $r) {
      $temp = $nums[$l];
      $nums[$l] = $nums[$r];
      $nums[$r] = $temp;
      $l++;
      $r--;
    }
    return $nums;
  }
}
