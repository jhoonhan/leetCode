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

  $chart = [
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
  }
}

$solution = new Solution();
$solution->romanToInt('III');
