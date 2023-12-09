<?php

class Solution
{

  /**
   * @param String $s
   * @return Integer
   */


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

    $i = strlen($s) - 1;
    // while ($i >= 0) {
    for ($i = 0; $i < strlen($s); $i++) {
      $chars = $this->chars;
      $curr = $chars[$s[$i]];
      if ($i + 1 < strlen($s) && $curr < $chars[$s[$i + 1]]) {
        $acc -= $curr;
      } else {
        $acc += $curr;
      }
    }

    return $acc;
  }
}

$solution = new Solution();
// $solution->romanToInt('MCMXCIV');
// $solution->romanToInt('IV');
$solution->romanToInt('LVIII');

  // I             1
  // V             5
  // X             10
  // L             50
  // C             100
  // D             500
  // M             1000