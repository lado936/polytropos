import json
basepath = "/dmz/github/etl4a/fixtures/2_mm_scan/data/entities/person"
for i in range(1, 10):
    fn = "person_%i.json" % i
    with open("%s/actual/%s" % (basepath, fn)) as in_fh, open("%s/expected/%s" % (basepath, fn), "w") as out_fh:
        correct = json.load(in_fh)
        json.dump(correct, out_fh, indent=2, sort_keys=False)