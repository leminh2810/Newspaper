import json

data = json.loads(output_str)
df = pd.DataFrame(data)
df.to_excel("output_table.xlsx", index=False)
