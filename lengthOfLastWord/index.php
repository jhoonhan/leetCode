<?php

declare(strict_types=1);

class Solution
{


  function lengthOfLastWord(string $s): int
  {
    $splittedString = explode(" ", $s);
    print_r($splittedString);


    return 0;
  }
}


$solution = new Solution();
$solution->lengthOfLastWord("aaang 12345");
