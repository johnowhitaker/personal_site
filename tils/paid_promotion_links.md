---
title: Hiding an Annoying Element with Stylus
date: 2025-04-10
category: TILs
---

YouTube has this annoying thing where on hover a little overlay pops up over some videos that says 'Includes paid promotion...'. I click on this accidentally fairly frequently, opening up a support.google.com link instead of the video I want. This bugs me, but it's a very minor annoyance. In the past I'd probably just ignore it. I tried inspecting the element in the Chrome dev tools but couldn't find it and that's about as much effort as I'm willing to manually do for somethig this small. FOrtunately, these days we have AI! A quick back-and-forth with GPT4.5 and I've solved the problem for myself!

![The problem](yt_overlay.png)

I went with a CSS rule in the Stylus browser extension:

```CSS
@-moz-document domain("youtube.com") {
    a[href*="support.google.com/youtube"] {
        display: none !important;
        pointer-events: none !important;
    }
}
```

I'm amused how low my tolerance for painful stuff on a computer is these days, and how happy it makes me to fix any remaining tiny paper cuts with my code-slinging AI buddies.