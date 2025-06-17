package md2html;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Map;

public class Parser {
    private final int BUFFERSIZE = 2048;
    private boolean hasNextParagraph;
    private boolean endLevel;
    private int start;
    private final StringBuilder sb = new StringBuilder();
    private final StringBuilder counter = new StringBuilder();
    private final Map<String, String> markdownStartSymbols = Map.of(
            "*", "<em>",
            "_", "<em>",
            "`", "<code>",
            "**", "<strong>",
            "__", "<strong>",
            "--", "<s>",
            "~", "<mark>");
    private final Map<String, String> markdownEndSymbols = Map.of(
            "*", "</em>",
            "_", "</em>",
            "`", "</code>",
            "**", "</strong>",
            "__", "</strong>",
            "--", "</s>",
            "~", "</mark>");
    private final Map<String, String> htmlSymbols = Map.of(
            "<", "&lt;",
            ">", "&gt;",
            "&", "&amp;");

    public void getFile(String inputFileName, String outputFileName) {
        try {
            try (BufferedReader br = new BufferedReader(new InputStreamReader(
                    new FileInputStream(inputFileName), StandardCharsets.UTF_8), BUFFERSIZE); BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(
                    new FileOutputStream(outputFileName), StandardCharsets.UTF_8), BUFFERSIZE)) {
                String line;
                while ((line = br.readLine()) != null) {
                    if (!sb.isEmpty() && !line.isEmpty()) sb.append(System.lineSeparator());
                    parseLine(line);
                    if (hasNextParagraph && !sb.isEmpty()) {
                        findStartSymbols();
                        bw.write(sb.toString());
                        sb.setLength(0);
                    }
                }
                hasNextParagraph = true;
                closeStringBuilder("");
                findStartSymbols();
                bw.write(sb.toString());
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    private void parseLine(String line) {
        StringBuilder tempSB = new StringBuilder();
        if (line.isEmpty() && !hasNextParagraph) {
            hasNextParagraph = true;
            endLevel = false;
            closeStringBuilder(tempSB.toString());
            return;
        } else if (line.isEmpty()) return;
        hasNextParagraph = false;
        openStringBuilder(line);
        tempSB.append(text(line));
        closeStringBuilder(tempSB.toString());
    }

    private StringBuilder text(String line) {
        StringBuilder tempSB = new StringBuilder();
        for (int i = start; i < line.length(); i++) {
            if (htmlSymbols.containsKey(Character.toString(line.charAt(i)))) {
                tempSB.append(htmlSymbols.get(Character.toString(line.charAt(i))));
                continue;
            }
            tempSB.append(line.charAt(i));
            start = 0;
        }
        return tempSB;
    }

    private void openStringBuilder(String line) {
        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) == '#' && !endLevel) {
                counter.append('#');
            } else if (!counter.isEmpty() && Character.isWhitespace(line.charAt(i)) && !endLevel) {
                sb.append("<h").append(counter.length()).append(">");
                start = counter.length() + 1;
                endLevel = true;
                break;
            } else if ((line.charAt(0) != '#' && !endLevel) ||
                    (!counter.isEmpty() && !Character.isWhitespace(line.charAt(i)) && !endLevel)) {
                sb.append("<p>");
                start = counter.length();
                sb.append(counter);
                counter.setLength(0);
                endLevel = true;
                break;
            }
        }
    }

    private void closeStringBuilder(String line) {
        if (!counter.isEmpty() && hasNextParagraph) {
            sb.append(line).append("</h").append(counter.length()).append(">").append(System.lineSeparator());
            counter.setLength(0);
        } else if (hasNextParagraph && !sb.isEmpty()) sb.append(line).append("</p>").append(System.lineSeparator());
        else sb.append(line);
    }

    private void findStartSymbols() {
        int startSymbolPose = 0;
        boolean isProtected = false;
        String symbol;
        while (startSymbolPose < sb.length()) {
            if (Character.toString(sb.charAt(startSymbolPose)).equals("\\")) {
                sb.replace(startSymbolPose, startSymbolPose + 1, "");
                isProtected = true;
                startSymbolPose++;
                continue;
            } else if (startSymbolPose + 1 < sb.length()
                    && markdownStartSymbols.containsKey(Character.toString(sb.charAt(startSymbolPose)) + sb.charAt(startSymbolPose + 1))
                    && !isProtected) {
                symbol = Character.toString(sb.charAt(startSymbolPose)) + (sb.charAt(startSymbolPose));
                startSymbolPose = replaceHTML(startSymbolPose, symbol, 2);
            } else if (markdownStartSymbols.containsKey(Character.toString(sb.charAt(startSymbolPose)))
                    && !isProtected) {
                symbol = Character.toString(sb.charAt(startSymbolPose));
                startSymbolPose = replaceHTML(startSymbolPose, symbol, 1);
            }
            startSymbolPose++;
            isProtected = false;
        }
    }

    private int findLastSymbols(String Symbol, int startSymbolPose) {
        int endSymbolPosition = 0;
        while (startSymbolPose < sb.length()) {
            if (startSymbolPose + 1 < sb.length()
                    && (Character.toString(sb.charAt(startSymbolPose)) + sb.charAt(startSymbolPose + 1)).equals(Symbol)) {
                endSymbolPosition = startSymbolPose;
                break;
            } else if (Character.toString(sb.charAt(startSymbolPose)).equals(Symbol)) {
                if (!Character.toString(sb.charAt(startSymbolPose - 1)).equals("\\")) {
                    if (startSymbolPose + 1 < sb.length()
                            && (Character.toString(sb.charAt(startSymbolPose)) + sb.charAt(startSymbolPose + 1)).equals(Symbol + Symbol)) {
                        startSymbolPose += 2;
                        continue;
                    }
                    endSymbolPosition = startSymbolPose;
                    break;
                } else {
                    startSymbolPose += 2;
                    continue;
                }
            }
            startSymbolPose++;
        }
        return endSymbolPosition;
    }

    private int replaceHTML(int startSymbolPose, String symbol, int index) {
        int endSymbolPose;
        endSymbolPose = findLastSymbols(symbol, startSymbolPose + 1);
        if (endSymbolPose > 0) {
            sb.replace(startSymbolPose, startSymbolPose + index, markdownStartSymbols.get(symbol));
            sb.replace(endSymbolPose + markdownEndSymbols.get(symbol).length() - (index + 1),
                    endSymbolPose + markdownEndSymbols.get(symbol).length() - 1,
                    markdownEndSymbols.get(symbol));
            startSymbolPose += 2;
        }
        return startSymbolPose;
    }
}