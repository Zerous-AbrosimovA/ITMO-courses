package markup;

import java.util.List;

public abstract class AbstractMarkdown implements Markdown {
    private final List<Markdown> list;

    AbstractMarkdown(List<Markdown> list) {
        this.list = list;
    }

    public void toMarkdown(StringBuilder sb, String markdownElement) {
        sb.append(markdownElement);
        for (Markdown markdown : list) {
            markdown.toMarkdown(sb);
        }
        sb.append(markdownElement);
    }

    public void toTypst(StringBuilder sb, String typstElementStart) {
        sb.append(typstElementStart);
        for (Markdown markdown : list) {
            markdown.toTypst(sb);
        }
        sb.append("]");
    }
}
