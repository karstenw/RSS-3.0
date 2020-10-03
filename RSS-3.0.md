

# RSS 3.0

This builds upon the ideas and descriptions of <a href="http://www.aaronsw.com/">Aaron Swartz</a>, where in his blog he described and defined in the entry <a href="http://www.aaronsw.com/weblog/000574">Introduction</a>.



Introduction

As to collect all information in one document, the <a href="http://www.aaronsw.com/weblog/000574">Introduction</a> has been quoted below.

There’s been a lot of talk in the community about how RSS 2.0 is too complicated. I haven’t heard any objections, so I’m going to move ahead with the following changes that will result in RSS 3.0.


1. Remove XML. XML is just too complicated and is against the spirit of RSS, which is Really Simple Syndication. I don’t want people to have to buy one of these 200 page XML books to understand RSS. And XML sucks up bandwidth like nobody’s business. Instead, we’ll go back to RFC822-style fields. There are lots of available parsers for those.

2. Remove namespaces. Namespaces are just a waste of time. If people want to add an element to RSS, then just send it to me and I’ll add it to my list of all elements in use. This system is easy to use and doesn’t result in any wasteful URIs all over the place.

3. HTML forbidden. No one needs HTML. Email has been just fine for years before Microsoft introduce their stupid rich HTML extensions. HTML is for those loser newbies. Any intelligent Internet user deals in plain text.



References:

1. http://www.aaronsw.com/2002/rss30
2. http://www.aaronsw.com/weblog/000574
3. http://r3r.sourceforge.net/rss3-spec.xhtml
4. https://communitywiki.org/wiki/RSS_3.0
5. https://patandkat.com/pat/weblog/rss3.txt



<h2>Format</h2>

<p>An <strong>item</strong> consists of a series of <strong>lines</strong> separated by "\n".</p>

<p>Each <strong>line</strong> is a series of letters, numbers, "-", "." or "_" (called the <strong>name</strong>) followed by ": " followed by a series of characters (called the <strong>value</strong>). No two lines should start with the same name. If a line starts with a space or tab character, then it is a continuation of the value on the previous line. The newline in between is preserved. UTF-8 encoding is always used.</p>

An item ends at the first blank line (that is, a line with no characters).





<h2>Document</h2>

<p>An RSS 3.0 document consists of one head item followed by zero or more body items.</p>



<h3>Head</h3>

<p>The head is an <strong>item</strong>. Names for the lines are globally assigned. Names are case-insensitive. The assigned names are:</p>

<a href="#title">title</a>
<a href="#description">description</a>
<a href="#link">link</a>
<a href="#generator">generator</a>
<a href="#errorsto">errorsto</a>
<a href="#creator">creator</a>
<a href="#created">created</a>
<a href="#last-modified">last-modified</a>
<a href="#language">language</a>
<a href="#rights">rights</a>
<a href="#license">license</a>
<a href="#guid">guid</a>
<a href="#uri">uri</a>
<a href="#subject">subject</a>

Most properties refer to the whole feed in addition to the item. i.e. last-modified is the last-modified date of the feed.



<h2>Body</h2>

The body is a series of zero or more items. Names for the lines are globally-assigned and case-insensitive. The assigned names are:

<a href="#title">title</a>
<a href="#description">description</a>
<a href="#link">link</a>
<a href="#generator">generator</a>
<a href="#creator">creator</a>
<a href="#created">created</a>
<a href="#last-modified">last-modified</a>
<a href="#language">language</a>
<a href="#rights">rights</a>
<a href="#license">license</a>
<a href="#guid">guid</a>
<a href="#uri">uri</a>
<a href="#subject">subject</a>
<a href="#enclosure-type">enclosure-type</a>
<a href="#enclosure-length">enclosure-length</a>
<a href="#enclosure-uri">enclosure-uri</a>
<a href="#enclosure-episode">enclosure-episode</a>
<a href="#enclosure-season">enclosure-season</a>
<a href="#enclosure-explicit">enclosure-explicit</a>
<a href="#enclosure-duration">enclosure-duration</a>
<a href="#enclosure-tags">enclosure-tags</a>



<h2>Tokens</h2>

