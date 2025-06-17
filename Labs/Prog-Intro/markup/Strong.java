package markup;

import java.util.List;

public class Strong extends AbstractMarkdown {
    protected Strong(List<Markdown> list) {
        super(list);
    }

    @Override
    public void toMarkdown(StringBuilder sb) {
        super.toMarkdown(sb, "__");
    }

    @Override
    public void toTypst(StringBuilder sb) {
        super.toTypst(sb, "#strong[");
    }
}
