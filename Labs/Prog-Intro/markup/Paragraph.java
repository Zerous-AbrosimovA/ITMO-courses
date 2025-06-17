package markup;

import java.util.List;

public class Paragraph implements Markdown {
    private final List<Markdown> list;

    protected Paragraph(List<Markdown> list) {
        for (Markdown elements : list) {
            if (elements instanceof Paragraph) {
                throw new IllegalArgumentException();
            }
        }
        this.list = list;
    }

    @Override
    public void toMarkdown(StringBuilder sb) {
        for (Markdown markdown : list) {
            markdown.toMarkdown(sb);
        }
    }

    @Override
    public void toTypst(StringBuilder sb) {
        for (Markdown markdown : list) {
            markdown.toTypst(sb);
        }
    }
}
