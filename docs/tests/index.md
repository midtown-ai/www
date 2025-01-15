# Welcome to MkDocs

## images

Relative path

![](glossary/img/a/activation_function.png){style="width:100%"}
/// caption
Image caption
///

Absolute path (not recommended!)

```
![](/glossary/img/a/activation_function.png)
```

### Fails

```
![](a/activation_function.png)
```



## PDFs

/// warning | Warning
mkdocs-pdf creates an embed tag which is deprecated and replace with 'object' or 'iframe'
///

/// warning | Warning

Github does not support PDF with URL that are redirected. Use the final URL!
///

```
![Alt text](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210101201653/PDF.pdf){ type=application/pdf }
```

Redirect (Not supported on github!)

![Alt text](https://arxiv.org/pdf/2411.14251v1.pdf){ type=application/pdf }

Without redirect

![Alt text](https://arxiv.org/pdf/2411.14251v1){ type=application/pdf }

![Alt text](https://arxiv.org/pdf/2411.14251v1){ type=application/pdf style="min-height:100vh;width:100%" }


## Icons, Smileys and highlights/marks

fontawesome (53,663 icons) - https://fontawesome.com/search

 * : fontawesome - class - name :   <!> to find the class look at the  HTML
 * `<i class="fa-brands fa-html5">` turns into `:fontawesome-brands-html5:` which renders as :fontawesome-brands-html5: 


materialdesign (7447 icons) - https://pictogrammers.com/library/mdi/

 * https://pictogrammers.com/library/mdi/icon/clock-fast/
 * turns into `:material-clock-fast:` rendered :material-clock-fast:

octicons - https://primer.style/foundations/icons

 * https://primer.style/foundations/icons/arrow-right-24
 * turns into  `:octicons-arrow-right-24:` or :octicons-arrow-right:

simpleicons - https://simpleicons.org/

***

:smile: and :heart: those ==emojis are awesome,== isn't it?

***

text below rule



## CSS

 :fontawesome-brands-twitter: :fontawesome-brands-twitter:{ .twitter-blue .font42px}

 :fontawesome-brands-youtube: :fontawesome-brands-youtube:{ .youtube-red .fading-in-and-out }
 <div class="fading-in-and-out">Fading text!</div>

 :fontawesome-solid-arrow-up: :fontawesome-solid-arrow-up:{ .bouncing-vertically }
 <div class="bouncing-vertically">Bouncing text!</div>

 :fontawesome-solid-arrow-right: :fontawesome-solid-arrow-right:{ .bouncing-horizontally } Text
 <div class="bouncing-horizontally">Bouncing text!</div>

 :fontawesome-brands-html5: :fontawesome-brands-html5:{ .flipping }
 <div class="flipping">Flipping text!</div>

 :fontawesome-solid-bell: :fontawesome-solid-bell:{ .shaking .red }
 :fontawesome-regular-bell: :fontawesome-regular-bell:{ .shaking .red }
 <div class="shaking">Shaking text!</div>

 :fontawesome-solid-arrows-spin: :fontawesome-solid-arrows-spin:{ .spinning-clockwise }
 :fontawesome-solid-spinner: :fontawesome-solid-spinner:{ .spinning-counter-clockwise }

 :octicons-heart-fill-24: :octicons-heart-fill-24:{ .heartbeating } :octicons-heart-fill-24:{ .heartbeating .red }
 <div class="heartbeating">Headbeating text!</div>

/// warning |
```
# attr_list
{: #id1 .class1 id=id2 class="class2 class3" .class4 }
results in
id="id2" class="class2 class3 class4"
```
///

 More at: https://python-markdown.github.io/extensions/attr_list/

## Links & Tooltips & Abbreviations & footnotes

### links

 * open pdf - https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210101201653/PDF.pdf
 * open web - page https://www.google.com

 [:octicons-arrow-right-24: Google](https://www.google.com "Go to Google")


Work:

 * https://www.ggogle.com
 * [markdown link to a](glossary/a.md#ablation)
 * [in-page Reference-Style external Links][markdown syntax]
 * [in-page Reference-Style internal Links][glossary link]
 * [markdown syntax]
 * [glossary link] and [GloSSAry Link]

```
 * [snippets admonition][ablation]
 * direct snippets [ablation] and [accuracy]
```

[markdown syntax]: https://daringfireball.net/projects/markdown/syntax#link "title"
[glossary link]: glossary/a.md#ablation "title"

```
Deprecated by snippets

 * [include-markdown links toto]
 * [include-markdown links_a titi] = include of include!
{% include '../includes/links.md' %}
```

Fail:

```
 * [#big] just to anchor (fails)
 * [in-page Reference-Style no match][no match]
```

### tooltips

:material-information-outline:{ title="Important information" }

[Hover me using inline syntax](https://example.com "I'm a tooltip!")

```
[Hover me using external reference link][example]
```

[Hover me using internal reference link][example2]

  [example2]: https://example.com "I'm a tooltip!"

### abbreviations

 Do these abbreviations work: CSS, W3C, and not HTML ? What about FAQ, Faq, TOC, Toc, and GFM?
 Yes if you hover the acronym !

/// danger| beware
abbreviations are case sensitive
///

In-page abbreviations
*[CSS]: Custom Style Sheet
*[W3C]:  World Wide Web Consortium

Disabled reference abbreviations
*[HTML]: 'H'

### footnotes

Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.

[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

