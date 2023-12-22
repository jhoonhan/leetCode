<?php

declare(strict_types=1);


class Solution
{

  /**
   * @param String $s
   * @param String $t
   * @return Boolean
   */
  function isSubsequence($s, $t)
  {
    $i = 0;
    $j = 0;

    while ($j < strlen($t) && $i < strlen($s)) {
      if ($s[$i] === $t[$j]) {
        $i++;
      }
      $j++;
    }

    if ($i < strlen($s)) {
      return false;
    } else {
      return true;
    }
  }
}

$solution = new Solution();
$solution->isSubsequence("axcc", "ahbgdc");
