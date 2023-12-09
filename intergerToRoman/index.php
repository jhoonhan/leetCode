<?php

declare(strict_types=1);


// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000

// I can be placed before V (5) and X (10) to make 4 and 9. 
// X can be placed before L (50) and C (100) to make 40 and 90. 
// C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution
{

  private $chars = [
    'I' => 1,
    'IV' => 4,
    'V' => 5,
    'IX' => 9,
    'X' => 10,
    'XL' => 40,
    'L' => 50,
    'XC' => 90,
    'C' => 100,
    'CD' => 400,
    'D' => 500,
    'CM' => 900,
    'M' => 1000
  ];
  private $str = "";
  private $remainder = 0;

  function check(int $val, string $strVal, bool $autoIterate): void
  {
    $counta = (int) ($val / $this->chars[$strVal]);
    // echo ("$val / $numVal");
    // echo ('<br>');

    if ($counta > 0) {
      if ($autoIterate) {
        for ($i = 0; $i < $counta; $i++) {
          $this->str .= $strVal;
          $this->remainder -= $this->chars[$strVal];
        };
      } else {
        $this->str .= $strVal;
        $this->remainder -= $this->chars[$strVal];
      }
    }
    // echo ("Checking for $strVal: $numVal");
    // echo ('<br>');
    // echo ("COUNTA: $counta | REMAINDER: $this->remainder");
    // echo ('<br>');
    // echo ('<br>');
  }

  function intToRoman(int $num): string
  {
    $this->remainder = $num;
    $alternator = false;

    foreach (array_reverse(array_keys($this->chars)) as $key) {
      $this->check($this->remainder, $key, !$alternator);
    }



    // Check for L (50s)
    // echo ('<br>');
    // echo ('<br>');
    // echo ("Result:");
    // echo ('<br>');
    // echo ("$this->str | $num");
    return $this->str;
  }
}

$solution = new Solution();
$solution->intToRoman(3999);
