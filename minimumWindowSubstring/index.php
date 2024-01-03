<?php

declare(strict_types=1);

class Solution
{
  function minWindow(string $s, string $t): string
  {
    if ($t === "" || strlen($t) > strlen($s)) {
      return "";
    }

    // Create hashmap
    $countT = array_fill_keys(str_split($t), 0);
    foreach (str_split($t) as $value) {
      $countT[$value]++;
    }

    $have = 0;
    $need = count($countT);
    $res = [-1, -1];
    $resLen = strlen($s) + 1;
    $l = 0;
    for ($r = 0; $r < strlen($s); $r++) {
      $curr = $s[$r];
      if (array_key_exists($curr, $countT)) {
        $window[$curr] = 1 + ($window[$curr] ?? 0);
      }

      if (array_key_exists($curr, $countT) && $window[$curr] === $countT[$curr]) {
        $have++;
      }


      while ($have === $need) {
        if (($r - $l + 1) < $resLen) {
          $res = [$l, $r];
          $resLen = ($r - $l + 1);
        }
        if (array_key_exists($s[$l], $countT)) {
          $window[$s[$l]]--;
        }
        if (array_key_exists($s[$l], $countT) && $window[$s[$l]] < $countT[$s[$l]]) {
          $have--;
        }
        $l++;
      }
    };

    if ($res[0] >= 0 && $res[1] >= 0) {
      return implode('', array_slice(str_split($s), $res[0], $resLen));
    } else {
      return "";
    }
  }
}

$solution = new Solution();
// $solution->minWindow("abc", "b");
$solution->minWindow("a", "b");
