package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func readCsvFile(filePath string) [][]string {
	f, err := os.Open(filePath)
	if err != nil {
		log.Fatal("Unable to read input file "+filePath, err)
	}
	defer f.Close()

	csvReader := csv.NewReader(f)
	csvReader.Comma = ';'
	records, err := csvReader.ReadAll()
	if err != nil {
		log.Fatal("Unable to parse file as CSV for "+filePath, err)
	}

	return records
}

func arraySort(array []int) []int {
	sort.Slice(array, func(i, j int) bool {
		return array[i] < array[j]
	})
	return array
}

func positiveDiff(a int, b int) int {
	if a > b {
		return a - b
	} else {
		return b - a
	}
}

func main() {
	fmt.Println("Application is starting...")
	records := readCsvFile("../data.csv")

	var firstArray []int
	var secondArray []int

	for _, el := range records {
		first, _ := strconv.Atoi(el[0])
		second, _ := strconv.Atoi(el[1])
		firstArray = append(firstArray, first)
		secondArray = append(secondArray, second)
	}

	firstArray = arraySort(firstArray)
	secondArray = arraySort(secondArray)

	diffBetweenArrays := 0
	for index, _ := range firstArray {
		diffBetweenArrays += positiveDiff(firstArray[index], secondArray[index])
	}

	fmt.Println(diffBetweenArrays)
}
