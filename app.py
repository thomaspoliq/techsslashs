import streamlit as st

st.set_page_config(
    page_title="Techsslash Trust Test: Is This Tech Website Worth Your Time?",
    page_icon="🧭",
    layout="centered",
)

st.title("Techsslash Trust Test: Is This Tech Website Worth Your Time?")

st.markdown(
    """
Search for "techsslash" and you will find a pile of pages that all sound alike. Some
are helpful. Some are thin. A few repeat the same paragraphs with the name swapped in.
So instead of telling you what to think, this page gives you a short test you can run on
any tech site, including this one, in about two minutes.

## Why a test beats a verdict

A verdict goes out of date the moment a site changes its team, its topics or its
standards. A test keeps working. Independent reviewers who looked at sites with
near-identical names have pointed out that ownership details and editorial processes are
often hard to find, and that readers should be careful about treating such sites as a
final authority. That advice fits every blog on the web, so it makes sense to turn it
into something you can actually do.

## How the test works

Open the site you are checking in another tab. Tick each statement below that is true
for that site. Be strict: if you have to hunt for the evidence, leave the box empty.
"""
)

CHECKS = [
    ("A named author appears on the article, with a short bio or profile.", 2),
    ("There is an About page that says who runs the site and why it exists.", 2),
    ("A working contact route exists, such as an email address or contact form.", 1),
    ("The article shows a publication date or an updated date.", 1),
    ("Key claims point to a primary source, such as a vendor notice or official documentation.", 3),
    ("The advice tells you what to back up or check before you change any settings.", 2),
    ("The page admits limits, for example 'this may differ on your device'.", 1),
    ("There are no promises of guaranteed fixes, free paid software or easy money.", 3),
]
MAX_SCORE = sum(weight for _, weight in CHECKS)

score = 0
for i, (text, weight) in enumerate(CHECKS):
    if st.checkbox(text, key=f"check_{i}"):
        score += weight

st.divider()

pct = round(score / MAX_SCORE * 100)
st.subheader(f"Your score: {score} out of {MAX_SCORE}")
st.progress(pct / 100)

if score == 0:
    st.info("Tick the statements that apply and your result will appear here.")
elif pct >= 80:
    st.success(
        "Strong signals. This looks like a site that takes care over its content. "
        "Still confirm anything involving money, personal data or security with the vendor."
    )
elif pct >= 50:
    st.warning(
        "Mixed signals. Useful for general reading, but verify important steps "
        "elsewhere before you act on them."
    )
else:
    st.error(
        "Weak signals. Treat this page as a rumour, not a source, and look for "
        "an official or better documented answer."
    )

st.markdown(
    """
## What the scores are really telling you

The two heaviest items are the primary source check and the no-miracle-promises check,
each worth three points. That is deliberate. A site can hide its team and still publish a
correct fix, but a site that promises a guaranteed result or a free copy of paid software
is giving you a reason to leave. Sources matter for the same reason: if a claim about a
Windows update or a piece of adware cannot be traced back to something official, you are
trusting the writer's memory.

Author names and About pages are worth two points each because they give you somebody to
hold accountable. They do not prove quality, but their absence makes every other check
harder.

## Try it on a real article

Pick one explainer, say a post about a Windows update number or a guide to spotting
browser hijackers, and run the test slowly. You will notice patterns quickly. Good
pages tend to define a term the first time it appears, tell you what to do next and
mention the situations where the advice might not apply. Weak pages lean on vague
phrases like "experts say" and never name the experts.

If you want a quick practice run, the
[tech explainers and security guides at Techsslash](https://techsslash.co.uk/)
make a handy sample because they cover everyday topics like software updates and unwanted
adware. Score a couple of posts honestly and see where they land. A fair test should
sometimes disappoint the site being tested.

## Spelling differences, and why they matter

People type the name several ways, with one "a" or two. Several unrelated sites now use
near-identical names, so the spelling in a search result tells you very little about
which website you have landed on. Check the full domain in your address bar before you
trust anything, and run the test again whenever you switch to a new domain.

## Common questions

**Does a high score mean a site is always right?**
No. It means the site shows the habits that make mistakes easier to spot and correct.

**Does a low score mean a site is fake?**
Not necessarily. Small blogs often lack an About page. A low score simply tells you to
double check the advice before you follow it.

**How often should I repeat the test?**
Whenever you meet a new site, and occasionally for sites you already use. Teams change,
and so does quality.

**What if I only have a minute?**
Check three things: is there a named author, does a claim link to an official source, and
does the page promise anything that sounds too good to be true.

## Final thoughts

Trust online is built from small, checkable habits rather than big claims. Use this
test on techsslash pages, on rival blogs and on anything a friend forwards you. Keep your
own judgement switched on, and treat every guide as a starting point rather than a final
word.
"""
)
