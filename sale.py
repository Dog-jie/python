import csv
totals = {}
with open("sales.csv",encoding="utf-8") as f :
	for row in csv.DictReader(f) :
		store = row["store"]
		amount = int(row["qty"]) * int(row["unit_price"])
		totals[store] = totals.get(store,0) + amount
with open("report.txt","w",encoding="utf-8") as f :
	for k, v in totals.items():
		f.write("f"{k}": {v}\n")
with open("summary.json","w",encoding="utf-8") as f :
	json.dump(totals,f,ensure_ascii=False,indent=2)
with open("summary.json",encoding="utf-8") as f :
	data = json.load(f)
		