<?php

declare(strict_types=1);

class Solution
{
  function longestCommonPrefix(array $strs): string
  {
    $prefix = "";
    $i = 0;
    while (true) {
      $prev = "";
      $tempPrefix = "";
      foreach ($strs as $str) {
        if ($prev === "" || $prev === $str[$i]) {
          $prev = $str[$i];
          $tempPrefix .= $str[$i];
        }
      }
      if (strlen($tempPrefix) === count($strs)) {
        $prefix .= $str[$i];
        $i++;
      } else {
        return $prefix;
      }
    }
  }
}


$solution = new Solution();
$solution->longestCommonPrefix(["flower", "flow", "flight"]);
// $solution->longestCommonPrefix(["flower", "flow", "flight", "aaang"]);
