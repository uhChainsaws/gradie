// #let bg_colour = rgb("#fffcf2")
// #let text_colour = rgb("#252422")
// #let heading_colour = rgb("#403d39")
// #let accent_colour = rgb("#eb5e28")
#let bg_colour = rgb("#f2e8cf")
#let text_colour = rgb("#386641")
// #let heading_colour = rgb("#386641")
#let heading_colour = rgb("#6a994e")
#let accent_colour = rgb("#bc4749")

#let stylle(title: none, doc) = {
    set text(
        // font: ("Space Mono", "PT Mono"),
        font: "PT Mono",
        size: 12pt,
        fill: text_colour,
        hyphenate: false,
    )

    show math.equation: set text(fill: accent_colour)
    
    show heading: it => [
        #set align(right)
        #set text(
            16pt, 
            weight: "extrabold",
            fill: heading_colour,
            // tracking: 0.5em,
        )
        #block(upper(it.body))
    ]
    set par(
        justify: true,
        leading: 1em,
    )
    set page(
        paper: "a4",
        fill: bg_colour,
    )
    align(right+horizon)[
        #set text(
            size: 42pt,
            fill: accent_colour,
            tracking: 0.2em,
            hyphenate: true,
        )
        #title
    ]

    align(left+bottom)[#emph[
        #set text(size: 16pt)
        by Кравчук Владислав \ 
        #link("https://isu.ifmo.ru/pls/apex/f?p=2437:7:116994060325398")[ISU[368372]] \
        #link("https://t.me/uhChainsaws")[\@uhChainsaws] \
    ]]
    
    pagebreak()

    set page(
        margin: (x: 4cm, y: auto),
        header: align(left + horizon)[
            #set text(size: 8pt)
            _#repeat([#title]+[;])_
        ],
    )

    doc
}
