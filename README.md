# Zad

**Open source security tooling, verified**
Provisions for the road, for anyone starting in cybersecurity.

[Open the catalogue](https://siteq8.github.io/Zad/) · [العربية](#زاد)

---

## What this is

A curated catalogue of 94 open source security tools, organised by what you are
trying to do rather than by alphabet. Nine paths: starting out, capture the
flag, offensive, defensive, application security, cloud, governance,
intelligence, and research.

## Why another list

Most curated security lists rot. They are written once, and years later they
still point at repositories that have been archived, renamed by their
maintainer, or abandoned. You find out by opening ten tabs.

Zad resolves every entry against the GitHub API on each build and records what
is true right now: stars, licence, language, whether the project is archived,
and the date of the last push. Maintenance is classified from that date rather
than from an impression:

| Status | Meaning |
| --- | --- |
| maintained | pushed within 6 months |
| quiet | pushed within 2 years |
| dormant | nothing for over 2 years |
| archived | the maintainer has stopped |

**An entry that cannot be resolved is not published.** A renamed repository is
followed and the new name recorded, so the catalogue corrects itself instead of
rotting. Building this catalogue found one entry pointing at the wrong owner and
one project that had moved, both of which would have sat in a hand written list
indefinitely.

Where a project has stopped and a live replacement exists, the card says so and
names it. Two entries carry that pointer today.

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

كتالوج منتقى لأربع وتسعين أداة أمنية مفتوحة المصدر، مرتبة حسب ما تريد أن تفعله لا
حسب الحروف، وفيه تسعة مسارات هي البداية ومسابقات التقاط العلم والأمن الهجومي
والأمن الدفاعي وأمن التطبيقات والسحابة والحوكمة والاستخبارات والبحث.

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
