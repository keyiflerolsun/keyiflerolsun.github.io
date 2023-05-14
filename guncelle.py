# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ghapi.all import GhApi

api     = GhApi()
repolar = [
    repo for repo in api.repos.list_for_user(username="keyiflerolsun", per_page=100, sort="pushed")
        if repo.get("stargazers_count") >= 3
]
repolar = sorted(repolar, key=lambda veri: veri["stargazers_count"], reverse=True)

with open("__README.md", "r", encoding="utf-8") as dosya:
    eldeki_dosya = dosya.read()

eklenecek_metin = "".join(
    f"""
**[{repo.get("name")}](https://github.com/keyiflerolsun/{repo.get("name")})**

> *{repo.get("description").replace("|", "-")}*

* * *
"""
    for repo in repolar
)

with open("README.md", "w", encoding="utf-8") as dosya:
    dosya.write(eldeki_dosya.replace("{{ ÇOKOMELLİ }}", eklenecek_metin))