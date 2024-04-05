<?php

declare(strict_types=1);

class Solution
{
    function rotate(&$matrix)
    {
        $l = 0;
        $r = count($matrix) - 1;

        while ($l < $r) {
            for ($i = 0; $i < $r - $l; $i++) {
                $t = $l;
                $b = $r;

                // store tl
                $tl = $matrix[$t][$l + $i];

                // BL to TL
                $matrix[$t][$l + $i] = $matrix[$b - $i][$l];

                // BR to BL
                $matrix[$b - $i][$l] = $matrix[$b][$r - $i];

                // TR to BR
                $matrix[$b][$r - $i] = $matrix[$t + $i][$r];

                // TR to TL
                $matrix[$t + $i][$r] = $tl;
            }
            $r--;
            $l++;
        }
    }
}


$solution = new Solution();
$matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
$solution->rotate($matrix);
