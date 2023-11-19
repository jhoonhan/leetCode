<?php

declare(strict_types=1);

class Solution
{

  /**
   * @param Integer[] $nums
   * @return Integer
   */
  function removeDuplicates(&$nums)
  {
    /** 
     * @var int|null $prev
     */
    $k = 0;
    $prev = null;
    $double = false;
    for ($i = 0; $i < count($nums); $i++) {
      if ($nums[$i] !== $prev) {
        $nums[$k] = $nums[$i];
        $k++;
        $double = false;
      }
      if ($nums[$i] === $prev && !$double) {
        $nums[$k] = $nums[$i];
        $k++;
        $double = true;
      }
      $prev = $nums[$i];
    }
    return $k;
  }
}


$solution = new Solution();

$nums = [1, 1, 2];
$solution->removeDuplicates($nums);
