<?php

declare(strict_types=1);

class Solution
{
  function minWindow(string $s, string $t): string
  {
    $tLength = strlen($t);
    $l = 0;
    $r = $tLength;

    for ($i = 0; $i < strlen($s) - strlen($t); $i++) {
      # code...
    }


    return '';
  }
}

$solution = new Solution();
$solution->minWindow("ADOBECODEBANC", "ABC");
