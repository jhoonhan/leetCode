<?php

declare(strict_types=1);

class Solution
{
  function strStr(string $haystack, string $needle): int
  {
    // O(n^2)
    // for ($i = 0; $i < strlen($haystack); $i++) {
    //   $acc = "";
    //   if ($haystack[$i] === $needle[0]) {
    //     // echo ('<br>');
    //     // echo ("First Letter Match: $haystack[$i] | $needle[0]");
    //     // echo ('<br>');

    //     for ($x = 0; $x < strlen($needle); $x++) {
    //       // $index = $x + $i;
    //       // echo ("Checking: $haystack[$index] | $needle[$x]");
    //       // echo ('<br>');
    //       if ($haystack[$x + $i] === $needle[$x]) {
    //         $acc .= $haystack[$x + $i];
    //         // echo ("ACC updated: $acc");
    //         // echo ('<br>');
    //       }
    //     }
    //     // echo ("FINAL: $acc");
    //     // echo ('<br>');
    //     if ($acc === $needle) {
    //       // echo ("HOOYA");
    //       // echo ($i);
    //       return $i;
    //     }
    //   }
    // }

    // why...?
    for ($i = 0; $i < strlen($haystack) + 1 - strlen($needle); $i++) {
      for ($j = 0; $j < strlen($needle); $j++) {
        if ($haystack[$i + $j] !== $needle[$j]) {
          break;
        }
        if ($j === strlen($needle) - 1) {
          return $i;
        }
      }
    }
    return -1;
  }
}

$solution = new Solution();
$solution->strStr('sadbu', 'sad');
