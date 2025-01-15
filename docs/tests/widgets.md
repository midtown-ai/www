# Widgets

## Grid of cards (md_in_html)

### card grids

/// warning | Warning

First div must not be indented

///

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

```
    Material for MkDocs is licensed under MIT and available on [GitHub]
```

    [:octicons-arrow-right-24: License](#)

</div>


<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

## Content Tabs

### simple

=== "Tab A"
    In a different tab set.

=== "Tab B"
    ```
    More content.
    ```

### linked tabs

=== "C"

    C code linked tab

=== "C++"

    C++ code linked tab

===! "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```


## Table

| First Header | Second Header | Third Header
| :----------- |:-------------:| -----------:
| Left         | Center        | Right :material-check:
| Left         | Center        | Right :material-check-all:
| Left         | Center        | Right :material-close:


## admonition

### blocks.adminition

/// note | note: ...
///

/// attention | attention ~ note ...
///

/// caution | caution ~ note ...
///

/// danger | danger ...
///

/// error | error ~ note ...
///

/// hint | hint ~ note ...
///

/// tip | tip ...
///

/// warning |
Warning with no Warning title!
///


/// warning | warning ...
///

#### Tentative

/// warning | warning ...
```
---8<--- abbreviations.md
```
///

```
---8<--- abbreviations.md
```

/// example | e
///

### blocks.details

/// details | note ...
///

/// details | danger ...
    type: danger
///
/// details | tip ...
    type: tip
///
/// details | question ...
    type: question
///

/// details | warning ...
    type: warning
    open: True

Rendering of pymdownx.blocks.details is function of type, which is a CSS class!
///

#### Tentative

/// details | examplee
Hello!
///

