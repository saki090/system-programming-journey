import json
import os
import time

config = {
    "app_name": "Dumpies",
    "version": "1.0.0",
    "debug": False,
    "max_speed": 12.0000
}
def save_config(config, filename):
    with open(filename, "w") as f:
        json.dump(config, f, indent=5)
def load_config(filename):
    with open(filename, "r") as f:
        return json.load(f)
def update_config(filename, key, value):
    config = load_config(filename)
    config[key] = value
    save_config(config, filename)
    print(f"Update {key} to {value}")
if __name__ == "__main__":
    start = time.perf_counter()
    filename = "config.json"
save_config(config, filename)
print("===Config Saved!===")

loaded = load_config(filename)
print(f"\n=== Loaded Config===")
for key, value in loaded.items():
    print(f"{key}: {value}")

print("\n===Updating Config===")
update_config(filename, "debug", True)
update_config(filename, "max_speed", 350.0)

print("\n===Update Config===")
final = load_config(filename)
for key, value in final.items():
    print(f"{key}: {value}")

end = time.perf_counter()
print(f"\nTime taken: {end - start:.6f} seconds")