<?php

declare(strict_types=1);

class Solution
{
    function rotate(array &$matrix): array
    {
        for ($i = count($matrix) - 1; $i <= 0; $i--) {
            echo ($i);
            echo ('<br>');
        }


        return [];
    }
}


$solution = new Solution();
$solution->rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
