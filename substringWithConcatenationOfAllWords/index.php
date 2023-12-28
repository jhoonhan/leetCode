<?php

declare(strict_types=1);

class Solution
{


  function findSubstring(string $s, array $words): array
  {
    $wordLegnth = strlen($words[0]);
    $success = [];


    for ($i = 0; $i <= strlen($s) - ($wordLegnth * count($words)); $i++) {
      // Check first 3
      $substr = substr($s, $i, $wordLegnth);


      // echo ("$i :: $substr");
      // echo ('<br>');

      // If yes
      $brute = $words;
      if (in_array($substr, $brute)) {
        for ($j = $i; $j <= ($wordLegnth * count($words)) + $i; $j += $wordLegnth) {
          # code...
          echo ($j);
          echo (" | ");
          echo ($wordLegnth * count($words) + $wordLegnth);


          echo ('<br>');

          $nextWord = substr($s, $j, $wordLegnth);
          echo ("$i-$j :: $nextWord");
          echo ('<br>');
          echo (json_encode($brute));
          echo ('<br>');
          var_dump(in_array($nextWord, $brute));



          $key = array_search($nextWord, $brute);
          if (in_array($nextWord, $brute)) {
            echo ("AANG");
            echo ('<br>');
            unset($brute[$key]);
            echo (json_encode($brute));
            echo ('<br>');
            if (count($brute) === 0) {
              echo ("SUCCESS!");
              echo ('<br>');
              $success[] = $i;
              break;
            }
          } else {
            // echo ("Moving On");
            echo ('<br>');
            echo ('<br>');
            break;
          }
        }
      }
      // If no
      else {
        // echo ("Moving On");
        echo ('<br>');
        echo ('<br>');
      }
    }


    echo (json_encode($success));
    echo ('<br>');

    return $success;
  }
}

$solution = new Solution();
$solution->findSubstring("barfoothefoobarman", ["foo", "bar"]);
// $solution->findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]);
