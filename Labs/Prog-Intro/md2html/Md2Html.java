package md2html;

public class Md2Html {
    public static void main(String[] args) {
        Parser parser = new Parser();
        parser.getFile(args[0], args[1]);
    }
}
