package markup;

public class Text implements Markdown {
    private final String strings;

    protected Text(String strings) {
        this.strings = strings;
    }

    @Override
    public void toMarkdown(StringBuilder sb) {
        sb.append(strings);
    }

    @Override
    public void toTypst(StringBuilder sb) {
        sb.append(strings);
    }
}
