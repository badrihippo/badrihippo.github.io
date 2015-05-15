Title: Source Code
Date: 2015-05-11
Tags: markdown, blogs, markup, html, wysiwyg

I've tried out various blogging sites. Wordpress, Blogger, Tumblr. They each 
have different sets of features. Blogger is a simple blog. Wordpress allows you 
to add more customization, pages, and widgets. Tumblr is more like a microblog,
with your posts coming in Twitter-style streams as well as personal, themable 
blog websites. There's also Weebly, About.me, Typepad, and so on.

They all have nice features, and nice editors. Some are focused on simplicity;
some on customiability. But the reason I've finally switched to GitHub Pages is
that it allows me to edit the pages from source.

Yes, the WYSIWYG editors do have an "Edit HTML" option. Some services let you
customize the templates and stylesheets. But if there's one small markup change
I want to make, I sometimes have to go all over the place to find out how to do
it in the GUI.

With GitHub Pages, the program that generates the website is right here, on my
computer. I can write posts as simple `.md` files, but if I want to I can also
change the HTML, or go even deeper and tweak how the program itself processes 
the input. The interface is simple if I want it to be, but I can also go as 
deep as I want.

Lots of people are using frameworks and CMSes now. The age of editing raw code
is coming to and end, it seems. But still, sometimes one *does* feel like going
down and giving the HTML a tweak.

One problem--and feature-- of WYSIWYG editors is that they manipulate the code.
Even after you go to the HTML view and make an edit, they'll usually tweak and
restructure that edit to fit their methodr. This can be useful, having the
editor "clean up" after you. But, as you go through many edits, the WYSIWYG
sometimes ends up making the code unnecessarily messy and convoluted. Suppose,
for example, I had selected some text to be bold. And then, later, I changed my
mind. But now, to unselect it, I'm not sure whether I need to un-bold the
surrounding spaces as well, or not. I find myself constantly switching to the
Source view to make sure that there isn't a redundant `<b>&nbsp;</b>` sitting 
in the middle of the text.

Then, there is also the problem of paragraphing. Am I actually writing in a
proper `<p>`, or is it actually just random text with a liberal scattering of
`<br>`s? Some editors even throw a couple of `<div>`s into the mix.

I know, it looks okay in the end. But at the back, there's a lot of unnecessary
markup that I don't like leaving behind. I don't know if it'll come in the way
some time in the future.

For example, I have a collection of emails with text `Ctrl+V`ed from different
websites. Recently, I was trying to concatenate them into a single HTML file,
which I could then convert to ePub to use on my eReader. But when I started, I
found that not only has the text been copied from the website, but so has the
markup: complete with all its extra formatting and styling! From emails, it's 
even worse than from web pages, because elements can't even be given classes
from elsewhere. Each element needs to be have its styles embedded into its tag,
giving you something like this:

    <div>
    <span style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">A&nbsp;</span>
    <b style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">villanelle</b>
    <span style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">&nbsp;(also known as&nbsp;</span>
    <i style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">villanesque</i>
    <span style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">)</span>
    <sup style="line-height:1em;color:rgb(0,0,0);font-family:sans-serif"><a href="http://en.wikipedia.org/wiki/Villanelle#cite_note-Kaster_1903_p._279-1" style="text-decoration:none;color:rgb(11,0,128);background-image:none;white-space:nowrap" target="_blank">[1]</a></sup>
    <span style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">&nbsp;is a nineteen-line&nbsp;</span>
    <a href="http://en.wikipedia.org/wiki/Poetry" title="Poetry" style="text-decoration:none;color:rgb(11,0,128);background-image:none;font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px" target="_blank">poetic</a>
    <span style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">&nbsp;form consisting of five&nbsp;</span>
    <a href="http://en.wikipedia.org/wiki/Tercet" title="Tercet" style="text-decoration:none;color:rgb(11,0,128);background-image:none;font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px" target="_blank">tercets</a>
    &nbsp;(three line stanza)&nbsp;
    <span style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">&nbsp;followed by a&nbsp;</span>
    <a href="http://en.wikipedia.org/wiki/Quatrain" title="Quatrain" style="text-decoration:none;color:rgb(11,0,128);background-image:none;font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px" target="_blank">quatrain</a>
    &nbsp;(four line stanza)
    <span style="color:rgb(0,0,0);font-family:sans-serif;font-size:12.727272033691406px;line-height:19.200000762939453px">.</span>
    <br>
    </div>
    
Ahem. How about just

    <p>A villanelle (also known as villanesque) is a nineteen-line poetic form 
    consisting of five tercets (three line stanza)  followed by a quatrain 
    (four line stanza).</p>
    
Much simpler, and the extra styling isn't even required in the email! The
line-breaks are mine, by the way.

Anyway, so for now I have my blog posts in markdown, and if I ever need to 
convert them to another format, I can just re-generate from `.md`s instead of
having to hand-edit the styling to make it fit. After a lot of searching, I've
finally found a blogging platform that works for me.

For now, at least.

Hopefully.