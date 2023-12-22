<?php

declare(strict_types=1);

class Solution
{
  function twoSum(array $numbers, int $target): array
  {
    $map = array();
    for ($i = 0; $i < count($numbers); $i++) {
      if (isset($map[$target - $numbers[$i]])) {
        return [$map[$target - $numbers[$i]], $i + 1];
      } else {
        $map[$numbers[$i]] = $i + 1;
      }
    }
  }
}


$solution = new Solution();
$solution->twoSum([2, 7, 11, 15], 9);
