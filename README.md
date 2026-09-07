# Zad

**Open source security tooling, verified**
Provisions for the road, for anyone starting in cybersecurity.

[Open the catalogue](https://siteq8.github.io/Zad/) · [العربية](#زاد)

---

## What this is

A curated catalogue of 114 open source repositories and 64 sites and platforms,
organised by what you are trying to do rather than by alphabet. Half of what a
beginner needs is not a repository: it is a place to practise, a standard to
read, a lookup service, or someone explaining what happened last week. Twelve paths: starting out, capture the
flag, offensive, defensive, application security, cloud, governance,
intelligence, industrial and OT, mobile, hardware and radio, and research.

Starting out is an ordered route rather than a grid, because the hardest part of
beginning is not knowing what to do second. Every step in it is checked on each
build and the build fails if a step points at a project that has stopped.

## Why another list

Most curated security lists rot. They are written once, and years later they
still point at repositories that have been archived, renamed by their
maintainer, or abandoned. You find out by opening ten tabs.

Zad verifies both halves on every build. Repositories are resolved against the
GitHub API, which records stars, licence, language, archive status and the date
of the last push, and maintenance is classified from that date rather than from
an impression:

| Status | Meaning |
| --- | --- |
| maintained | pushed within 6 months |
| quiet | pushed within 2 years |
| dormant | nothing for over 2 years |
| archived | the maintainer has stopped |

**An entry that cannot be resolved is not published.** A renamed repository is
followed and the new name recorded, so the catalogue corrects itself instead of
rotting. Building this catalogue found one entry pointing at the wrong owner, three
projects that had moved to new names, and one recommended in the starting path
that had been archived. All five would have sat in a hand written list
indefinitely.

Where a project has stopped and a live replacement exists, the card says so and
names it. Two entries carry that pointer today.

Sites and platforms have no API to ask, so they are fetched instead, and the
result is classified rather than reduced to alive or dead:

| Status | Meaning |
| --- | --- |
| reachable | answered normally |
| redirected | answered from a different host, and the link now points where it landed |
| blocks automated checks | refused the request, which is a bot filter and not evidence of closure |

Treating a refusal as death would have quietly deleted five of the most used
services in the catalogue, so a blocked resource is kept and labelled. Only a
genuine error or no answer at all removes an entry. Verification found two
resources that had moved host: one documentation wiki, and Project Zero, which
left blogspot for its own domain while most lists still point at the old one.

Headline figures on the page are computed from the catalogue rather than typed,
because the first version of them was already stale by twenty tools.

## Both languages, completely

Every tool carries a note in English and Arabic. The build fails if a note is
missing, if Latin words appear in an Arabic note, or if Arabic script appears in
an English one. Neither language is a translation layer over the other.

## Rebuilding

```
GITHUB_TOKEN=your_token python3 scripts/build.py
python3 scripts/build_site.py
```

The first resolves every entry and reports what changed. The second embeds the
result into a single page with no external request of any kind, then checks that
the headline figures written in the template still match the data.

Use `--strict` on the first to fail the build on any unresolved entry.

## Adding a tool

Add a row to `data/seed.py` and a note to `data/notes.ar.json`, then rebuild. The
build will tell you if the repository does not resolve or the Arabic is missing.

Suggestions are welcome by issue. A tool needs a reason to be here that is
useful to someone who has not used it, so please write the note as if for them.

## Licence

MIT. Each catalogued tool carries its own licence, shown on its card.

---

# زاد

**أدوات أمنية مفتوحة المصدر، مُتحقَّق منها**
زاد الطريق لمن يبدأ في الأمن السيبراني.

[افتح الكتالوج](https://siteq8.github.io/Zad/)

## ما هذا

كتالوج منتقى لمئة وأربعة عشر مستودعا مفتوح المصدر وأربعة وستين موقعا ومنصة، مرتبة
حسب ما تريد أن تفعله لا حسب الحروف، فنصف ما يحتاجه المبتدئ ليس مستودعا بل مكانا
يتدرب فيه أو معيارا يقرؤه أو خدمة بحث أو من يشرح له ما جرى الأسبوع الماضي، وفيه اثنا عشر مسارا هي البداية ومسابقات التقاط العلم والأمن الهجومي
والأمن الدفاعي وأمن التطبيقات والسحابة والحوكمة والاستخبارات والأنظمة الصناعية
والأجهزة المحمولة والعتاد والراديو والبحث.

ومسار البداية طريق مرتب لا شبكة بطاقات، لأن أصعب ما في البداية ألا تعرف الخطوة
الثانية، وتُفحص كل خطوة فيه في كل بناء ويسقط البناء إن أشارت خطوة إلى مشروع توقف.

## لماذا قائمة أخرى

أكثر القوائم الأمنية المنتقاة تتعفن، إذ تُكتب مرة ثم تبقى بعد سنوات تشير إلى
مستودعات أُرشفت أو غيّر أصحابها أسماءها أو هُجرت، ولا تكتشف ذلك إلا بفتح عشر
نوافذ.

أما زاد فيحلّ كل مدخل أمام واجهة غِت هَب البرمجية في كل بناء ويسجل ما هو صحيح
الآن من نجوم ورخصة ولغة وحالة أرشفة وتاريخ آخر دفع، ثم تُصنَّف الصيانة من ذلك
التاريخ لا من انطباع:

| الحالة | المعنى |
| --- | --- |
| مصانة | دُفع إليها خلال ستة أشهر |
| هادئة | دُفع إليها خلال سنتين |
| راكدة | لا شيء منذ أكثر من سنتين |
| مؤرشفة | أوقفها صاحبها |

**والمدخل الذي لا يُحَل لا يُنشر،** أما المستودع الذي غُيّر اسمه فيُتتبَّع ويُسجَّل
اسمه الجديد، فيصحح الكتالوج نفسه بدل أن يتعفن، وقد كشف بناء هذا الكتالوج مدخلا
يشير إلى مالك خاطئ ومشروعا انتقل، وكلاهما كان سيبقى في قائمة يدوية إلى ما لا
نهاية.

وحين يتوقف مشروع ويوجد بديل حي تقول البطاقة ذلك وتسمّي البديل، ويحمل مدخلان هذه
الإشارة اليوم.

## اللغتان كاملتان

تحمل كل أداة وصفا بالإنجليزية والعربية، ويسقط البناء إن غاب وصف أو ظهرت كلمات
لاتينية في وصف عربي أو ظهر حرف عربي في وصف إنجليزي، فليست إحدى اللغتين طبقة
مترجمة فوق الأخرى.

## إعادة البناء

```
GITHUB_TOKEN=your_token python3 scripts/build.py
python3 scripts/build_site.py
```

يحلّ الأمر الأول كل مدخل ويبلغ عما تغيّر، ثم يدمج الثاني النتيجة في صفحة واحدة لا
تصدر أي طلب خارجي، ويتحقق من أن الأرقام المكتوبة في القالب ما زالت تطابق البيانات.

## إضافة أداة

أضف سطرا في ملف البذرة ووصفا عربيا في ملف الأوصاف ثم أعد البناء، وسيخبرك البناء
إن لم يُحَل المستودع أو غاب النص العربي.

والاقتراحات مرحب بها عبر البلاغات، على أن يكون للأداة سبب وجود مفيد لمن لم
يستعملها من قبل، فاكتب الوصف كأنك تخاطبه.

## الرخصة

رخصة إم آي تي، ولكل أداة مفهرسة رخصتها الخاصة المعروضة على بطاقتها.
