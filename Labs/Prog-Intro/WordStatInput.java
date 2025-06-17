import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;

public class WordStatInput {
    public static void main(String[] args) {
        Map<String, Integer> wordsAndCount = new LinkedHashMap<>();
        StringBuilder str = new StringBuilder();
        int ch;
        try {
            MyScanner sc = new MyScanner(args[0], "UTF-8");
            try {
                while (sc.hasNextChar()) {
                    char currentChar = sc.nextChar();
                    if (Character.isLetter(currentChar) ||
                            Character.getType(currentChar) == Character.DASH_PUNCTUATION ||
                            currentChar == '\'') {
                        str.append(Character.toLowerCase(currentChar));
                    } else {
                        if (str.length() > 0) {
                            if (wordsAndCount.containsKey(str.toString())) {
                                wordsAndCount.put(str.toString(), wordsAndCount.get(str.toString()) + 1);
                            } else {
                                wordsAndCount.put(str.toString(), 1);
                            }
                        }
                        str.setLength(0);
                    }
                }
                if (str.length() > 0) {
                    if (wordsAndCount.containsKey(str.toString())) {
                        wordsAndCount.put(str.toString(), wordsAndCount.get(str.toString()) + 1);
                    } else {
                        wordsAndCount.put(str.toString(), 1);
                    }
                }
                str.setLength(0);
            } finally {
                sc.close();
            }
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }

        try {
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(
                    new FileOutputStream(args[1]), StandardCharsets.UTF_8
            ), 1024);
            try {
                for (Map.Entry<String, Integer> entry : wordsAndCount.entrySet()) {
                    bw.write(entry.getKey() + " " + entry.getValue() + "\n");
                }
            } finally {
                bw.close();
            }
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }
}