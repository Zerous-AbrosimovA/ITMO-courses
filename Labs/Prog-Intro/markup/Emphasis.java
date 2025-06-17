package markup;

import java.util.List;

public class Emphasis extends AbstractMarkdown {
    protected Emphasis(List<Markdown> list) {
        super(list);
    }

    @Override
    public void toMarkdown(StringBuilder sb) {
        super.toMarkdown(sb, "*");
    }

    @Override
    public void toTypst(StringBuilder sb) {
        super.toTypst(sb, "#emph[");
    }
}