<dl>
<dt id="title">title</dt>
<dd>The title of the item.</dd>
<dt id="description">description</dt>
<dd>A short description of the item.</dd>
<dt id="link">link</dt>
<dd>A link to the item.</dd>
<dt id="generator">generator</dt>
<dd>The person or program that generated the item.</dd>
<dt id="errorsto">errorsto</dt>
<dd>An email address, optionally followed by a space and a name, of the person to send error reports about the feed to.</dd>
<dt id="creator">creator</dt>
<dd>An email address, optionally followed by a space and a name, of the person who created the item.</dd>
<dt id="created">created</dt>
<dd>The date (in <a href="http://www.w3.org/TR/NOTE-datetime">W3CDTF format</a>) the item was created.</dd>
<dt id="last-modified">last-modified</dt>
<dd>The date (in <a href="http://www.w3.org/TR/NOTE-datetime">W3CDTF format</a>) the item was modified.</dd>
<dt id="language">language</dt>
<dd>The language of the item, using the language tag format specified in <a href="http://www.ietf.org/rfc/rfc3066.txt">RFC 3066</a>.</dd>
<dt id="rights">rights</dt>
<dd>The copyright statement for the item.</dd>
<dt id="license">license</dt>
<dd>A URI for the copyright license of the item.</dd>
<dt id="guid">guid</dt>
<dd>A globally unique identifier for the item.</dd>
<dt id="uri">uri</dt>
<dd>A globally unique identifier in the form of a URI for the item.</dd>
<dt id="subject">subject</dt>
<dd>The topic of the item.</dd>
<dt id="enclosure-type" style="color:#00f;">enclosure-type</dt>
<dd>A MIME-type identifier for enclosure, audio/mpeg or video/mpeg</dd>
<dt id="enclosure-length" style="color:#00f;">enclosure-length</dt>
<dd>Number of bytes in Base10 notation</dd>
<dt id="enclosure-uri" style="color:#00f;">enclosure-uri</dt>
<dd>A URI for the item</dd>
<dt id="enclosure-episode" style="color:#00f;">enclosure-episode</dt>
<dd>A date in W3CDTF format, episode number to indicate order</dd>
<dt id="enclosure-season" style="color:#00f;">enclosure-season</dt>
<dd>A year or season number to indicate order</dd>
<dt id="enclosure-explicit" style="color:#00f;">enclosure-explicit</dt>
<dd>A flag to indicate if item is explicit, positive values should be "1", "Yes" or "True"</dd>
<dt id="enclosure-duration" style="color:#00f;">enclosure-duration</dt>
<dd>A value of whole seconds in Base10 format or colon-separated values in order Hours, minutes, seconds (hh:mm:ss)</dd>
<dt id="enclosure-tags" style="color:#00f;">enclosure-tags</dt>
<dd>A single entry or comma-separated list of categories (IAB19) and/or keywords</dd>
</dl>



The tokens highlighted in blue color are suggested extensions to Aaron's original specification, so a RSS 3.0 would be able to carry enough information for podcasts. This is done by adding tokens to describe and specify properties for podcast episodes, download length, duration, MIME-type and episode season and sequence numbers, as well to signal if the particular episode is explicit in content, tags to further describe the episode. 








<h2>Example 1 (Original RSS 3.0 specification by Aaron Swartz)</h2>

<pre>
title: RSS 3.0 News
description: Latest updates on RSS 3.0.
link: http://www.aaronsw.com/2002/rss30
creator: me@aaronsw.com Aaron Swartz
errorsTo: me@aaronsw.com Aaron Swartz
language: en-US

title: Spec Introduced
created: 2002-09-06
guid: 00795648-C1E0-11D6-9AA6-003065F376B6
description: 
 The spec was introduced to the world.

 A few people noticed.

Title: Zooko Likes It
Created: 2002-09-06
GUID: 0894CB2F-C1E0-11D6-9649-003065F376B6
Description: Zooko says he likes the spec.
</pre>



<h2>Example 2 (With suggested extensions applied)</h2>

<pre>
title: RSS 3.0 News
description: Latest updates on RSS 3.0.
link: http://www.aaronsw.com/2002/rss30
creator: me@aaronsw.com Aaron Swartz
errorsTo: me@aaronsw.com Aaron Swartz
language: en-UStitle: Spec Introduced
created: 2002-09-06
guid: 00795648-C1E0-11D6-9AA6-003065F376B6
description:
  The spec was introduced to the world.

  A few people noticed.

Title: Zooko Likes It
Created: 2002-09-06
GUID: 0894CB2F-C1E0-11D6-9649-003065F376B6
Description: Zooko says he likes the spec.

title: A podcast extension?
created: 2018-04-08 19:19:26
last-modified: 2018-04-08 19:21:34
description: A possible extension of Aaron's RSS 3.0 draft with aim to add podcast capabilities.
  New tokens added to accommodate values used for podcasts of audio and video contents.
  enclosure-type
  enclosure-length
  enclosure-uri
  enclosure-episode
  enclosure-season
  enclosure-explicit
  enclosure-duration
  enclosure-tags
  The above list would be able to carry enough information to replace RSS 2.0 feeds
enclosure-type: audio/mpeg
enclosure-length: 10485760
enclosure-uri: https://content.example.com/podcast/audio/does-not-exist.mp3
enclosure-explicit: No
enclosure-duration: 00:08:13
enclosure-tags: RSS 3.0, podcast, tokens, random blab, horses are insects
</pre>