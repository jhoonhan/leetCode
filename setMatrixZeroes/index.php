<?php

declare(strict_types=1);

class Solution
{
    /**
     * @param Integer[][] $matrix
     * @return NULL
     */
    function setZeroes(&$matrix)
    {
        $rows = [];
        $cols = [];
        for ($row = 0; $row < count($matrix); $row++) {
            for ($col = 0; $col < count($matrix); $col++) {
                if ($matrix[$row][$col] === 0) {
                    $rows[] = $row;
                    $cols[] = $col;
                }
            }
        }
        echo (json_encode($rows));
        echo ('<br>');
        echo (json_encode($cols));
    }
}

$solution = new Solution();
$solution->setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]);
