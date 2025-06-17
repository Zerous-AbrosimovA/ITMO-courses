import java.io.*;

public class MyScanner {
    private final Reader reader;
    private final char[] buffer = new char[1024];
    private int position = 0;
    private int read = 0;

    public MyScanner(String fileName, String fileEncoding) throws IOException {
        this.reader = new InputStreamReader(new FileInputStream(fileName), fileEncoding);
    }

    public MyScanner(String input) throws IOException {
        this.reader = new StringReader(input);
    }

    public MyScanner() throws IOException {
        this.reader = new InputStreamReader(System.in);
    }

    private boolean fillBuffer() throws IOException {
        if (position >= read) {
            read = reader.read(buffer);
            position = 0;
        }
        return read > 0;
    }

    public boolean hasNext() throws IOException {
        if (!fillBuffer()) {
            return false;
        }
        while (Character.isWhitespace(buffer[position])) {
            position++;
            if (!fillBuffer()) {
                return false;
            }
        }
        return true;
    }

    public boolean hasNextInt() throws IOException {
        if (!fillBuffer()) {
            return false;
        }
        while (Character.isWhitespace(buffer[position])) {
            position++;
            if (!fillBuffer()) {
                return false;
            }
        }
        return Character.isDigit(buffer[position]) || buffer[position] == '-' || buffer[position] == '+';
    }

    public String next() throws IOException {
        StringBuilder sb = new StringBuilder();
        if (hasNext()) {
            while (!Character.isWhitespace(buffer[position])) {
                sb.append(buffer[position++]);
                if (!fillBuffer()) {
                    break;
                }
            }
        }
        return sb.toString();
    }

    public int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    public String nextLine() throws IOException {
        if (!fillBuffer()) {
            throw new IOException();
        }
        StringBuilder sb = new StringBuilder();
        while (position < buffer.length) {
            if (buffer[position] == System.lineSeparator().charAt(0)) {
                StringBuilder tempStringBuilder = new StringBuilder();
                while (position < buffer.length) {
                    tempStringBuilder.append(buffer[position++]);
                    if (tempStringBuilder.toString().equals(System.lineSeparator())) {
                        return sb.toString();
                    } else if (tempStringBuilder.length() >= System.lineSeparator().length()) {
                        break;
                    }
                    if (!fillBuffer()) {
                        return tempStringBuilder.toString();
                    }
                }
                sb.append(tempStringBuilder);
                if (!fillBuffer()) {
                    return sb.toString();
                }
            }
            sb.append(buffer[position++]);
            if (!fillBuffer()) {
                return sb.toString();
            }
        }
        return sb.toString();
    }

    public char nextChar() throws IOException {
        if (fillBuffer()) {
            return buffer[position++];
        }
        throw new IOException();
    }

    public boolean hasNextChar() throws IOException {
        return fillBuffer();
    }

    public boolean hasNextLine() throws IOException {
        return fillBuffer();
    }

    public void close() throws IOException {
        reader.close();
    }
}