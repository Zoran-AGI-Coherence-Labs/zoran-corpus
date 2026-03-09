# gen_sbom.py — generate a minimal CycloneDX SBOM for current directory files
import os, json, hashlib
def sha256_of(path):
    h = hashlib.sha256()
    with open(path,"rb") as f:
        while True:
            b = f.read(65536)
            if not b: break
            h.update(b)
    return h.hexdigest()

def main():
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    comps = []
    for f in files:
        comps.append({
            "type":"file",
            "name":f,
            "version":"1.0",
            "hashes":[{"alg":"SHA-256","content":sha256_of(f)}]
        })
    sbom = {
        "bomFormat":"CycloneDX",
        "specVersion":"1.5",
        "version":1,
        "components": comps
    }
    print(json.dumps(sbom, indent=2))

if __name__ == "__main__":
    main()
