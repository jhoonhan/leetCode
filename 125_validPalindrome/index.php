<?php

declare(strict_types=1);

class Solution
{
  function isPalindrome(string $s): bool
  {
    $newStr = strtolower(preg_replace("/[^a-zA-Z0-9]/", "", $s));

    $i = 0;
    $j = strlen($newStr) - 1;

    while ($i < strlen($s) && $j >= 0) {
      if ($newStr[$i] !== $newStr[$j]) {
        return false;
      }
      $i++;
      $j--;
    }

    return true;
  }
}

$solution = new Solution();
$solution->isPalindrome('race a car');
