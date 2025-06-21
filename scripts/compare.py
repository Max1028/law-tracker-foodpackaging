import difflib

def compare_laws(old_list, new_list):
    diff = []
    old_titles = {item['title']: item for item in old_list}
    for new_item in new_list:
        title = new_item['title']
        old_item = old_titles.get(title)
        if not old_item:
            diff.append({
                "id": f"new-{title[:10]}",
                "title": new_item['title'],
                "date": new_item['date'],
                "old": "(無舊資料)",
                "new": new_item['content'] or new_item['link']
            })
        elif old_item.get("content") != new_item.get("content"):
            diff.append({
                "id": f"chg-{title[:10]}",
                "title": new_item['title'],
                "date": new_item['date'],
                "old": old_item.get("content") or old_item.get("link"),
                "new": new_item.get("content") or new_item.get("link")
            })
    return diff
