import java.util.HashSet;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Cbic {
    public static void main(String[] args) {
        String input1 = "The UN was established on 12-05-1945 and Chile joined on 12-05-1950";
        String input2 = "The UN was established on 12-05-1945 and Chile joined on 12-05-1945";
        String input3 = "The year is 12-01-1949 11-01-1949";
        
        System.out.println(countUniqueYears(input1));  // Output: 2
        System.out.println(countUniqueYears(input2));  // Output: 1
        System.out.println(countUniqueYears(input3));  // Output: 1
    }

    public static int countUniqueYears(String input) {
        Set<String> uniqueYears = new HashSet<>();
        String regex = "\\b\\d{1,2}-\\d{1,2}-(\\d{4})\\b";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(input);

        while (matcher.find()) {
            uniqueYears.add(matcher.group(1));
        }

        return uniqueYears.size();
    }
}
