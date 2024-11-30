.PHONY: all
all: stimpresentation.json

stiminfo.json: rawstiminfo.json stiminfomaker.py
		python3 stiminfomaker.py < rawstiminfo.json > stiminfo.json

stimpresentation.json: stiminfo.json stimpresentationmaker.py
		python3 stimpresentationmaker.py < stiminfo.json > stimpresentation.json

.PHONY: clean
clean:
		rm stiminfo.json stimpresentation.json
