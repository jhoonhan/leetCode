<?php

declare(strict_types=1);

class Solution
{
  function strStr(string $haystack, string $needle): int
  {
    $acc = "";
    $i = 0;
    $j = 0;
    while ($j < strlen($needle) && $i < strlen($haystack)) {
      if ($haystack[$i] === $needle[$j]) {
        $acc .= $haystack[$i];
        $j++;
      } else {
        $acc = "";
        $j = 0;
      }

      if ($acc === $needle) {
        return $i - (strlen($needle) - 1);
      }

      $i++;
    }
  }
}

$solution = new Solution();
$solution->strStr('sadbutsad', 'sad');
