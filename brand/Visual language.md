# Visual language: the breakdown

The one drawing the brand owns. A rectangle is a number. Cutting it into pieces is showing what the number is made of. Cutting one of the pieces again is looking closer. Keep cutting and you reach one square, which is one person.

## The rule

1. Start with one block in `violet`. Its area is the whole count.
2. Split it into pieces whose areas match the real proportions of the sub-counts. Four quarters is the default when the data is not yet attached; real data gives real proportions.
3. Choose one piece and split it again. Only one. The eye should follow a single path from the whole to the one.
4. Repeat until the smallest piece is at the limit of the medium: 4px on screen, 1mm in print. That piece is `magenta`. It is the person.
5. Every cut is a `space-1` (4px) gap showing `void`, or a `hairline` rule when the pieces touch. Pieces have `radius-0`.
6. Color the pieces from the slick: `violet` for the largest, `green` and `magenta` for the sheen, `surface-raised` for the quiet piece. `gold` only when the piece is a dollar amount. `alert` only when the piece is a death count.

A breakdown with a label on each piece is a chart. A breakdown with no labels is the pattern. Both are the same drawing.

## Depth

Three levels of subdivision is the minimum for the pattern to read as a fractal; five is the practical maximum before the smallest pieces blur. The cover uses four. A poster can use five. A favicon uses two.

## Where it goes

- The cover and the top of every long document, in the top-right, bleeding off the top and right edges.
- The Cage Clock: the live count on the left, its breakdown on the right, the magenta square ticking when the number changes.
- Legislator cards: a cage count broken down into the bills that built it.
- The receipt QR card in hemp retail: the state count breaking down to the county the shop is in.
- The wordmark, when one is drawn.

## What it is not

- Not a Sierpinski carpet or any other textbook fractal. Those are symmetric; ours follows one path toward one person and is lopsided on purpose.
- Not a treemap in a chart library's default colors. Use the tokens.
- Not a background texture. If the breakdown is behind text it is doing nothing, and text over it fails contrast.

## Motion

The breakdown animates in one way: the whole appears, then it cuts, then one piece cuts, then one piece of that, in `150ms` steps, ending on the magenta square. Nothing else on the page moves. Honor `prefers-reduced-motion` by showing the final state.
