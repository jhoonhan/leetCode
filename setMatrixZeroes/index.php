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
            for ($col = 0; $col < count($matrix[0]); $col++) {
                if ($matrix[$row][$col] === 0) {
                    $rows[] = $row;
                    $cols[] = $col;
                }
            }
        }

        for ($row = 0; $row < count($matrix); $row++) {
            for ($col = 0; $col < count($matrix[0]); $col++) {
                if (in_array($row, $rows) || in_array($col, $cols)) {
                    $matrix[$row][$col] = 0;
                }
            }
        }
    }
}

$solution = new Solution();
$matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]];
$solution->setZeroes($matrix);
