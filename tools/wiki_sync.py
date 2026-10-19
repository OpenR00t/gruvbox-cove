# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 The Gruvbox Cove contributors
"""Copy wikipedia/gruvbox-wikipedia.css to the account's global.css on Meta-Wiki (applies on every Wikimedia wiki).

Environment:
  WIKI_USER          bot-password login name, "Username@botname" (from Special:BotPasswords)
  WIKI_BOT_PASSWORD  the bot password
The bot password needs the grant "Edit your user CSS/JSON/JavaScript"."""
import http.cookiejar, json, os, pathlib, sys, urllib.parse, urllib.request

API = "https://meta.wikimedia.org/w/api.php"
CSS = pathlib.Path(__file__).resolve().parents[1] / "wikipedia" / "gruvbox-wikipedia.css"
login_name, password = os.environ["WIKI_USER"], os.environ["WIKI_BOT_PASSWORD"]
user = login_name.split("@", 1)[0]
repo = os.environ.get("GITHUB_REPOSITORY", "gruvbox-cove")
agent = f"gruvbox-cove-wiki-sync/1.0 (https://github.com/{repo})"
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

def call(params, post=False):
    params = {**params, "format": "json", "formatversion": "2"}
    data = urllib.parse.urlencode(params).encode() if post else None
    url = API if post else API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, data=data, headers={"User-Agent": agent})
    with opener.open(req, timeout=60) as r:
        out = json.load(r)
    if "error" in out:
        sys.exit(f"API error: {out['error'].get('code')}: {out['error'].get('info')}")
    return out

token = call({"action": "query", "meta": "tokens", "type": "login"})["query"]["tokens"]["logintoken"]
result = call({"action": "login", "lgname": login_name, "lgpassword": password, "lgtoken": token}, post=True)["login"]
if result.get("result") != "Success":
    sys.exit(f"Login failed: {result.get('reason', result.get('result'))}")
csrf = call({"action": "query", "meta": "tokens"})["query"]["tokens"]["csrftoken"]
title = f"User:{user}/global.css"
commit = os.environ.get("GITHUB_SHA", "")[:7]
edit = call({"action": "edit", "title": title, "text": CSS.read_text(encoding="utf-8"), "contentmodel": "css",
             "summary": f"Sync Gruvbox Cove theme {commit}".strip(), "token": csrf}, post=True)["edit"]
if edit.get("result") != "Success":
    sys.exit(f"Edit failed: {edit}")
print(f"{title}: {'no change' if edit.get('nochange') else 'updated, revision ' + str(edit.get('newrevid'))}")
