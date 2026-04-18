import hashlib
import logging
import os 
import time
import json

def hash_file(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()
def create_snapshot(folder):
    snapshot = {}
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            snapshot[filename] = hash_file(filepath)
    return snapshot
def check_integrity(old_snapshot, new_snapshot):
    changes = []
    for filename, old_hash in old_snapshot.items():
        if filename not in new_snapshot:
            changes.append(f"DELETED: {filename}")
        elif new_snapshot[filename] != old_hash:
            changes.append(f"MODIFIED: {filename}")
    return changes
def save_snapshot(snapshot, filename="snapshot.json"):
    with open(filename, "w") as f:
        json.dump(snapshot, f, indent=4)

def load_snapshot(filename="snapshot.json"):
    with open(filename, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    start = time.perf_counter()
    folder = "."  # scan current directory

    # create and save initial snapshot
    logging.info("Creating initial snapshot...")
    snapshot1 = create_snapshot(folder)
    save_snapshot(snapshot1)
    logging.info(f"Snapshot saved! {len(snapshot1)} files tracked.")

    # simulate a change
    with open("test_file.txt", "w") as f:
        f.write("original content")

    # create new snapshot and compare
    logging.info("Checking integrity...")
    snapshot2 = create_snapshot(folder)
    changes = check_integrity(snapshot1, snapshot2)

    if changes:
        for change in changes:
            logging.warning(change)
    else:
        logging.info("No changes detected!")

    end = time.perf_counter()
    logging.info(f"Done in {end - start:.6f} seconds")
    
   