import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.stream.Collectors;

public class AOC {
    static ArrayList<String> readFile() {
        ArrayList<String> myList = new ArrayList<String>();
        try {
            File myObj = new File("2.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                myList.add(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        } finally {
            return myList;
        }
    }

    public static void main(String[] args) {
        ArrayList<String> lines = readFile();
        int totalArea = 0;
        int totalRibbon = 0;
        for (String line: lines) {
            List<String> lineArr = Arrays.asList(line.split("x", 0));
            List<Integer> parsedNumbers = new ArrayList<Integer>();
            for(String number : lineArr) {
                parsedNumbers.add(Integer.parseInt(number));
            }
            parsedNumbers = parsedNumbers
                .stream().sorted().collect(Collectors.toList());
            int ribbonFirst = (2 * parsedNumbers.get(0)) + (2 * parsedNumbers.get(1));
            int ribbonSecond = parsedNumbers.stream().reduce(1, (a, b) -> a * b);
            totalRibbon += ribbonFirst + ribbonSecond;
            int first = parsedNumbers.get(0) * parsedNumbers.get(1);
            int second = parsedNumbers.get(2) * parsedNumbers.get(1);
            int third = parsedNumbers.get(0) * parsedNumbers.get(2);
            int slack = Math.min(Math.min(first, second), third);
            totalArea += 2 * (first + second + third) + slack;
        }
        System.out.println("Part 1: " + totalArea);
        System.out.println("Part 2: " + totalRibbon);
    }
}
