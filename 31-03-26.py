import time

start = time.perf_counter()

with open("f1_results.txt", "w") as f:
    f.write("Race: Australian GP\n")
    f.write("Winner: George Russell\n")
    f.write("Team: Mercedes\n")
    f.write("P2: Kimi Antonelli\n")
    f.write("P3: Charles Leclerc\n")
    f.write("\n")
    f.write("Race: Chinese GP\n")
    f.write("Winner: Kimi Antonelli\n")
    f.write("Team: Mercedes\n")
    f.write("P2: George Russell\n")
    f.write("Fastest Lap: Kimi Antonelli\n")
    f.write("\nRace: Japanese GP\n")
    f.write("Winner: Kimi Antonelli\n")
    f.write("Team: Mercedes\n")

print("=== File Written! ===")

with open("f1_results.txt", "r") as f:
    content = f.read()

print("=== Reading File ===")
print(content)

end = time.perf_counter()
print(f"Time taken: {(end - start):.6f} seconds")
