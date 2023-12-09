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

    $numVal = $this->chars[$strVal];
    echo ("$val / $numVal");
    echo ('<br>');

    if ($counta > 0) {
      if ($autoIterate) {
        for ($i = 0; $i < $counta; $i++) {
          $this->str .= $strVal;
          $this->remainder -= $numVal;
        };
      } else {
        $this->str .= $strVal;
        $this->remainder -= $numVal;
      }
    }
    echo ("Checking for $strVal: $numVal");
    echo ('<br>');
    echo ("COUNTA: $counta | REMAINDER: $this->remainder");
    echo ('<br>');
    echo ('<br>');
  }

  function intToRoman(int $num): string
  {
    $this->remainder = $num;
    $alternator = false;

    foreach (array_reverse($this->chars) as $key => $value) {
      # code...
      $this->check($this->remainder, $key, !$alternator);
    }

    // // Check for M (1000s)
    // $this->check($this->remainder, "M", true);

    // // Check for CM (900s)
    // $this->check($this->remainder, "CM", false);

    // // Check for D (500s)
    // $this->check($this->remainder, "D", true);

    // // Check for CD (400s)
    // $this->check($this->remainder, "CD", false);

    // // Check for C (100s)
    // $this->check($this->remainder, "C", true);

    // // Check for XC (90s)
    // $this->check($this->remainder, "XC", false);

    // // Check for XC (50s)
    // $this->check($this->remainder, "L", true);

    // // Check for XC (40s)
    // $this->check($this->remainder, "XL", false);

    // // Check for XC (10s)
    // $this->check($this->remainder, "X", true);

    // // Check for XC (9s)
    // $this->check($this->remainder, "IX", false);

    // // Check for XC (5s)
    // $this->check($this->remainder, "V", true);

    // // Check for XC (4s)
    // $this->check($this->remainder, "IV", false);

    // // Check for XC (1s)
    // $this->check($this->remainder, "I", true);



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
