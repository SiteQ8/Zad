"""Resources that do not live on GitHub.

Half of what a beginner actually needs is not a repository. It is a place to
practise, a standard to read, a lookup service, or someone explaining what
happened last week. Those are verified differently: the build fetches each one
and records whether it answered, where it ended up, and whether it refused the
request.

Fields:
  url    canonical address
  kind   category id
  roles  who this is for
  note   one line on why it is here
"""

KINDS = {
    "practice": ("Practice platforms", "منصات التدرب"),
    "ctf": ("Competition", "المسابقات"),
    "docs": ("Reference and documentation", "المراجع والتوثيق"),
    "standard": ("Standards and frameworks", "المعايير والأطر"),
    "lookup": ("Lookup and intelligence services", "خدمات البحث والاستخبارات"),
    "sandbox": ("Online analysis", "التحليل عبر الإنترنت"),
    "reading": ("Reading and reporting", "القراءة والتقارير"),
    "cert": ("Certification", "الشهادات"),
    "regional": ("Kuwait and Gulf authorities", "الجهات الكويتية والخليجية"),
}

WEB = [
    # ---- Practice platforms
    ("https://tryhackme.com/", "practice", ["start", "red", "blue"],
     "Guided rooms that hold your hand at the start and let go gradually. The gentlest entry."),
    ("https://www.hackthebox.com/", "practice", ["red", "ctf"],
     "Machines to break with no guidance. Move here once guided rooms feel slow."),
    ("https://portswigger.net/web-security", "practice", ["start", "appsec"],
     "The Web Security Academy. Free, thorough, and the best web application training that exists."),
    ("https://overthewire.org/wargames/", "practice", ["start", "ctf"],
     "Wargames over SSH that teach Linux and binary basics one small puzzle at a time."),
    ("https://pwn.college/", "practice", ["ctf"],
     "A university course on exploitation, released free with its lectures and challenges."),
    ("https://cryptohack.org/", "practice", ["ctf"],
     "Cryptography as a set of puzzles rather than a textbook."),
    ("https://www.root-me.org/", "practice", ["ctf", "red"],
     "A very large challenge archive across every category, free and long running."),
    ("https://exploit.education/", "practice", ["ctf"],
     "Virtual machines built purely to teach memory corruption in order of difficulty."),
    ("https://microcorruption.com/", "practice", ["ctf"],
     "Embedded exploitation in the browser, with a debugger built in. Unusually well made."),
    ("https://www.vulnhub.com/", "practice", ["red", "start"],
     "Downloadable vulnerable machines to run in your own lab, no account needed."),
    ("https://cyberdefenders.org/", "practice", ["blue"],
     "Blue team challenges built on real artefacts. The defensive answer to Hack The Box."),
    ("https://letsdefend.io/", "practice", ["blue"],
     "A simulated SOC where you work real alerts to a conclusion."),
    ("https://blueteamlabs.online/", "practice", ["blue"],
     "Investigation and incident response exercises with a scoring system."),
    ("https://hackthissite.org/", "practice", ["start"],
     "One of the oldest free practice sites and still a reasonable first hour."),

    # ---- Competition
    ("https://ctftime.org/", "ctf", ["ctf"],
     "The calendar and ranking for competitions worldwide. Start here to find one running."),
    ("https://picoctf.org/", "ctf", ["start", "ctf"],
     "Built for school students, which makes it the best on ramp for adults too."),

    # ---- Reference and documentation
    ("https://attack.mitre.org/", "docs", ["blue", "red", "intel", "grc"],
     "The catalogue of adversary techniques that almost everything else maps to. Learn its structure."),
    ("https://d3fend.mitre.org/", "docs", ["blue"],
     "The defensive counterpart to ATT&CK, mapping countermeasures to techniques."),
    ("https://capec.mitre.org/", "docs", ["appsec", "red"],
     "Attack patterns described at the level of design rather than implementation."),
    ("https://cwe.mitre.org/", "docs", ["appsec"],
     "The taxonomy of software weakness types. What a vulnerability is an instance of."),
    ("https://www.cve.org/", "docs", ["blue", "appsec"],
     "The identifier scheme for publicly known vulnerabilities."),
    ("https://nvd.nist.gov/", "docs", ["blue", "appsec"],
     "Severity scores, affected versions and references for published vulnerabilities."),
    ("https://owasp.org/", "docs", ["appsec", "start"],
     "The open application security community. Most of the guides you will read start here."),
    ("https://gtfobins.org/", "docs", ["red", "ctf"],
     "Unix binaries that can be abused to escape restrictions or escalate. Check before giving up."),
    ("https://lolbas-project.github.io/", "docs", ["red", "blue"],
     "The Windows equivalent, listing signed binaries that attackers live off."),
    ("https://book.hacktricks.wiki/", "docs", ["red", "ctf"],
     "An enormous practical wiki of techniques per situation. Messy and consistently useful."),
    ("https://www.exploit-db.com/", "docs", ["red"],
     "An archive of public exploits and the papers behind them."),
    ("https://ippsec.rocks/", "docs", ["ctf", "red"],
     "Searchable index of walkthrough videos by technique, so you can find who explained a thing."),

    # ---- Standards and frameworks
    ("https://www.nist.gov/cyberframework", "standard", ["grc"],
     "The NIST Cybersecurity Framework. The vocabulary most other frameworks translate into."),
    ("https://csrc.nist.gov/", "standard", ["grc"],
     "NIST's publication library, including the 800 series most controls trace back to."),
    ("https://www.cisecurity.org/controls", "standard", ["grc"],
     "The CIS Critical Security Controls, ordered by what to do first."),
    ("https://www.cisecurity.org/cis-benchmarks", "standard", ["grc", "blue"],
     "Configuration baselines per platform, and the source most hardening tools check against."),
    ("https://www.iso.org/standard/27001", "standard", ["grc"],
     "The management system standard organisations get certified against. Paid, but this is the source."),
    ("https://www.pcisecuritystandards.org/", "standard", ["grc"],
     "Where the payment card standards are published, rather than a summary of them."),
    ("https://cloudsecurityalliance.org/research/cloud-controls-matrix", "standard", ["grc", "cloud"],
     "A cloud control framework already mapped to the other major standards."),
    ("https://www.enisa.europa.eu/", "standard", ["grc", "intel"],
     "The European agency's threat landscape reports and guidance, free to read."),

    # ---- Lookup and intelligence
    ("https://www.shodan.io/", "lookup", ["intel", "red", "ics"],
     "Searches what is exposed on the internet by service rather than by page content."),
    ("https://search.censys.io/", "lookup", ["intel", "red"],
     "The other internet wide scan index. Worth checking both, they disagree usefully."),
    ("https://crt.sh/", "lookup", ["intel", "red"],
     "Certificate transparency search. Finds subdomains that never appear in DNS lists."),
    ("https://urlscan.io/", "lookup", ["intel", "blue"],
     "Submits a URL and reports what the page actually loaded, safely and publicly."),
    ("https://www.virustotal.com/", "lookup", ["blue", "research"],
     "Multi engine file and URL reputation. Remember that uploads become visible to others."),
    ("https://bazaar.abuse.ch/", "lookup", ["research", "blue"],
     "A free malware sample repository for researchers, with hashes and tags."),
    ("https://urlhaus.abuse.ch/", "lookup", ["blue", "intel"],
     "Tracks URLs used for malware distribution, and publishes usable blocklists."),
    ("https://haveibeenpwned.com/", "lookup", ["start", "blue"],
     "Checks whether an address appears in a known breach. The first thing to show a non specialist."),
    ("https://www.abuseipdb.com/", "lookup", ["blue"],
     "Community reported reputation for addresses seen attacking."),

    # ---- Online analysis
    ("https://any.run/", "sandbox", ["research", "blue"],
     "Interactive sandbox where you can click through the infection as it runs."),
    ("https://www.hybrid-analysis.com/", "sandbox", ["research", "blue"],
     "Automated sandbox reports, free to search even without submitting."),
    ("https://www.joesandbox.com/", "sandbox", ["research"],
     "Deep behavioural reports, with a free tier that is enough to learn from."),

    # ---- Reading
    ("https://isc.sans.edu/", "reading", ["blue", "intel"],
     "A daily handler diary on what is actually being seen. Short and consistently worth it."),
    ("https://thedfirreport.com/", "reading", ["blue", "research"],
     "Full intrusion write ups with timelines and detections. The best free DFIR reading."),
    ("https://krebsonsecurity.com/", "reading", ["start", "intel"],
     "Long running investigative reporting on cybercrime, readable without a background."),
    ("https://googleprojectzero.blogspot.com/", "reading", ["research", "appsec"],
     "Deep vulnerability research written up properly. Hard, and worth the effort."),
    ("https://www.sans.org/white-papers/", "reading", ["grc", "blue"],
     "A large free paper archive, useful when you need a citable source."),
    ("https://www.first.org/cvss/", "docs", ["blue", "grc"],
     "How severity scores are actually calculated, which matters when you disagree with one."),

    # ---- Certification
    ("https://www.comptia.org/certifications/security", "cert", ["start", "grc"],
     "Security+ is the usual first certification and the one most job adverts recognise."),
    ("https://www.offsec.com/courses/pen-200/", "cert", ["red"],
     "OSCP. Practical, exhausting, and still the offensive certification people respect."),
    ("https://www.giac.org/", "cert", ["blue", "grc"],
     "GIAC certifications, expensive and technically serious, usually employer funded."),
    ("https://www.isc2.org/certifications/cissp", "cert", ["grc"],
     "CISSP is broad rather than deep, and is what management roles ask for."),
    ("https://www.isaca.org/credentialing/cisa", "cert", ["grc"],
     "CISA is the audit credential, and the natural one if compliance is your direction."),

    # ---- Kuwait and Gulf
    ("https://www.cbk.gov.kw/en/", "regional", ["grc"],
     "The Central Bank of Kuwait, which issues the resilience framework banks are held to."),
    ("https://www.citra.gov.kw/", "regional", ["grc"],
     "Kuwait's communications and information technology regulatory authority."),
    ("https://nca.gov.sa/en/", "regional", ["grc"],
     "Saudi Arabia's National Cybersecurity Authority, publisher of the essential controls."),
    ("https://www.sama.gov.sa/en-US/", "regional", ["grc"],
     "The Saudi central bank, whose cybersecurity framework is widely used as a Gulf reference."),
    ("https://siteq8.github.io/Markaz/", "regional", ["grc", "research"],
     "Kuwait's regulatory instruments published as open data, with crosswalks and research notes."),
]
