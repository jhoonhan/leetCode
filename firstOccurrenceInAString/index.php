<?php

declare(strict_types=1);

class Solution
{
  function strStr(string $haystack, string $needle): int
  {
    for ($i = 0; $i < strlen($haystack); $i++) {
      $acc = "";
      if ($haystack[$i] === $needle[0]) {
        // echo ('<br>');
        // echo ("First Letter Match: $haystack[$i] | $needle[0]");
        // echo ('<br>');

        for ($x = 0; $x < strlen($needle); $x++) {
          $index = $x + $i;
          echo ("Checking: $haystack[$index] | $needle[$x]");
          echo ('<br>');
          if ($haystack[$index] === $needle[$x]) {
            $acc .= $haystack[$index];
            echo ("ACC updated: $acc");
            echo ('<br>');
          }
        }
        echo ("FINAL: $acc");
        echo ('<br>');
        if ($acc === $needle) {
          echo ("HOOYA");
          echo ($i);
          return $i;
        }
      }
    }

    echo ("Failed");
    return -1;
  }
}

$solution = new Solution();
$solution->strStr('a', 'a');
