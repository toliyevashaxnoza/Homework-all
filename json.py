# 1.

import json
data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
data_matn = json.dumps(data)
print(data_matn)

# 2.

import json
talaba_json = """{"ism":"Shaxnoza","familiya":"Toliyeva","tyil":2006}"""
talaba = json.loads(talaba_json)
print(f"Familiya: {talaba['familiya']} Ism: {talaba['ism']}")

# 3.

file = "talaba.json"
with open(file, "w") as file:
 json.dump(data,file)


file = "talaba2.json"
with open(file, "w") as file:
 json.dump(talaba,file)




