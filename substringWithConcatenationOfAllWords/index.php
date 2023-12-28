<?php

declare(strict_types=1);

class Solution
{


  function findSubstring(string $s, array $words): array
  {
    $wordLegnth = strlen($words[0]);
    $success = [];


    for ($i = 0; $i < strlen($s) - ($wordLegnth * count($words)); $i++) {
      // Check first 3
      $substr = substr($s, $i, 3);


      echo ("$i :: $substr");
      echo ('<br>');

      // If yes

      $aleady = [];
      if (in_array($substr, $words)) {
        $counter = $i;
        foreach ($words as $word) {
          $nextWord = substr($s, $counter, 3);
          if (in_array($nextWord, $words) && !in_array($nextWord, $aleady)) {
            $aleady[] = $nextWord;
            $counter += $wordLegnth;
          } else {
            echo ("Moving On");
            echo ('<br>');
            echo ('<br>');
            break;
          }

          if (count($aleady) === count($words)) {
            echo ('<br>');
            echo ('<br>');
            echo ('<br>');
            echo ("SUCCESS with counter: $i");
            $success[] = $i;

            echo ('<br>');
            echo ('<br>');
            echo ('<br>');
          }
        }
      }
      // If no
      else {
        echo ("Moving On");
        echo ('<br>');
        echo ('<br>');
      }
    }


    echo (json_encode($success));
    echo ('<br>');

    return [0, 0];
  }
}

$solution = new Solution();
// $solution->findSubstring("barfoothefoobarman", ["foo", "bar"]);
$solution->findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]);
