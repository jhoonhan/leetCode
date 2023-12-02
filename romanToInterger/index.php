<?php

class Solution
{

  /**
   * @param String $s
   * @return Integer
   */

  //    I             1
  // V             5
  // X             10
  // L             50
  // C             100
  // D             500
  // M             1000

  private $chars = [
    'I' => 1,
    'V' => 5,
    'X' => 10,
    'L' => 50,
    'C' => 100,
    'D' => 500,
    'M' => 1000
  ];

  function romanToInt($s)
  {
    $acc = 0;
    $prevKeep = false;

    for ($i = strlen($s) - 1; $i >= 0; $i--) {
      $curr = $this->chars[$s[$i]];
      $next = $this->chars[$s[$i - 1]];
      if ($i === 0) {
        $next = NAN;
      }
      $val = 0;

      if ($next >= $curr) {
        // Same or smaller ex: III || VI
        echo ("$i | A: $acc + $curr = " . $acc + $curr);
        echo ('<br>');
        echo ('<br>');
        $acc += $curr;
        $prevKeep = false;
      } elseif ($next < $curr) {
        // Larger ex: IV
        echo ("$i | B: value = " . $curr - $next);
        echo ('<br>');
        echo ('<br>');
        $val = $curr - $next;
        $acc += $val;
      }

      if ($i === 0 && $prevKeep === false) {
        echo ("$i | Last");
        echo ('<br>');

        $acc += $curr;
      }
    }
    echo ($acc);
    echo ('<br>');

    return $acc;
  }
}

$solution = new Solution();
$solution->romanToInt('MCMXCIV');
