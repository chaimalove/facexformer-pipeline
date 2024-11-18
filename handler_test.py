from handler import EndpointHandler

h = EndpointHandler()

payload = {
    "inputs": "https://github.com/karaposu/facexformer-pipeline/blob/1c4cc2b75a1c796d734ffd113c29bf42648912bf/sample_image.jpg",
}

results = h(payload)

print(results)
