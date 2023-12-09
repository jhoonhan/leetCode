<?php

declare(strict_types=1);

class Solution
{
  function lengthOfLastWord(string $s): int
  {
    $splittedString = explode(' ', trim($s));
    return strlen(end($splittedString));
  }
}


$solution = new Solution();
$solution->lengthOfLastWord("   fly me   to   the moon  ");
