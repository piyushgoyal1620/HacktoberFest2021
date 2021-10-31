package main

import (
	"fmt"
)

//https://leetcode.com/problems/stone-game/
func main() {
	fmt.Println(stoneGame([]int{3, 2, 10, 4}))
}

func stoneGame(piles []int) bool {
	var alexScore, leeScore int
	var i, j int

	j = len(piles) - 1
	numOfLooping := 0
	for {
		if numOfLooping == len(piles) {
			break
		}
		var currentScore int
		if piles[i] > piles[j] {
			currentScore = piles[i]
			i++
		} else {
			currentScore = piles[j]
			j--
		}
		if numOfLooping%2 == 0 {
			alexScore += currentScore
		} else {
			leeScore += currentScore
		}
		numOfLooping++
	}

	return alexScore > leeScore
}
