<?php

declare(strict_types=1);


class Solution
{
  function reverseWords(string $s): string
  {
    $trimmed = preg_replace('/\s+/', ' ', trim($s));
    $exploded = explode(" ", $trimmed);
    $imploded = join(" ", array_reverse($exploded));
    return trim($imploded);
  }
}


$solution = new Solution();
$solution->reverseWords("a good   example");
