devices = ["R1", "R2", "S1"]
interfaces = ["Gi0/0/0.75", "Gi0/0/0.100", "Gi0/0/0.400"]

for devi in devices:
    for interf in interfaces:
        print(f"interface {interf}\n description This is interface {interf} in {devi}\n")