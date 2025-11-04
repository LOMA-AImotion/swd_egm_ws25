german_to_bav = {
    "Spaß": "Gaudi",
    "Großes Bier": "A Maß"
}


german_to_bav["Champignon"] = "Schwammerl"
german_to_bav["Choleriker"] = "Wuthaferl"

print(german_to_bav["Spaß"])

print(german_to_bav.get("mürrisch", "Not found"))
print(german_to_bav["mürrisch"])

