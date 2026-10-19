# Open Moment

Every number is somebody.

Open Moment is an organization built to end the prison system as it exists in the United States, starting in Texas. This is its brand book: the name, the voice, the colors, the type, and the one visual idea everything else is built on.

## The name

The name comes from a night the founder spent in a jail cell in Austin. It was, in his words, an open moment of mind and memory: the cell did not close anything, it opened something. That is the whole brand in one line. A cage is a policy choice, and every one of them holds a person who is still thinking, still remembering, still a whole life.

Write it as two words, both capitalized: **Open Moment**. Never "OpenMoment", never "the Open Moment", never an acronym. In running text it is the organization; in a headline it can be the idea.

## What we are against

We name the enemy, not the victim. The thing we fight is **Big Prison**: the phone vendors, the commissary contracts, the bail bondsmen, the private operators, the rural payroll, the county budget line that eats the property tax. "Prison-industrial complex" is a seminar word and "law and order" is a vibe; Big Prison is a name a pastor, a podcast listener and a district attorney can all say out loud. Use it. Capitalize it.

## How we look at the problem

The country counts people in prison by the million. A million is not a number anyone can feel. Our job is to take the big number and break it down, piece by piece, until it is the size of one person. 1.9 million becomes Texas, becomes a county, becomes a jail, becomes a cell, becomes a name we do not print.

That operation, the breakdown, is our visual language. It is why the brand uses fractal and recursive geometry: a block that splits into four, one quarter of which splits again, and again, until the smallest piece is one. The pattern is trippy on purpose, because the night the name came from was, and because the way out of a system that survives by being invisible is to make people see all of it at once. But every fractal we draw is doing arithmetic. Each subdivision is a real split in a real number. See **Visual language** for the rules.

## Voice

We sound like someone who has the receipts and has also been inside. Plain, exact, a little dry, never a seminar and never a sermon.

- Lead with the number and name its source in the same breath. "Texas held 68,000 people in county jails last month, most not convicted of anything (TCJS, Sept. 2026)."
- Say "people in jail," "people in prison," "people who were inside." Never "inmates," "offenders," "convicts," "felons" as nouns for people. "Cage" is allowed and encouraged for the thing, never for the person.
- Name the policy, not the villain's character. A legislator has a cage count, not a moral failing.
- Every public claim carries its receipt: a citation, a link, a report number. In an environment drowning in generated content, a campaign that is one hundred percent receipts is itself the differentiator.
- Short sentences. Active voice. No em-dash asides, no "not X, but Y," no "it's worth noting."
- Humor is allowed. Cruelty is not, in either direction.

Sample headline voice: "Senator Hughes has voted to build 4,200 prison beds. Her district has 1,100 people in TDCJ." Sample body voice: "Expunction in Texas requires a petition under Code Crim. Proc. Ch. 55A, a filing fee, and usually a lawyer. Most eligible Texans never file. We are going to file for them."

## Color: the slick

The palette is an oil slick on black. Black is the ground; violet is the body of the slick; green and magenta are the sheen that moves across it; gold is the rare flash. The slick is never a gradient we paint on. It is the result of putting the sheen colors next to each other on black at full strength, which is what a breakdown does automatically.

| Token | Role |
| --- | --- |
| `void` | The ground. Dark by default. |
| `surface`, `surface-raised` | Panels and hover, one and two steps up. |
| `hairline` | Rules and the cuts between tiles. 1px, never more. |
| `ink`, `ink-muted` | Text. Both pass 4.5:1 on every surface in both themes. |
| `violet` | Primary. Links, buttons, the largest tile. |
| `green` | Sheen. Second tile, cleared or released states. |
| `magenta` | Sheen. Third tile, the live tick, one emphasis per screen. |
| `gold` | Money. If it is gold, it is a dollar figure. |
| `alert` | Deaths in custody, errors. Never decoration. |

Rules that keep it clean:

- Dark is the default theme (`Slick`). `Daylight` exists for print, legal filings, and documents that will be photocopied. Both themes share the same tokens; nothing is tuned for one only.
- The sheen colors never carry meaning by hue alone. Green does not mean good and magenta does not mean bad; a label says what a tile is.
- No purple-to-blue gradient heroes, no glow, no blur. The iridescence comes from flat sheen colors meeting on black with a hairline cut between them.
- `alert` stays out of the slick. If a death count sits inside a breakdown, the tile is `alert` and the label says "died in custody."

## Type

Three faces, each with one job.

- **Syne** (`display`) for the name and headlines. Heavy, slightly strange, built to be large. Use weight 800 at `display-xl` and `display`, 700 at `title`. Never below 32px.
- **Atkinson Hyperlegible** (`body`) for everything people read. It was designed for low vision, which matters when the reader is on a phone in a county clerk's hallway or reading a letter in a cell. 17px running text, 60 to 70 characters a line.
- **JetBrains Mono** (`data`) for every number that is a count, a dollar, a date, or a citation. Tabular figures always, so a column of counts lines up. A number set in the body face is a number nobody checked.

All three are hosted on Google Fonts; load them with a single stylesheet link and declare the fallback stacks in `type.families`.

## Figures and receipts

A figure is a number plus its source, and it is not finished without both. The pattern is `figure` on top, a `label` eyebrow above it saying what it counts, and a `small` source line under it in `ink-muted` with the report name, the date, and the statute the data is published under where there is one. Examples of source lines:

- Source: TCJS Abbreviated Population Report, Sept. 2026 (Gov't Code Ch. 511)
- Source: TDCJ High Value Data Set, Oct. 2026 (Gov't Code §2054.1265)
- Source: Attorney General custodial death reports (Code Crim. Proc. art. 49.18)

Aggregates only. No names, no mugshots, no case numbers. This is a courtesy to the people counted and a rule of the brand, and it keeps the organization clear of mugshot-publication law (Bus. & Com. Code Ch. 109) and out of the business of republishing records later expunged under Code Crim. Proc. Ch. 55A or sealed under Gov't Code Ch. 411, Subch. E-1.

## Imagery

- Use: the breakdown pattern, hairline grids, oversized figures, documents and receipts as objects, photographs of real people who chose to be photographed, Texas landscape and rural infrastructure (a shuttered unit, a processing floor, a courthouse square).
- Do not use: bars, handcuffs, chain-link, orange jumpsuits, silhouettes behind bars, stock photos of hands on cell doors, or any mugshot. These are Big Prison's own iconography and they make the person disappear.
- Fractals are geometry, not wallpaper. A fractal in our work subdivides a real number. A decorative Mandelbrot set is off-brand.

## Spacing and radius

A 4px base. `space-1` (4px) is the cut between tiles in a breakdown and is the most important step in the system. Pieces of a larger thing have no radius (`radius-0`); controls get `radius-sm`; cards get `radius-md`. The rule: if it is a piece of a number, it is square.

## The mark

The mark is a formula, not a file: the Julia set of z² + c rendered in the slick palette, live in `mark/index.html`. A specific instance of the logo is a seed, a center and a zoom (the "Copy view" output), which anyone can regenerate at any resolution. Until a seed is chosen, the name set in Syne 800 is the wordmark.
