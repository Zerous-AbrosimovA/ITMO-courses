public class Sum {
    public static void main(String[] args) {
        int argsLength = args.length;
        int sum = 0;
        StringBuilder num = new StringBuilder();
        for (int i = 0; i < argsLength; i++) {
            for (int j = 0; j < args[i].length(); j++) {
                if (!Character.isWhitespace(args[i].charAt(j))) {
                    num.append(args[i].charAt(j));
                } else {
                    if (!num.isEmpty()) {
                        sum += Integer.parseInt(num.toString());
                        num.setLength(0);
                    }
                }
            }
            if (!num.isEmpty()) {
                sum += Integer.parseInt(num.toString());
                num.setLength(0);
            }
        }
        System.out.println(sum);
    }
}
