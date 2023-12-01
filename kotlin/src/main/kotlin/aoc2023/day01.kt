package aoc2023

import java.io.File
import kotlin.math.max


/*
* thanks for hacking with me @ Gundy  and @ Rudy <3
* */


class FileReader {
    val inputFile: File
        get() = getFile()

    private fun getFile(): File {
        val dataPath = System.getProperty("user.dir")+
            // File.separator allows it to be read on other devices, like Macs
            File.separator + "data" +
            File.separator + "aoc2023" +
            File.separator + "day01.txt"

        return File(dataPath)
    }
}

val input = FileReader().inputFile.readLines().map { it.trim() }


fun main() {
    solution(input)
    solution2(input)
}

fun solution(input: List<String>) {
    print("Sum of Part A is ${calculateCalibrationSum(input)}")
}

fun solution2(input: List<String>) {

    val alteredInput = input.map { row ->
        var currentIndex = 0
        var modifiedRow = ""
        var foundMatch = true

        while(foundMatch) {
        Regex("one|two|three|four|five|six|seven|eight|nine").find(row, max(currentIndex - 1, 0))?.let { match ->
            if (currentIndex <= match.range.first) modifiedRow += row.substring(currentIndex, match.range.first)
            currentIndex = match.range.last + 1
            modifiedRow += match.value.transformDigit()
            match.value.transformDigit()
        } ?: run {
            foundMatch = false
            modifiedRow += row.substring(currentIndex, row.length)
            }
        }
        modifiedRow
    }
    print("Sum of Part B is ${calculateCalibrationSum(alteredInput)}")
}

fun calculateCalibrationSum(input: List<String>): Int {
    var calibrationSum = 0
    input.forEach {
            row ->
        row.filter { it.isDigit() }.let { digits ->
            calibrationSum += (digits.first().digitToInt() * 10) + digits.last().digitToInt()
        }
    }
    return calibrationSum
}

private fun String.transformDigit(): String {
    return when(this){
        "one" -> "1"
        "two" -> "2"
        "three" -> "3"
        "four" -> "4"
        "five" -> "5"
        "six" -> "6"
        "seven" -> "7"
        "eight" -> "8"
        "nine" -> "9"
        else -> throw RuntimeException("Bad number!")
    }
}
