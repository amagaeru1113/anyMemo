"""
<?xml version='1.0' encoding='utf-8'>
<root>
    <employee>
        <employ>
            <id>111</id>
            <name>Mike</name>
        </employ>
        <employ>
            <id>222</id>
            <name>Nancy/name>
        </employ>
    </employee>
</root>

{
    "employee":
        [
            {"id": 111,"name": "Mike"},
            {"id": 222,"name": "Nancy},

        ]
}

"""

import json

j = {"employee": [{"id": 111, "name": "Mike"}, {"id": 222, "name": "Nancy"}]}

print(j)

print(json.dumps(j))
a = json.dumps(j)  # jsonにする

d = json.loads(a)  # dictにする

# 書き込みはできる
with open("test.json", "w") as f:
    json.dump(j, f)

with open("test.json", "r") as f:
    print(json.load(f))
