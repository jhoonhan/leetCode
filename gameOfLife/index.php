<?php

declare(strict_types=1);
class Solution
{
    protected function countNei($board, $i, $j)
    {

        $acc = 0;
        // TL
        if (isset($board[$i - 1][$j - 1])) {
            if ($board[$i - 1][$j - 1] === 1 || $board[$i - 1][$j - 1] === 3) {
                $acc += 1;
            }
        }
        // T
        if (isset($board[$i - 1][$j])) {
            if ($board[$i - 1][$j] === 1 || $board[$i - 1][$j] === 3) {
                $acc += 1;
            }
        }
        // TR
        if (isset($board[$i - 1][$j + 1])) {
            if ($board[$i - 1][$j + 1] === 1 || $board[$i - 1][$j + 1] === 3) {
                $acc += 1;
            }
        }
        // L
        if (isset($board[$i][$j - 1])) {
            if ($board[$i][$j - 1] === 1 || $board[$i][$j - 1] === 3) {
                $acc += 1;
            }
        }
        // R

        if (isset($board[$i][$j + 1])) {
            if ($board[$i][$j + 1] === 1 || $board[$i][$j + 1] ===   3) {
                $acc += 1;
            }
        }
        // BL
        if (isset($board[$i + 1][$j - 1])) {
            if ($board[$i + 1][$j - 1] === 1 || $board[$i + 1][$j - 1] === 3) {
                $acc += 1;
            }
        }
        // B
        if (isset($board[$i + 1][$j])) {
            if ($board[$i + 1][$j] === 1 || $board[$i + 1][$j] === 3) {
                $acc += 1;
            }
        }
        // BR
        if (isset($board[$i + 1][$j + 1])) {
            if ($board[$i + 1][$j + 1] === 1 || $board[$i + 1][$j + 1] === 3) {
                $acc += 1;
            }
        }
        return $acc;
    }
    function gameOfLife(array &$board)
    {
        //  ORG     New     State
        //  0       0       0
        //  1       0       1
        //  0       1       2
        //  1       1       3
        for ($i = 0; $i < count($board); $i++) {
            for ($j = 0; $j < count($board[0]); $j++) {
                $currVal = $board[$i][$j];
                $nei = $this->countNei($board, $i, $j);
                if ($currVal !== 0) {
                    if ($nei === 2 || $nei === 3) {
                        $board[$i][$j] = 3;
                    }
                } elseif ($nei == 3) {
                    $board[$j][$i] = 2;
                }
            }
        }
        for ($i = 0; $i < count($board); $i++) {
            for ($j = 0; $j < count($board[0]); $j++) {
                if ($board[$i][$j] === 1) {
                    $board[$i][$j] = 0;
                } elseif ($board[$i][$j] === 2) {
                    $board[$i][$j] = 1;
                } elseif ($board[$i][$j] === 3) {
                    $board[$i][$j] = 1;
                }
            }
        }
        echo (json_encode($board));
        echo ('<br>');
    }
}
$solution = new Solution();
$aang = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]];
$solution->gameOfLife($aang);
