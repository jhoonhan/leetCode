<?php

declare(strict_types=1);



class Solution
{
  function threeSum(array $nums): array
  {
    sort($nums);
    $res = [];
    for ($i = 0; $i < count($nums); $i++) {
      $l = $i + 1;
      $r = count($nums) - 1;
      if ($i > 0 && $nums[$i] === $nums[$i - 1]) {
        continue;
      }
      while ($l < $r) {
        $target = $nums[$i] + $nums[$l] + $nums[$r];
        if ($target > 0) {
          $r--;
        } elseif ($target < 0) {
          $l++;
        } else {
          $res[] = [$nums[$i], $nums[$l], $nums[$r]];
          $l++;
          while ($nums[$l] === $nums[$l - 1] and $l < $r) {
            $l++;
          }
        }
      }
    }
    return $res;
  }
}

$solution = new Solution();
$solution->threeSum([-1, 0, 1, 2, -1, -4]);
