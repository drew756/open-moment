# Figure

A Figure is a number with its receipt: an eyebrow saying what is counted, the count in the data face, a breakdown of what it is made of, and a source line naming the report, the date and the statute it is published under.

## Use it for

The Cage Clock, legislator cage counts, county cards, any statistic that will be screenshotted and shared. If a number appears on its own anywhere public, it should be a Figure.

## Rules

- The count is set in `figure` (JetBrains Mono 700, tabular) in `ink`. Dollar figures use `gold`; death counts use `alert`.
- The eyebrow is `label`, uppercase, in `ink-muted`.
- The breakdown on the right follows the rule in Visual language: the whole in `violet`, real proportions, one path of subdivision ending on a `magenta` square. Each piece is labeled with a `data` style caption when space allows.
- The source line is `small` in `ink-muted` and is mandatory. The consumer provides the report name, the date and the citation; the component does not invent one.
- Aggregates only. The component never renders a name, a case number or a photograph.
